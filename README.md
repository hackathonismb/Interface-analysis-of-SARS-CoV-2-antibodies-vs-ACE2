# SARS2 antibody interface analysis

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

![Interface flowchart](https://github.com/hackathonismb/Interface-analysis-of-SARS-CoV-2-antibodies-vs-ACE2/blob/main/images/flowchart.png?raw=true)

##
## Installation

Assuming you have cloned the git repository and are in the main repository folder. These steps are also found in the setup.md file.

### Setup a working node js version

One option to do this is to create a conda environment and install nodejs into a new environment

```cmd
conda create -n isbm2021hack nodejs
conda activate isbm2021hack
```

To continue you should have the node package manager (npm) available.

```cmd
npm --version
```

### install required node packages

```cmd
npm install three jquery axios querystring
npm install icn3d
```

### DelPhi calculation

Calculate the DelPhi potential map using a nodejs script.

```cmd
node bin/delphipot.js [PDB ID] [comma-separated Chain IDs] > data/[PBID]
```

The DelPhi potential map is now located in the data folder.

