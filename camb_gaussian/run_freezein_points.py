# Runs CAMB to get delta Cl for gaussian points.

#import numpy as np
import os, sys
#import argparse

keVtogram=1.78e-30

# mass points in MeV
#mXvec = np.logspace(-3,0,15)
#mXname = [str(round(mXvec[i]*1e4)/10.0) for i in range(len(mXvec))]

mXvec = [0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04] 
mXname = ['10.0', '15.0','20.0', '25.0','30.0','35.0', '40.0']

# sigma points in cm^2, converted to cm^2/gram. Taken from 2sigma PCA constraint
#dat = np.loadtxt('Planck_PCA_sigma.dat').T 
#sigvec = dat[1]/(mXvec*1e3*keVtogram)/3.0
sigvec = [4.18618971e-13, 2.95009927e-13, 2.66773946e-13, 1.98396315e-13,
       1.30018684e-13, 9.75529944e-14, 8.23432138e-14]

#mXvec = [.01]
#mXname = ['10.0']
#sigvec = [1e-12]
#mXvec = [.035]
#mXname = ['35.0']
#sigvec = [1e-13]

# Write a new ini file with these mX, sigvec values and run camb for Cls

for i in range(len(mXvec)):
	print(i)
	os.system("cp nm4_base.ini nm4_run.ini")
	f = open('nm4_run.ini', "a")
	newout = """
output_root = /app/camb_gaussian/outputs/nm4_mX""" + mXname[i] + """
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

	