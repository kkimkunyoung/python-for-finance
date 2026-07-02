#!/bin/bash
#
# Script to Install
# Linux System Tools,
# Basic Python Components,
# and Jupyter Notebook Server
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#

# Linux General
apt-get update
apt-get upgrade -y
apt-get install -y bzip2 gcc git htop screen vim wget
apt-get upgrade -y bash
apt-get clean

# Install Miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda.sh
bash Miniconda.sh -b
rm -rf Miniconda.sh

# Add New Path
export PATH="/root/miniconda3/bin:$PATH"

# Add New Path Variable to Settings File
echo ". /root/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate" >> ~/.bashrc

# Accept ToS Before Installing Python Libraries
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# Install Python Libraries
conda update -y conda
conda create -y --name py4fi python
source activate py4fi
conda install -y jupyter
conda install -y pytables
conda install -y pandas
conda install -y matplotlib
conda install -y scikit-learn
conda install -y openpyxl
conda install -y pyyaml

pip install --upgrade pip
pip install cufflinks

# Copy Files and Create Directories
mkdir /root/.jupyter
mv /root/jupyter_notebook_config.py /root/.jupyter/
mv /root/cert.* /root/.jupyter
mkdir /root/notebook
cd /root/notebook

# Run Jupyter Notebook
jupyter notebook --allow-root

# If Running Jupyter Notebook on Background
# jupyter notebook --allow-root &
