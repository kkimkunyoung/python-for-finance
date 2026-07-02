#
# Dockerfile to Create
# Docker Image with
# Latest Ubuntu and Python
#
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#

# Latest Ubuntu Version
FROM ubuntu:latest

# Add Bash Script
ADD install.sh /

# Change Script Permission
RUN chmod u+x /install.sh

# Execute Bash Script
RUN /install.sh

# Add New Path
ENV PATH=/root/miniconda3/bin:$PATH

# Execute Python when Executing Container
CMD ["ipython"]
