#%% #####################################################
##################### Import packages ###################
#########################################################
import string
import subprocess
import numpy as np
from header import run_header
path = run_header(yelmox_version = "v1.75")

#%% #####################################################
####################### Run command #####################
#########################################################

fmax_vec = np.round( np.arange(2.3, 2.85, 0.1), 2 )
a_vec = [0.05]
# a_vec = np.round( np.logspace( np.log10(1e-3), np.log10(5e-2), 10 ), 4)
rsl = 32

batch_name = "output/ramp4"

cmd = " jobrun ./runylmox -q short -w 24 -e ismip6 -n par/yelmo_ismip6_Antarctica_Rtip.nml -- -o "
cmd+= "output/ramp4"
cmd+= " ctrl.run_step=\"hysteresis_proj\""
cmd+= " hysteresis_proj.time_end=30e3 hysteresis_proj.dtt=1.0"
cmd+= " hysteresis_proj.dt1D_out=10.0 hysteresis_proj.dt2D_out=1e3"
cmd+= " hysteresis.dt2D_small_out=200 hysteresis.f_ta=1.0"
cmd+= " hyster.dt_init=5e3 hyster.method=\"ramp-slope\" hyster.df_sign=1"
cmd+= " hyster.f_min=0 hyster.with_kill=\"False\""
cmd+= " hyster.df_dt_max=0.05"
cmd+= " hyster.f_max=2.3,2.4,2.5,2.6,2.7,2.8"
cmd+= " isostasy.tau=1e2,5e2,1e3"
cmd+= " yelmo.restart=\"/p/projects/megarun/jan/yelmox/yelmox_v1.75/output/spinup_alex_v1.75/yelmo_restart.nc\""

print(cmd)
# subprocess.call(cmd, shell=True)

# i=0
# for fmax in fmax_vec:
#     for dfdt in a_vec:
#         i+=1

#         cmd = " jobrun ./runylmox -q short -w 24 -e ismip6 -n par/yelmo_ismip6_Antarctica_Rtip.nml -- -o "
#         cmd+= batch_name
#         # cmd+= " ctrl.run_step=\"hysteresis_proj\""
#         cmd+= " hysteresis_proj.time_end=30e3 hysteresis_proj.dtt=1.0"
#         # cmd+= " hysteresis_proj.dt1D_out=10.0 hysteresis_proj.dt2D_out=1e3"
#         # cmd+= " hysteresis.dt2D_small_out=200 hysteresis.f_ta=1.0"
#         # cmd+= " hyster.dt_init=5e3 hyster.method=\"ramp-slope\" hyster.df_sign=1"
#         # cmd+= " hyster.f_min=0 hyster.with_kill=False"
#         cmd+= " hyster.df_dt_max="+str(dfdt)
#         cmd+= " hyster.f_max="+str(fmax)
#         cmd+= " isostasy.tau=1e2,5e2,1e3"
#         # cmd+= " yelmo.restart=\"/p/projects/megarun/jan/yelmox/yelmox_v1.75/output/spinup_alex_v1.75/yelmo_restart.nc\""

#         print(cmd)
#         # subprocess.call(cmd, shell=True)


# ####### Ramp4 - Longer end time to make sure everythin that has to tip did? ###########
# fmax_vec = np.round( np.arange(2.3, 2.85, 0.1), 1)
# a_vec = np.round( np.logspace( np.log10(1e-3), np.log10(5e-2), 10 ), 4)

# # Batch 1 
# a_vec = a_vec[5:]

# # Batch 2
# a_vec = a_vec[:5]

# batch_name = "ramp4/1"

############# Ramp5 - Only oceanic warming ################
# fmax_vec = np.round( np.arange(2.4, 2.95, 0.1), 1)
# a_vec = np.round( np.logspace( np.log10(1e-3), np.log10(5e-2), 10 ), 4)

# # Batch 1 
# a_vec = a_vec[5:]

# # Batch 2
# a_vec = a_vec[:5]

# batch_name = "ramp5/1"