import os
import sys
sys.path.append('/data/g_gamazon_lab/wudh/PRS/Prscsgrex/')
import argparse
import gigrnd
import numpy as np
import pandas as pd
from numpy import linalg 
from numpy import random
from scipy.stats import norm
import re

parser = argparse.ArgumentParser(description='MCMC for TWAS results')
parser.add_argument('--twas_file', type=str, default=None,required=True)
parser.add_argument('--outdir', type=str, default=None,required=True)
parser.add_argument('--param_a', type=float, default=1)
parser.add_argument('--param_b', type=float, default=0.5)
parser.add_argument('--param_phi', type=float, default=None)
args = parser.parse_args()

# label="X250.22"
label=re.sub("/data/g_gamazon_lab/wudh/PRS/Prscsgrex/compiled_ukbb_TWAS_phecode_","",re.sub(".txt","",args.twas_file))
print(label,flush=True)
phi_updt=True
beta_std=False
seed=74711
random.seed(seed)
#sum stats info
n=400000
n_sqrt=np.sqrt(n)

##mcm parameters
n_iter=2000
n_burnin=1000
thin=5

##for debug
# out_dir="/data/g_gamazon_lab/wudh/PRS/Prscsgrex/results/"
# a=1
# b=0.5
# twas=pd.read_csv("/data/g_gamazon_lab/wudh/PRS/Prscsgrex/compiled_ukbb_TWAS_phecode_X250.2.txt",sep='\t')
# phi = None
##remaining params
out_dir=args.outdir
a=args.param_a
b=args.param_b
phi=args.param_phi

twas=pd.read_csv(args.twas_file,sep='\t')
#['gene', 'gene_name', 'tissue', 'phenotype', 'pvalue', 'effect_size','pred_perf_r2']
print(np.unique(twas['phenotype']), flush=True)


beta_std =np.sign(twas["effect_size"])*abs(norm.ppf(twas["pvalue"]/2.0))/n_sqrt
beta_mrg = np.array(beta_std, ndmin=2).T
n_pst = (n_iter-n_burnin)/thin
p=len(twas['gene'])

#initialization
beta = np.zeros((p,1))
psi = np.ones((p,1))
sigma = 1.0
if phi == None:
    phi = 1.0; phi_updt = True
else:
    phi_updt = False

beta_est = np.zeros((p,1))
psi_est = np.zeros((p,1))
sigma_est = 0.0
phi_est = 0.0

for itr in range(1,n_iter+1):
    print('iter-' + str(itr) + ' of '+str(n_iter+1),flush=True)


    quad = 0.0
    idx_blk = range(0,p)
    dinvt_inv = 1-(1.0/(1+psi[idx_blk]))
    dinvt_inv +=1e-100
    print('dinvt_inv_zero-' + str(any(dinvt_inv==0)),flush=True)
    beta[idx_blk]  = (dinvt_inv)*(beta_mrg) + np.sqrt(dinvt_inv)*np.sqrt(sigma/n)*random.randn(len(idx_blk),1)
    quad += sum(beta[idx_blk]*(1/dinvt_inv)*beta[idx_blk])
   

    err = max(n/2.0*(1.0-2.0*sum(beta*beta_mrg)+quad), n/2.0*sum(beta**2/psi))
    sigma = 1.0/random.gamma((n+p)/2.0, 1.0/err)

    delta = random.gamma(a+b, 1.0/(psi+phi))

    for jj in range(p):
        psi[jj] = gigrnd.gigrnd(a-0.5, 2.0*delta[jj], n*beta[jj]**2/sigma)
    #psi +=1e-300
    psi[psi>1] = 1.0
    print('psi_zero-' + str(any(psi==0)),flush=True)

    if phi_updt == True:
        w = random.gamma(1.0, 1.0/(phi+1.0))
        phi = random.gamma(p*b+0.5, 1.0/(sum(delta)+w))

    # posterior
    if (itr>n_burnin) and (itr % thin == 0):
        beta_est = beta_est + beta/n_pst
        psi_est = psi_est + psi/n_pst
        sigma_est = sigma_est + sigma/n_pst
        phi_est = phi_est + phi/n_pst



if phi_updt == True:
    eff_file = out_dir + '_pst_eff_a%d_b%.1f_phiauto_%s_sqrt(divint).txt' % (a, b, label)
else:
    eff_file = out_dir + '_pst_eff_a%d_b%.1f_phi%1.0e_%s_sqrt(divint).txt' % (a, b, phi, label)


with open(eff_file, 'w') as ff:
        for gene, tissue, beta in zip(twas['gene'], twas['tissue'], beta_est):
            ff.write('%s\t%s\t%.6e\n' % (gene, tissue, beta))

    # print estimated phi
if phi_updt == True:
    print('... Estimated global shrinkage parameter: %1.2e ...' % phi_est )

print('... Done ...')