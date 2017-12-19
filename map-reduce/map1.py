#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    elements = line.split(',')
    key = elements[10]
    value = ','.join([elements[0],elements[1],elements[11]])
    print('\t'.join([key,value]))