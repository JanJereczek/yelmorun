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
path = run_header(yelmox_version = "v1.75")

#%% #####################################################
####################### Run command #####################
#########################################################

cmd = "python2 yelmo_ismip6.py -l -f -a output/aqef_retreat"
cmd+= " \&ctrl=\"run_step=\"hysteresis_proj\"\""
cmd+= " \&hysteresis_proj=\"time_end=130e3 dtt=1.0 dt1D_out=1.0 dt2D_out=1e3\""
cmd+= " \&hysteresis=\"dt2D_small_out=100\""
cmd+= " \&hyster=\"dt_init=1e3 method=\"PI42\" df_sign=1 f_min=0 f_max=5.5 df_dt_max=5e-4 with_kill=False\""
cmd+= " \&yelmo=\"restart=\"/home/janswier/yelmo-ucm/yelmox_v1.75/output/spinup_alex/yelmo_restart.nc\"\""
# cmd+= " \&ydyn=\"ssa_lis_opt=\"-i idrs -p ssor -maxiter 100 -tol 1.0e-1 -initx_zeros false\"\""

#print(cmd)
subprocess.call(cmd, shell=True)