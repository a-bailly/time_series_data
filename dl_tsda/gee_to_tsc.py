#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import sys
import numpy
import matplotlib.pyplot as plt

__author__ = 'adeline.bailly@univ-rennes2.fr'

def read_csv_cl(filename, _type = numpy.int, _start=2):
	with open(filename) as f:
		ncols = len(f.readline().split(','))
#	if(_start <> 1):
#		ncols += 1
	
	reader = numpy.genfromtxt(filename, delimiter=',', skip_header=True)[:, _start:]
	#numpy.loadtxt(filename, delimiter=',', skiprows=1, dtype=_type, usecols=range(_start,ncols)) 
	return reader

def read_csv_ts(filename, _type = numpy.int, _start=2):
	reader = numpy.genfromtxt(filename, delimiter=',', skip_header=True)[:, _start:]
	return reader

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if(len(argv) == 4):
		return argv[1], argv[2], argv[3]
    else:
		print('Need arguments: classes file, time series file, output file')
		sys.exit()

def nan_helper(y):
	return numpy.isnan(y), lambda z: z.nonzero()[0]

# Main

if __name__ == "__main__":
	classfile, tsfile, outfile = main()
	cl = read_csv_cl(classfile)
	ts = read_csv_cl(tsfile, numpy.float)
	
	# Old classes to new classes
	
	l = [2, 4, 7, 9]
	for i, e in enumerate(cl[:,:]):
		for ii, ee in enumerate(e):
			if ee in l:
				cl[i,ii] -= 1
	
	new_cl = numpy.array([0] * cl.shape[1], dtype=int)	
	for i in range(cl.shape[1]):
		if(cl[0,i] == cl[1,i] and cl[1,i] == cl[2,i]):
			new_cl[i] = cl[0,i]

	# Assemble infomations from different files
	
	dataset = numpy.c_[new_cl, numpy.transpose(ts)]

	# Remove unwanted classes
	
	l = [1, 2, 3, 4, 6, 7, 8, 9, 10, 12]
	indices = numpy.array([False] * dataset.shape[0], dtype=bool)
	
	for i, x in enumerate(new_cl):
		if x in l:
			indices[i] = True
		
	dataset = dataset[indices, :]

	# One-dimensional Linear Interpolation
	
	indices = numpy.array([True] * dataset.shape[0], dtype=bool)
	_len = dataset.shape[1]-1
	
	for i in range(0, dataset.shape[0]):
		if(numpy.count_nonzero(numpy.isnan(dataset[i,:])) == _len):
			indices[i] = False
	
	dataset = dataset[indices, :]
	
	x = numpy.linspace(0, _len-1, num=_len, endpoint=True)
	for i in range(0, dataset.shape[0]):
		if(numpy.count_nonzero(numpy.isnan(dataset[i,1:])) > 0):
			nans, x = nan_helper(dataset[i,1:])
			dataset[i,1:][nans] = numpy.interp(x(nans), x(~nans), dataset[i,1:][~nans])
	
#	print dataset.shape,
	
	# Save ready-to-use dataset
	
	numpy.savetxt(outfile, dataset, fmt='%.3e')
	
	if(False):
		l = [1, 3, 6, 8, 10, 12]
		for x in l:
			indices = (dataset[:, 0] == x)
			plt.plot(dataset[indices, 1:].transpose())
			plt.axis([0,_len,-0.5,1.0])
			s = 'class' + str(x)
			plt.savefig(s)
			plt.close()
	
