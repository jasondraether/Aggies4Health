#!/bin/bash

echo "Counting JSON objects..."

for i in {01..16};
do
	for f in "../../data/pmdata/p${i}/fitbit/"*.json;
	do
		echo -n "${f}: "
		jq length "${f}"
	done
done

echo "Counting CSV lines..."

for i in {01..16};
do
        for f in "../../data/pmdata/p${i}/fitbit/"*.json;
        do
                wc -l "${f}"
        done
done

echo "Finished"

