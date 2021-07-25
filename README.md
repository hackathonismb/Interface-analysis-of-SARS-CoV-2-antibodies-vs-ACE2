# Interface analysis of SARS-CoV-2 antibodies vs ACE2

## Authors
- Marcus Mendes   mmendes@lji.org
- Mahita Jarjapu  mjarjapu@lji.org
- Henry Webel     henry.webel@cpr.ku.dk
- David Bell      david.bell@nih.gov

## Problem Statement

The Covid19 pandemic has been accompanied by the emergence of several SARS-CoV-2 variants. These variants have developed mutations that enable the SARS-CoV-2 Spike protein to more effectively bind the ACE2 receptor on the host cells, thereby increasing transmissibility of the virus into the host, as well as leading to reduced binding by neutralizing antibodies targeting the wild-type version of SARS-CoV-2.

Most of these mutations have appeared on the ACE2-binding region on Spike, called the receptor-binding domain (RBD). Investigating how these mutations alter the surface properties of the Spike:ACE2 binding interface will guide the design of therapeutic antibodies.

## How we solve the problem

### Goals
1. Characterize differences in surface properties (electrostatic) of ACE2-binding regions between SARS-CoV-2 variants.
2. Develop an inexpensive way to characterize these ACE2-RBD binding interfaces from PDB structures to predict binding potential
3. Create a methodology to compare the wild type and mutated spike proteins to predict if the mutation impacts antibody recognition.

### Approach
1. Collect all available SARS-CoV-2 structures of different variants 
2. Use iCn3D to extract ACE2-binding regions (RBD) on Spike
3. Compute electrostatic potential of each subregion for every structure
4. Break the RBD region into smaller subregions for each structure
5. Compare the electrostatic potential of corresponding subregions and compute a similarity score
   - Similarity scores  for all subregions for a pair of structures  is represented as a matrix 

### Workflow

![Interface flowchart](/Users/belldr/Documents/projects/ismb_hackathon_2021/flowchart/flowchart.pdf)


