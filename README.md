# PTRS-Bayes-CS [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/gamazonlab/PTRS-Bayes-CS/blob/main/LICENSE) 

#### Phenome-wide association scan and disease subtyping through a polygenic Bayesian continuous shrinkage framework applied to genetically determined transcriptomic data  
#### David H. Wu<sup>1</sup>, Nancy J. Cox<sup>2,3</sup>, Eric R. Gamazon<sup>2,3,*</sup>

<sup>1</sup>Medical Scientist Training Program, Vanderbilt University, Nashville, TN 37232  
<sup>2</sup>Vanderbilt Genetics Institute, Vanderbilt University, Nashville, TN 37232  
<sup>3</sup>Division of Genetic Medicine, Vanderbilt University Medical Center, Nashville, TN 37232  

<sup>*</sup>Correspondence:  eric.gamazon@vumc.org   
Repository maintained by:  davewu92@gmail.com  

### Abstract

With the growing size and abundance of large-scale biobanks containing genome-wide genetic information tied to patient electronic medical records (EMR), our ability to uncover novel disease-causing loci has dramatically improved. However, despite the increasing library of genetic associations, our limited ability to interpret the biological mechanisms mediating the effects of these loci and our subsequently deficient capacity to facilitate their integration into other fields of study has substantially reduced the impact of these discoveries.  To address these issues, many groups have worked to quantify the genetic contribution to gene expression (GReX) and have developed tools to interrogate the entire genetically determined transcriptome for its contribution to disease. Moreover, previous work has shown the advantages of building polygenic scores utilizing gene-based GReX quantifications akin to training locus-based polygenic scores. Here, we implement a methodology, termed PTRS-Bayes-CS, that can be used to both stratify disease subtypes and perform phenome-wide scans to discover other traits associated with the underlying genetic liability. In addition to our results showing markedly improved model performance over existing widely-used approaches, we also find evidence that our method can potentially provide higher resolution clinical utility in stratifying patients by disease severity. Taken together, this work demonstrates the advantages of a polygenic Bayesian framework, integrated with GReX models, for more immediate biological interpretation and greater clinical utility.

####INSTRUCTIONS
python library suggestions:

script built using Python 3.9.13

numpy >=1.21.5
pandas>=1.4.4
scipy >=1.9.1

Input file must be a  tab delimited compiled TWAS summary statistic across all tissues and genes with header:

gene    gene_name       tissue  phenotype       pvalue	effect_size     pred_perf_r2


The columns gene, tissue, pvalue, and effect_size must be present

Then use command (see prscs_grex_411.sh file in /data/ for example)

python PTRS_BAYES_CS.py --twas_file $PATH_TO_TWAS_SUM_STAT --outdir $PATH_TO_OUTPUT_DIR --param_a $PARAM_A  --param_b $PARAM_B --param_phi $PARAM_PHI

$PATH_TO_TWAS_SUM_STAT (required): path to file containing TWAS summary stats

$PATH_TO_OUTPUT_DIR (required): Path to folder for output files to be written to

$PARAM_A (optional): manually set value parameter A (default=1)

$PARAM_B (optional): manually set value parameter B (default=0.5)

$PARAM_PHI (optional): manually set value shrinkage parameter phi (default=None; i.e. learns from your data)


Output:

Tab-delimited File with no header and 3 columns: 

gene  tissue  weight
