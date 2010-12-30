from Config import *
from ftplib import FTP

ftp = FTP(ftpserver,ftpuser,ftppwd)

# upload as binary file
ftp.storbinary("STOR sample.xml",file('sample.xml'))

# download as binary file
out = file('downloaded.xml','wb')
ftp.retrbinary("RETR sample.xml", out.write)
out.close()
