#!/usr/bin/env python

"""
Extract residual information from PDB files

Map atoms to residual.
"""
__author__ = 'Mahita Jarapu'


from pathlib import Path


data_folder = Path('data')

with open (data_folder / 'list_residue_pot', 'r') as IFH1:
    for file in IFH1:
        file = file.strip("\n")
        name = file.split("_")[0]
        res_pot_dict = {}
        with open(data_folder / file, 'r') as IFH2:
            for line in IFH2:
                line = line.strip("\n")
                res_id = line.split(",")[0]
                pot_value = line.split(",")[1]
                if res_id not in res_pot_dict:
                    res_pot_dict[res_id] = float(pot_value)
            print(res_pot_dict)

    res_surface_area = {}
    with open(data_folder / f"{name}_surface", 'r') as IFH3:
        for i, line in enumerate(IFH3):
            if i > 0:
                line = line.strip("\n")
                fields = line.split(":")
                surface_area = fields[2].strip()
                res_details = fields[1]
                res_details_list = res_details.split(" ")
                res_full_id = res_details_list[1]
                res_full_id_list = res_full_id.split("_")
                # print(res_full_id_list)
                residue_id = res_full_id_list[2]+"_"+res_full_id_list[3]
                if residue_id not in res_surface_area:
                    res_surface_area[residue_id] = float(surface_area)
        print(res_surface_area)

        regions_dict = {}
        region_pot = 0
        region_number = 0
        for res_id in res_pot_dict.keys():
            # for some reason threw errors where some residues were not in surface area calculation
            if res_id not in res_surface_area.keys():
                res_no = int(res_id.split("_")[0])
                if res_no > 320 and res_no <= 530 and res_no % 10 == 0:
                    region_number = region_number + 1
                    regions_dict['region_{}'.format(region_number)] = region_pot
                    region_pot = 0

                continue

            res_no = res_id.split("_")[0]

            res_no = int(res_no)
            if res_no >= 320 and res_no <= 530:
                # if res_no <=340:

                if res_no > 320 and res_no % 10 == 0:
                    if res_surface_area[res_id] >= 80:
                        region_pot = region_pot + res_pot_dict[res_id]

                    elif res_surface_area[res_id] < 80:
                        region_pot = region_pot + 0

                    region_number = region_number + 1
                    regions_dict['region_{}'.format(region_number)] = region_pot
                    region_pot = 0

                elif res_no % 10 != 0:
                    if res_surface_area[res_id] >= 80:
                        region_pot = region_pot + res_pot_dict[res_id]

                    elif res_surface_area[res_id] < 80:
                        region_pot = region_pot + 0

        print(regions_dict)
