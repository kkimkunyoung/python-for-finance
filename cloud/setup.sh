#!/bin/bash
# 
# Script to Install
# DigitalOcean Droplet,
# Basic Python Components,
# and Jupyter Notebook
# 
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#

# Get IP Address as Argument
MASTER_IP=$1

# Copy Files
scp install.sh root@${MASTER_IP}:
scp cert.* jupyter_notebook_config.py root@${MASTER_IP}:

# Execute install.sh
ssh root@${MASTER_IP} bash /root/install.sh
