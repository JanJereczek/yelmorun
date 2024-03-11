"""
Author: Jan Swierczek-Jereczek
Date: 17.11.2021

Script to run retreat of WAIS based on AQEF.
It is possible to run this by directly typing the shell command... however that can be very tedious!
"""

#%% #####################################################
##################### Import packages ###################
#########################################################
import subprocess
import numpy as np
from header import run_header
run_header()

#%% #####################################################
####################### Run command #####################
#########################################################
cmd = "python2 base/yelmo_ismip6.py -l -f -a output/spinup"
cmd+= " \&ctrl=\"run_step=\"spinup_ismip6\"\""
cmd+= " \&spinup_ismip6=\"dtt=5.0\" \&spinup=\"time_end=30e3\""
cmd+= " \&ytopo=\"kt=3e-3\""
cmd+= " \&tf_corr_ant=\"ronne=0.25 ross=0.2 pine=0.0\""
cmd+= " \&yelmo=\"restart=\"None\"\""

# if resolution = 16km, some variables are named differently in nc files. 
# cmd+= " \&snap_clim1=\"clim_names=\"z_srf\" \"t2m_ann\" \"t2m_sum\" \"pr_ann\" \""

# print(cmd)
subprocess.call(cmd, shell=True)

# ./runylmox -r -e ismip6 -n par/yelmo_ismip6_Antarctica.nml -o output/ismip6/spinup_opt11 -p ctrl.run_step="spinup_ismip6" opt_L21.cf_min=1e-3 ytopo.kt=0.10e-2 tf_corr_ant.ronne=0.0 tf_corr_ant.ross=0.0