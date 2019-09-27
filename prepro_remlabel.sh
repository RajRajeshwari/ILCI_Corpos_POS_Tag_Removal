#!/bin/bash
mkdir -p ~/Desktop/temp1
python preprocessing.py
for file in $HOME/Desktop/temp1/*
do
  x="$(echo $file | sed 's/_out.txt/detokoutput.txt/g')"
  #$HOME/anusaaraka/miscellaneous/HANDY_SCRIPTS/
  ./detokenizer.perl < $file >$x
done
find $HOME/Desktop/temp1 -name '*_out.txt' -delete

