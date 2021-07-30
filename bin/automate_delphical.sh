#!/usr/bin/bash

for i in $(cat list_pdb_files);
do

	#${A}= "$(cut -d'_' -f1 <<<"$i")"
	#echo "$A"


	#${B}= "$(cut -d'_' -f4 <<<"$i")"
	#echo "$B"

	A=$(awk -F_ '{print $1}' <<< ${i})
	B=$(awk -F_ '{print $3}' <<< ${i})

	echo "delphipot_surface.js ${A} ${B} > ${A}_out"
	node delphipot_surface.js ${A} ${B} > ${A}_surface

done