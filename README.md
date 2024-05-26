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
