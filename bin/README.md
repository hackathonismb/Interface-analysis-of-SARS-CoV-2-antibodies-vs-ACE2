

## Workflow

0.  Extract a single Ag chain from Ab-Ag complex using custom workflow
    - not provided is an automated way (biopython script/some other tools) to create a 
    list of `PDB_ID` and `Chain` pairs to store.
    ```
    # current format
    # <pdbid>_Ag_<chain>_rbd.pdb # pdbid and chain need to be extracted
    2dd8_Ag_S_rbd.pdb # example
    ```
1.  Create a currated list of all PDB files with their side-chain informatin
    - see [`data/list_pdb_files`](../data/list_pdb_files)
2.  Run `automate_delphical.sh` in the icn3d folder (for potential calculation) on all these files
    - after commenting out the code used for surface area calculation in the `delphipot_surface.js` script
    > [`delphipot.js`](delphipot.js) needs adaption to accomodate several options  
    > script has to be adapted. potentially change to snakemake
3.  Run `automate_delphical.sh` (for surface area/residue calculation) on all these files (in the icn3d folder) 
    - after commenting out the code used for electrostatic potential calculation in the `delphipot_surface.js` script
4.  Make list of output files generated in step 2 (`input_list_out`)
    - having suffix `*_out`
    - `out_files`: run script on files in folder `potentials`
5.  Make list of output files generated in step 3 (`list_surface_files`)
    - having suffix `*_surface`
    - `surface_files`: run script on files in folder `potentials_surface`
6.  Run `remove_undefined.py` on list from step 4, i.e. `input_list_out`
    - i.e. on files in folder `potentials`
7.  Make list of output files generated in step 6 (`list_clean_pot`)
    - put all into a new cleaned folder
8. Run `map_atom_to_res.py` using lists from step 7
    - after keeping output files and pdb files in the same folder
11. make list of csv files generated in step 8
12. keep surface files (filename format `<PDBID>_surface`) and .csv files in a single folder
13. run `group_into_regions.py` 
    - creates an output file `all_spike_strs_regions_pot.csv`
    - only keeps residues 320 to 530 
    > potentially previous processing could be restricted to region of interest