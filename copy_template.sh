#!/bin/bash

year=$(date +"%Y")
month=$(date +"%m")
day=$(date +"%d")

# Create a new directory
mkdir -p $year/$month/$day

# Copy the template file to the new directory
cp -r ./template/* $year/$month/$day
