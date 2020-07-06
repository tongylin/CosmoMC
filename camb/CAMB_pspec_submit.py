import os, sys

# mass points in keV
mvec = [  1.        ,   1.27427499,   1.62377674,   2.06913808,
         2.6366509 ,   3.35981829,   4.2813324 ,   5.45559478,
         6.95192796,   8.8586679 ,  11.28837892,  14.38449888,
        18.32980711,  23.35721469,  29.76351442,  37.92690191,
        48.32930239,  61.58482111,  78.47599704, 100.        ]


for i in range(len(mvec)):
	print(i)
	os.system("cp nm4_base.ini nm4_run.ini")
	f = open('nm4_run.ini', "a")
	newout = """
output_root = /app/camb/outputs_pspec/nm4_mX""" + str(mvec[i]) + """
# DM scattering stuff
dm_scatter = T
mDM = """ + str(mvec[i]*1e-3) + """
sig0omDM = 1e-16
sig0omDMHe = 0
n = -4
dm_delta = F
sig0_zmean = 800.0
sig0_zwidth = 100
"""
	f.write(newout)
	f.close()
	os.system("./camb nm4_run.ini")