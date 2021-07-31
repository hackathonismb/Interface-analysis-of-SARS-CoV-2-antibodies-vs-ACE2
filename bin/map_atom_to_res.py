#!/usr/bin/env python

"""
Extract residual information from PDB files

Map atoms to residual.
"""
__author__ = 'Mahita Jarapu'

IFH1 = open('list_of_pdb_files', 'r')
lines1 = IFH1.readlines()
for line1 in lines1:
    line1 = line1.strip("\n")
    pdb_name = line1.split("_")[0].lower()
    IFH2 = open(line1, 'r')
    res_dict = {}
    lines2 = IFH2.readlines()
    for i, line2 in enumerate(lines2):
        print(line2[0:4])
        print(line2[16:20].strip())
        print(line2[22:28].strip())
        res_dict[i] = line2[22:28].strip()+"_"+line2[16:20].strip()
    print(res_dict)
    IFH3 = open(pdb_name+"_clean", 'r')
    OFH3 = open(pdb_name+"_res_pot.csv", 'w')
    lines3 = IFH3.readlines()
    residue_pot = 0
    residue_pot_dict = {}
    for j, line3 in enumerate(lines3):
        if j == 0 and float(line3) == 0:

            for k in res_dict.keys():
                if j == k + 1:
                    line3 = line3.strip("\n")
                    residue_pot = residue_pot + float(line3)
                    # if k < len(res_dict.keys())-1:
                    if res_dict[k] != res_dict[k + 1]:
                        res_id = res_dict[k]
                        if res_id not in residue_pot_dict:
                            residue_pot_dict[res_id] = residue_pot
                        residue_pot = 0
        else:
            for k in res_dict.keys():
                if j == k + 1:
                    line3 = line3.strip("\n")
                    residue_pot = residue_pot + float(line3)
                    # if k < len(res_dict.keys())-1:
                    if res_dict[k] != res_dict[k + 1]:
                        res_id = res_dict[k]
                        if res_id not in residue_pot_dict:
                            residue_pot_dict[res_id] = residue_pot
                        residue_pot = 0

    print(residue_pot_dict)
    for res_id in residue_pot_dict.keys():
        OFH3.write("%s,%s\n" % (res_id, residue_pot_dict[res_id]))
    OFH3.close()
