import numpy as np
import os, sys
import argparse

keVtogram=1.78e-30

# mass points in MeV
mXvec = np.logspace(-3,0,15)
mXname = [str(round(mXvec[i]*1e4)/10.0) for i in range(len(mXvec))]

# sigma points in cm^2, converted to cm^2/gram. Taken from 2sigma PCA constraint
dat = np.loadtxt('Planck_PCA_sigma.dat').T 
sigvec = dat[1]/(mXvec*1e3*keVtogram)/3.0

# Write a new ini file with these mX, sigvec values and run camb for Cls

for i in range(len(mXvec)):
	print(i)
	os.system("cp nm4_base.ini nm4_run.ini")
	f = open('nm4_run.ini', "a")
	newout = """
output_root = /app/camb/outputs/nm4_mX""" + mXname[i] + """
# DM scattering stuff
dm_scatter = T
mDM = """ + str(mXvec[i]) + """
sig0omDM = """ + str(sigvec[i]) + """
sig0omDMHe = 0
n = -4
dm_delta = F
sig0_zmean = 800.0
sig0_zwidth = 100
"""
	f.write(newout)
	f.close()
	os.system("./camb nm4_run.ini")

	