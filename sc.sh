#!/bin/bash

for file in ./*
do
	ffmpeg -i "$file" -ar 22050 "./preprocessed/${file:2}"	
done
