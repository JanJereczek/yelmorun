#%% #####################################################
##################### Import packages ###################
#########################################################
import subprocess
from header import run_header
path = run_header(yelmox_version = "v1.75")

#%% #####################################################
####################### Run command #####################
#########################################################
cmd = "python2 " + path + "/yelmo_ismip6.py -l -f -a output/control"
cmd+= " \&ctrl=\"run_step=\"hysteresis_proj\"\""
cmd+= " \&hysteresis_proj=\"time_end=30e3 dtt=1.0 dt1D_out=1.0 dt2D_out=1e3\""
cmd+= " \&hysteresis=\"dt2D_small_out=200\""
cmd+= " \&hyster=\"dt_init=100e3 method=\"PI42\" f_min=0 with_kill=False\""
cmd+= " \&yelmo=\"restart=\"" + path + "/output/spinup_alex/yelmo_restart.nc\"\""

# print(cmd)
# cmd = "pwd"
subprocess.call(cmd, shell=True)