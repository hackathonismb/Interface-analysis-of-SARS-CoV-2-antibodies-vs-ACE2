#!/usr/bin/env python

IFH1 = open('list_residue_pot', 'r')
lines1 = IFH1.readlines()
for line1 in lines1:
    line1 = line1.strip("\n")
    name = line1.split("_")[0]
    res_pot_dict = {}
    IFH2 = open(line1, 'r')
    lines2 = IFH2.readlines()
    for line2 in lines2:
        line2 = line2.strip("\n")
        res_id = line2.split(",")[0]
        pot_value = line2.split(",")[1]
        if res_id not in res_pot_dict:
            res_pot_dict[res_id] = pot_value
    print(res_pot_dict)

    res_surface_area = {}
    IFH3 = open(name+"_surface", 'r')
    lines3 = IFH3.readlines()
    for i, line3 in enumerate(lines3):
        if i > 0:
            line3 = line3.strip("\n")
            fields = line3.split(":")
            surface_area = fields[2].strip()
            res_details = fields[1]
            res_details_list = res_details.split(" ")
            res_full_id = res_details_list[1]
            res_full_id_list = res_full_id.split("_")
            print(res_full_id_list)
            residue_id = res_full_id_list[2]+"_"+res_full_id_list[3]
            if residue_id not in res_surface_area:
                res_surface_area[residue_id] = surface_area
    print(res_surface_area)
    """
	regions_dict = {}
	region_pot = 0
	for res_id in res_pot_dict.keys():
		res_no = res_id.split("_")[0]
		

		res_no = int(res_no)
		if res_no >= 320 and res_no <= 530:
			if res_no <=340:

				if res_surface_area[res_id] > 80:
					region_pot = region_pot + res_pot_dict[res_id]

			regions_dict['region_1']

			elif res_no >340 and res_no <
	for i in range(320,531):
	"""
