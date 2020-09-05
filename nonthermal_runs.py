import os, sys

# mass points in keV
mvec = [  10, 15, 20, 25, 30, 35]

mXname = ['10','15','20','25','30','35', '40']
sigvec = [4.18618971e-13, 2.95009927e-13, 2.66773946e-13, 1.98396315e-13,
       1.30018684e-13, 9.75529944e-14, 8.23432138e-14]


for i in [5]: #range(2,len(mvec)):
	print(i)
	# first copy over correct equations_ppf to load the correct file
	os.system("cp camb/equations_ppf_R" + mXname[i] + ".f90 camb/equations_ppf.f90")
	# compile
	os.system("make clean")
	os.system("make")
	#### copy over script - first NO LENSING
	ini_name = "dmscat_" + mXname[i] + ".ini"
	os.system("cp test_dmscat.ini " + ini_name)
	f = open(ini_name, "a")
	newout = """
test_output_root = outputs/""" + str(mvec[i]) + """keV
CMB_lensing = F
param[mDM2mp] = """ + str(mvec[i]*1e3/938e6) + """
param[sigDMom] = """ + str(sigvec[i]) + """
"""
	f.write(newout)
	f.close()
	os.system("./cosmomc " + ini_name)
	#### WITH LENSING
	os.system("cp test_dmscat.ini " + ini_name)
	f = open(ini_name, "a")
	newout = """
test_output_root = outputs/""" + str(mvec[i]) + """keV_lensing
CMB_lensing = T
param[mDM2mp] = """ + str(mvec[i]*1e3/938e6) + """
param[sigDMom] = """ + str(sigvec[i]) + """
"""
	f.write(newout)
	f.close()
	#os.system("./cosmomc " + ini_name)