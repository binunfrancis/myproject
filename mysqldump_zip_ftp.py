import os
import zipfile
import ftplib
import os.path
from datetime import datetime

datestring = datetime.strftime(datetime.now(), '%Y%m%d')


os.chdir("C:\\Users\\webserver\\Downloads")
if os.path.exists('spo.sql'):
    os.mkdir(datestring)
    os.rename('./spo.sql','./'+datestring+'/backupspo.sql')



os.system("mysqldump -u root -proot -h localhost test>C:\\Users\\webserver\\Downloads\\spo.sql")


jungle_zip = zipfile.ZipFile('C:\\Users\\webserver\\Downloads\\spo.zip', 'w')
jungle_zip.write('./spo.sql', compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()

session = ftplib.FTP('192.168.1.142','test','123456')
file = open('C:\\Users\\webserver\\Downloads\\spo.zip','rb') # file to send
session.storbinary('STOR '+'spo.zip', file)     # send the file
file.close()                                    # close file and FTP
session.quit()


