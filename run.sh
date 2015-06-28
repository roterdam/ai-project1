#!/usr/bin/env bash

echo `python RavensProject.py`
cat SetResults.csv|while read line
do
    echo "$line"
done
echo " "