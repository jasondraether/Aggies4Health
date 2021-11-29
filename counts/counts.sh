#!/bin/bash


#for i in {01..16};
#do
#	for f in "../../data/pmdata/p${i}/fitbit/"*.json;
#	do
#		echo -n "${f}: "
#		jq length "${f}"
#	done
#done

for i in {01..16};
do
        for f in "../../../data/pmdata/p${i}/googledocs/"*.csv;
        do
                wc -l "${f}"
        done
done


