# Runs CAMB to get delta Cl for gaussian points.

#import numpy as np
import os, sys
#import argparse

keVtogram=1.78e-30

# mass points in MeV
#mXvec = np.logspace(-3,0,15)
#mXname = [str(round(mXvec[i]*1e4)/10.0) for i in range(len(mXvec))]

# - old values
#mXvec = [0.001     , 0.00163789, 0.0026827 , 0.00439397, 0.00719686,
#       0.01178769, 0.01930698, 0.03162278, 0.05179475, 0.08483429,
#       0.13894955, 0.22758459, 0.37275937, 0.61054023, 1.        ]
#mXname = ['1.0', '1.6', '2.7', '4.4', '7.2', '11.8', '19.3', '31.6', '51.8', '84.8', '138.9', '227.6', '372.8', '610.5', '1000.0']

mXvec = [0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04] 
mXname = ['10.0', '15.0','20.0', '25.0','30.0','35.0', '40.0']

# sigma points in cm^2, converted to cm^2/gram. Taken from 2sigma PCA constraint
#dat = np.loadtxt('Planck_PCA_sigma.dat').T 
#sigvec = dat[1]/(mXvec*1e3*keVtogram)/3.0
#sigvec = [3.20896572e-10, 5.64798485e-11, 8.76620800e-12, 1.89740883e-12,
#       5.90503429e-13, 3.09000779e-13, 2.76251396e-13, 1.07826360e-13,
#       4.64641117e-14, 2.53981054e-14, 1.51445277e-14, 9.24823105e-15,
#       5.66766443e-15, 3.46954805e-15, 2.12106484e-15]

sigvec = [4.18618971e-13, 2.95009927e-13, 2.66773946e-13, 1.98396315e-13,
       1.30018684e-13, 9.75529944e-14, 8.23432138e-14]

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

	