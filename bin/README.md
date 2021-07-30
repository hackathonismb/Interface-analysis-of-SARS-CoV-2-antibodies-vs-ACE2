

## Workflow

1.  Extract a single Ag chain from Ab-Ag complex using custom Biopython script
2.  Rename PDB containing single Ag chain to include pdb id and chain id
3.  Create list of all PDB files created in step 2 (`list_pdb_files`)
4.  Run `automate_delphical.sh` in the icn3d folder (for potential calculation) on all these files
    - after commenting out the code used for surface area calculation in the `delphipot_surface.js` script
5.  Run `automate_delphical.sh` (for surface area/residue calculation) on all these files (in the icn3d folder) 
    - after commenting out the code used for electrostatic potential calculation in the `delphipot_surface.js` script
6.  Make list of output files generated in step 4 (`input_list_out`)
7.  Make list of output files generated in step 5 (`list_surface_files`)
8.  Run `remove_undefined.py` on list from step 6
9.  Make list of output files generated in step 8 (`list_clean_pot`)
10. Run `map_atom_to_res.py` using lists from step 9 after keeping output files and pdb files in the same folder
11. make list of csv files generated in step 10
12. keep surface files (filename format `<PDBID>_surface`) and .csv files in a single folder
13. run `group_into_regions.py` - creates an output file `all_spike_strs_regions_pot.csv`


- currently: start at step 4 ()