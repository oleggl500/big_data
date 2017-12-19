#!/usr/bin/env python
# coding=utf-8
import sys
import math

prodTime = []
vals = []
n = 0

for line in sys.stdin:
	
	_,keys,values = line.split('\t')
	prodTime_from_reducer = keys.split(',')
	n += len(prodTime_from_reducer)
	prodTime.append(prodTime_from_reducer)
	vals.append(values.split(','))

for i in range(n):
	min_idx = 0
	min_val = float('inf')
	for idx in range(0,len(prodTime)):
		if len(prodTime[idx]) > 0:
			if float(prodTime[idx][0]) < min_val:
				min_idx = idx
				min_val = float(prodTime[idx][0])
	if i > math.ceil(0.95*n):
		break
	if i < math.ceil(0.05*n):
		prodTime[min_idx].pop(0)
		vals[min_idx].pop(0)
		vals[min_idx].pop(0)
		vals[min_idx].pop(0)
	else:
		prodTime[min_idx].pop(0)
		aN = vals[min_idx].pop(0)
		eventFile = vals[min_idx].pop(0)
		Pt = vals[min_idx].pop(0)
		print('\t'.join([aN,','.join([eventFile,Pt])]))