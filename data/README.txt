python library suggestions:

script built using Python 3.9.13

numpy >=1.21.5
pandas>=1.4.4
scipy >=1.9.1

Input file must be a  tab delimited compiled TWAS summary statistic across all tissues and genes with header:

gene    gene_name       tissue  phenotype       pvalue	effect_size     pred_perf_r2


The columns gene, tissue, pvalue, and effect_size must be present

Then use command (see command.sh file in /data/ for example)

python PTRS_BAYES_CS.py --twas_file $PATH_TO_TWAS_SUM_STAT --outdir $PATH_TO_OUTPUT_DIR --param_a $PARAM_A  --param_b $PARAM_B --param_phi $PARAM_PHI

$PATH_TO_TWAS_SUM_STAT (required): path to file containing TWAS summary stats
$PATH_TO_OUTPUT_DIR (required): Path to folder for output files to be written to
$PARAM_A (optional): manually set value parameter A (default=1)
$PARAM_B (optional): manually set value parameter B (default=0.5)
$PARAM_PHI (optional): manually set value shrinkage parameter phi (default=None; i.e. learns from your data)


Output:
Tab-delimited File with no header and 3 columns: 
gene  tissue  weight





