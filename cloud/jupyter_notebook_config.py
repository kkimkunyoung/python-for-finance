#
# Jupyter Notebook Congiguration File
# 
# Python for Finance, 2nd ed.
# (c) Dr. Yves J. Hilpisch
#

# SSL
c.ServerApp.certfile = '/root/.jupyter/cert.pem'
c.ServerApp.keyfile = '/root/.jupyter/cert.key'

# IP Address and Port
c.ServerApp.ip = '*'
c.ServerApp.port = 8888

# Password
c.PasswordIdentityProvider.hashed_password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$PoKlYPvMRBUfcQugN6OJvQ$+hH/eHCFwBP2WfdsdtBFS7mpQixcLCUdEdMZw26zWrM'

# Browser Option
c.ServerApp.open_browser = False
