#!/bin/bash
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
workon clearml-agent
python /home/cygan/utils/spin_clearml_agents.py
