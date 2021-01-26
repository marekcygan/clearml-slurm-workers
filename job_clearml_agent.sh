#!/bin/bash
#
#SBATCH --job-name=clearml_agent
#SBATCH --partition=common
#SBATCH --qos=lecturer
#SBATCH --gres=gpu:1
#SBATCH --output=/home/cygan/results/clearml_agent_%j.out
#SBATCH --error=/home/cygan/results/clearml_agent_%j.err

source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
workon clearml-agent
TRAINS_WORKER_ID=slurm_worker_$SLURM_JOB_ID stdbuf -o0 -e0 clearml-agent daemon --queue default --foreground 
