#!/usr/bin/env python
# coding=utf-8

import os
import sys
import fileinput
import re

# keyword
beginConsonants = "ngh|ch|gh|gi|kh|nh|ng|ph|th|tr|qu|tx|b|c|d|g|h|k|l|m|n|p|q|r|s|t|v|x"
endConsonants   = "ch|nh|ng|c|m|n|p|t"

# Preparing the file
f_input  = open(sys.argv[1], "r", encoding="utf-8")
f_output = open(sys.argv[2], "w", encoding="utf-8")

# Replace the target string
for line in f_input:
    # re-write original word
    f_output.write(line.replace(" sp", ""))

# Closing the file
f_input.close()
f_output.close()