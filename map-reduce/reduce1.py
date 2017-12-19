#!/usr/bin/env python
# coding=utf-8
import sys

sorted_keys = []
sorted_vals = []

for line in sys.stdin:
	
	key,value = line.split('\t')
	antiNucleus,eventFile, Pt = value.split(',')
	sorted_keys.append(key)
	sorted_vals.append(str(int(antiNucleus)))
	sorted_vals.append(eventFile)
	sorted_vals.append(str(float(Pt)))

# print("key" + "\t" + ",".join(sorted_keys) + "\t" + ",".join(sorted_vals) )
print('\t'.join(["key", ",".join(sorted_keys), ",".join(sorted_vals)]))