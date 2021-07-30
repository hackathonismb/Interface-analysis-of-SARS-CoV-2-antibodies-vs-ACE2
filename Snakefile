"""
Snakemake workflow file
https://snakemake.readthedocs.io/

Run all scripts to produce final results
"""

from pathlib import Path
configfile: 'config.yaml'  # access using config['key']


config['DATADIR'] = Path(config['DATADIR'])
config['SCRIPTDIR'] = Path(config['SCRIPTDIR'])
with open(config['DATADIR'] / config['INFILE']) as f:
    # format: 2dd8_Ag_S_rbd.pdb
    PDB_IDS = []
    CHAINS = []
    for line in f:
        line = line.split('_')
        PDB_IDS.append(line[0])
        CHAINS.append(line[2])


rule target:
    input:
        expand(config['DATADIR'] / 'potentials' / "{pdb_id}_{chain}_out.txt", 
               zip,
               pdb_id=PDB_IDS,
               chain=CHAINS)


rule calculate_potential:
    output:
        config['DATADIR'] / 'potentials' / "{pdb_id}_{chain}_out.txt"
    params:
        config['SCRIPTDIR'] / 'delphipot.js'
    shell:
        "node {params} {wildcards.pdb_id} {wildcards.chain} > {output}"
