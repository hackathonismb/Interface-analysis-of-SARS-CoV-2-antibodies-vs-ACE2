#!/usr/bin/env python

"""
Extract residual information from PDB files

Map atoms to residual.
"""
from pathlib import Path
import argparse
__author__ = 'Mahita Jarapu'

OUTFILE_TEMPLATE = '{}_clean'


def get_args():
    parser = argparse.ArgumentParser(
        'remove undefined potentials from residuals files.')
    parser.add_argument(
        '-f', '--folder', help='Folder with potential files to clean.')
    args = parser.parse_args()
    return args


args = get_args()

folder = Path(args.folder)

for _file in folder.iterdir():
	delphi_value_dict = {}
	outfile = OUTFILE_TEMPLATE.format(_file) 
	with open(_file) as f, open(outfile, 'w') as OFH2:
		header = next(f)
		# add check that header is as expected?
		for i, line in enumerate(f, start=1):
			# example: 7CDJ_E_333 : -35.06
			line = line.strip("\n").split(":")
			delphi_value = line[1]
			delphi_value_dict[i] = delphi_value # change to position in AG?

		for line_no in delphi_value_dict.keys():
			# print(line_no)
			"""What about NaN values

			Idea is to
			- replace undefined / NaN with 0 if the value before or after is defined?
			"""
			if delphi_value_dict[line_no] == ' undefined':
				if (line_no + 1) < (len(delphi_value_dict.keys())):
					if delphi_value_dict[line_no + 1] != ' undefined':
						delphi_value_dict[line_no +
										1] = delphi_value_dict[line_no + 1].strip()
						OFH2.write("%s\n" % (0)) # only write 0 if next is also not undef
					elif delphi_value_dict[line_no - 1] != ' undefined':
						delphi_value_dict[line_no -
										1] = delphi_value_dict[line_no - 1].strip()
						OFH2.write("%s\n" % (0))
			elif delphi_value_dict[line_no] != ' undefined':
				delphi_value_dict[line_no] = delphi_value_dict[line_no].strip()
				OFH2.write("%s\n" % (delphi_value_dict[line_no]))
