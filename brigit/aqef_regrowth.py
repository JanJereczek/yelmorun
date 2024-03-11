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
from header import run_header
run_header()

#%% #####################################################
####################### Run command #####################
#########################################################
cmd = "python2 yelmo_aqef.py -l -f -a output/aqef_regrowth/"
cmd+= " \&tf_corr_ant=\"ronne=0.25 ross=0.2 pine=-0.5\"  \&hysteresis_proj=\"time_end=300e3 dtt=1.0\""
cmd+= " \&hysteresis=\"dt2D_small_out=50e3\""
cmd+= " \&hyster=\"dt_init=10e3 df_sign=-1 f_min=-5 f_max=5.5 df_dt_max=2e-4 eps=10\""
cmd+= " \&yelmo=\"restart=\"/home/janswier/yelmo-ucm/yelmox_v1.662/output/aqef_retreat/dtt.1.0_tend.130000/yelmo_restart.nc\" dt_method=2\""
cmd+= " \&ydyn=\"ssa_lat_bc=\"floating\"\""

# print(cmd)
subprocess.call(cmd, shell=True)