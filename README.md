# PTRS-Bayes-CS [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/gamazonlab/PTRS-Bayes-CS/blob/main/LICENSE) 

#### David H. Wu<sup>1</sup>, Nancy J. Cox<sup>2,3</sup>, Eric R. Gamazon<sup>2,3,*</sup>

<sup>1</sup>Medical Scientist Training Program, Vanderbilt University, Nashville, TN 37232  
<sup>2</sup>Vanderbilt Genetics Institute, Vanderbilt University, Nashville, TN 37232  
<sup>3</sup>Division of Genetic Medicine, Vanderbilt University Medical Center, Nashville, TN 37232  

<sup>*</sup>Correspondence:  eric.gamazon@vumc.org   
Repository maintained by:  davewu92@gmail.com  

#### INSTRUCTIONS
python library suggestions:

script built using Python 3.9.13

numpy >=1.21.5
pandas>=1.4.4
scipy >=1.9.1

Input file must be a tab delimited compiled TWAS summary statistic across all tissues and genes with header:

gene&nbsp;&nbsp;&nbsp;&nbsp;gene_name&nbsp;&nbsp;&nbsp;&nbsp;tissue&nbsp;&nbsp;&nbsp;&nbsp;pvalue&nbsp;&nbsp;&nbsp;&nbsp;effect_size&nbsp;&nbsp;&nbsp;&nbsp;pred_perf_r2


The columns gene, tissue, pvalue, and effect_size must be present

Then use command (see command.sh file in /data/ for example):

python PTRS_BAYES_CS.py --twas_file $PATH_TO_TWAS_SUM_STAT --outdir $PATH_TO_OUTPUT_DIR --param_a $PARAM_A  --param_b $PARAM_B --param_phi $PARAM_PHI

The options are:
$PATH_TO_TWAS_SUM_STAT (required): path to file containing TWAS summary stats

$PATH_TO_OUTPUT_DIR (required): Path to folder for output files to be written to

$PARAM_A (optional): manually set value parameter A (default=1)

$PARAM_B (optional): manually set value parameter B (default=0.5)

$PARAM_PHI (optional): manually set value shrinkage parameter phi (default=None; i.e. learns from your data)


Output:

Tab-delimited File with no header and 3 columns: 

gene&nbsp;&nbsp;&nbsp;&nbsp;tissue&nbsp;&nbsp;&nbsp;&nbsp;weight
