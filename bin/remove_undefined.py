#!/usr/bin/env python

"""
Extract residual information from PDB files

Map atoms to residual.
"""
__author__ = 'Mahita Jarapu'

IFH1 = open('input_list_out', 'r') 
lines1 = IFH1.readlines()
for line1 in lines1:
	line1 = line1.strip("\n")
	IFH2 = open(line1, 'r')
	OFH2 = open(line1.split("_")[0]+'_'+'clean', 'w')
	IFH2 = open(line1, 'r')
	lines2 = IFH2.readlines()
	print(line1)
	delphi_value_dict = {}
		
	for i,line2 in enumerate(lines2):
		if i > 0:
			line2 = line2.strip("\n").split(":")
			delphi_value = line2[1]
			delphi_value_dict[i] = delphi_value
		#print(delphi_value)
		#if delphi_value == ' undefined':
			#if previous.strip("\n").split(":")[1] != ' undefined':
				#OFH2.write("%s\n"%(delphi_value))
	print(len(delphi_value_dict.keys()))
	for line_no in delphi_value_dict.keys():
		#print(line_no)
		

		
		if delphi_value_dict[line_no] == ' undefined':
			if (line_no + 1) < (len(delphi_value_dict.keys())):
				if delphi_value_dict[line_no + 1] != ' undefined':
					delphi_value_dict[line_no + 1] = delphi_value_dict[line_no + 1].strip()
					OFH2.write("%s\n"%(0))
				elif delphi_value_dict[line_no - 1] != ' undefined':
					delphi_value_dict[line_no - 1] = delphi_value_dict[line_no - 1].strip()
					OFH2.write("%s\n"%(0))
		elif delphi_value_dict[line_no] != ' undefined':
			delphi_value_dict[line_no] = delphi_value_dict[line_no].strip()
			OFH2.write("%s\n"%(delphi_value_dict[line_no]))
			
	OFH2.close()
	IFH2.close()
IFH1.close()