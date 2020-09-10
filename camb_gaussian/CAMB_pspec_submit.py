import os, sys

# mass points in keV
mvec = [  1.        ,   1.27427499,   1.62377674,   2.06913808,
         2.6366509 ,   3.35981829,   4.2813324 ,   5.45559478,
         6.95192796,   8.8586679 ,  11.28837892,  14.38449888,
        18.32980711,  23.35721469,  29.76351442,  37.92690191,
        48.32930239,  61.58482111,  78.47599704, 100.        , 
		130., 150., 200.]

mvec = [10, 15, 20, 25, 30, 35]
sigvec_FI = [2.95170297e-12, 7.32095846e-13, 2.79655917e-13, 1.35255836e-13,
 7.50191872e-14, 4.49840860e-14]

for i in range(len(mvec)):
	print(i)
	os.system("cp nm4_base.ini nm4_run.ini")
	f = open('nm4_run.ini', "a")
	newout = """
output_root = /app/camb_gaussian/outputs_pspec/nm4_mX""" + str(mvec[i]) + """
# DM scattering stuff
dm_scatter = T
mDM = """ + str(mvec[i]*1e-3) + """
sig0omDM = """ + str(1e-17) + """
sig0omDMHe = 0
n = -4
dm_delta = F
sig0_zmean = 800.0
sig0_zwidth = 100
"""
	f.write(newout)
	f.close()
	os.system("./camb nm4_run.ini")