import subprocess
from header import run_header
run_header()
cmd = "pwd";
subprocess.call(cmd, shell=True)