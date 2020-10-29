#!/bin/bash
#
#SBATCH --job-name=trains_agent
#SBATCH --partition=common
#SBATCH --qos=lecturer
#SBATCH --gres=gpu:1
#SBATCH --output=/home/cygan/results/trains_agent_%j.out
#SBATCH --error=/home/cygan/results/trains_agent_%j.err

source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
workon trains-agent
TRAINS_WORKER_ID=slurm_worker_$SLURM_JOB_ID stdbuf -o0 -e0 trains-agent daemon --queue default --foreground 
