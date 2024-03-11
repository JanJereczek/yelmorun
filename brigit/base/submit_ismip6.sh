#!/bin/bash
#BATCH -n 1
#SBATCH -p short
#SBATCH -J spinup
#BATCH --mem=2Gb
#SBATCH -t 0-23:30:00
#SBATCH -o yelmo.out
#SBATCH -e yelmo.err

# Run the job
./yelmox_ismip6.x yelmo_ismip6_Antarctica.nml