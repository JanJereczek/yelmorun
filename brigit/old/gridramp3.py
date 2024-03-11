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
dfdt1 = np.arange(2e-3, 1.2e-2, 2e-3)
dfdt2 = np.arange(2e-2, 5.1e-2, 1e-2)
dfdt_vec = np.round( np.concatenate((dfdt1, dfdt2)), 5)
dfdt_vec = np.flip(dfdt_vec)        # flip to have most interesting exp at begin
# print(dfdt_vec)
fmax_vec = np.flip(np.round(np.arange(3.8, 4.01, f_resolution), 2))

i=0
for fmax in fmax_vec:
    for dfdt in dfdt_vec:
        i+=1
        print(i, dfdt)
        dt_ramp = np.round(fmax/dfdt, 2)
        cmd = "python2 run_my_yelmo.py -l -f -a output/ramp/GridRamp3/1"
        cmd+= " \&tf_corr_ant=\"ronne=0.25 ross=0.2 pine=-0.5\" \&hysteresis_proj=\"time_end=75e3\" \&hyster=\"dt_init=5e3"
        cmd+= " dt_ramp="+str(dt_ramp)
        cmd+= " f_max="+str(fmax)+"\""
        cmd+= " \&ytherm=\"H_w_max=20\""
        cmd+= " \&yelmo=\"restart=\"/home/janswier/yelmo-ucm/yelmox_v1.662/output/ctrl_Hwmax.2_tend.10000/yelmo_restart.nc\" dt_method=2\""
        # print(cmd)
        subprocess.call(cmd, shell=True)
# %%
