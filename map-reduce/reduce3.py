#!/usr/bin/env python
# coding=utf-8
import sys

mean = 0
n = 0
uq_set = set()
cur_key = ""

for line in sys.stdin:
	
	key,value = line.split('\t')
	eventFile, Pt = value.split(',')
	if key != cur_key:
		if cur_key != "":
			print(cur_key + '\t' + str(mean/n) + '\t' + str(len(uq_set)) )
		mean = 0
		n = 0
		uq_set = set()
		cur_key = key

	uq_set.add(eventFile)
	mean += float(Pt)
	n += 1

print(cur_key + '\t' + str(mean/n) + '\t' + str(len(uq_set)) )
