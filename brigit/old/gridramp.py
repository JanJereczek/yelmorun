"""
Author: Jan Swierczek-Jereczek
Date: 01.12.2021

Somewhat hacky script to run the ramp experiments on brigit.
Why hacky? We cannot start batches easily on brigit --> call Ilaria's script.
However Ilaria's script designed to run permutations and WE DO NOT WANT PERMUTATIONS here.
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
f_resolution = 0.1
"""
dfdt1 = np.arange(2e-3, 1.2e-2, 2e-3)
dfdt2 = np.arange(2e-2, 5.1e-2, 1e-2)
dfdt_vec = np.round( np.concatenate((dfdt1, dfdt2)), 5)
dfdt_vec = np.flip(dfdt_vec)        # flip to have most interesting exp at begin
# print(dfdt_vec)
"""
dfdt_vec = np.array([1e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2, 5e-2])
fmax_vec = np.array([4, 4.5, 5, 5.5])

# dfdt_vec = np.array([5e-5])
# fmax_vec = np.arange(3.0, 6.0, 0.5)
# print(cmd)
# subprocess.call(cmd, shell=True)

# for regrowth, fmax = 6.55 and:
# cmd+= " \&yelmo=\"restart=\"/home/janswier/yelmo-ucm/yelmox_v1.73/output/aqef_retreat/kt.1e-3/retreat/yelmo_restart.nc\"\""

i=0
for fmax in fmax_vec:
    for dfdt in dfdt_vec:
        i+=1
        print(i, dfdt)
        dt_ramp = np.round(fmax/dfdt, 2)
        cmd = "python2 yelmo_ismip6.py -l -f -a output/gridramp/kt.1e-3"
        cmd+= " \&ctrl=\"run_step=\"hysteresis_proj\"\""
        cmd+= " \&hysteresis_proj=\"time_end=70e3 dtt=1.0 dt1D_out=1.0 dt2D_out=1e3\""
        cmd+= " \&hysteresis=\"dt2D_small_out=200\""
        cmd+= " \&hyster=\"dt_init=5e3 method=\"ramp-time\" df_sign=1 f_min=0 with_kill=False"
        cmd+= " dt_ramp="+str(dt_ramp)
        cmd+= " f_max="+str(fmax)+"\""
        cmd+= " \&tf_corr_ant=\"ronne=0.25 ross=0.2 pine=0.0\""
        cmd+= " \&ytopo=\"kt=1e-3\""
        cmd+= " \&yelmo=\"restart=\"/home/janswier/yelmo-ucm/yelmox_v1.73/output/control/2/yelmo_restart.nc\"\""

        # print(cmd)
        subprocess.call(cmd, shell=True)
# %%
