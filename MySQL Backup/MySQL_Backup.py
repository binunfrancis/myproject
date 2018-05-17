import os
import zipfile
import ftplib
import os.path
from datetime import date
from datetime import time
from datetime import datetime
import time

DATESTRING = datetime.strftime(datetime.now(), '%d%m%Y'+ time.strftime("%H%M%S"))
HOSTNAME = input("Host Address : ")
DATABASE = input("Database Name : ")
USERNAME = input("Database UserName : ")
PASSWORD = input("Database Password : ")
LOCATION = input("Location To Save (Eg:C:\\Users\\webserver\\Downloads) : ")
FTP_HOSTNAME = input("Please Enter The FTP HostName : ")
FTP_USERNAME = input("Please Enter The FTP UserName : ")
FTP_PASSWORD = input("Please Enter The FTP Password : ")


def BackupDB():
    os.system("mysqldump -u %s  -p%s -h %s  %s >%s\\%s.sql" % (USERNAME, PASSWORD, HOSTNAME, DATABASE, LOCATION, DATESTRING))
    print("Database Backup Completed successfully Your backup located at %s\%s.sql" % (LOCATION, DATESTRING))
    FILE_PATH = "%s\%s.sql" %(LOCATION,DATESTRING)
    return FILE_PATH


def ZipFile(FILE_PATH):
    ZIP_Path = "%s\%s.zip" %(LOCATION,DATESTRING)
    jungle_zip = zipfile.ZipFile(ZIP_Path, 'w')
    jungle_zip.write(FILE_PATH, compress_type=zipfile.ZIP_DEFLATED)
    print("File zipped successfully")
    jungle_zip.close()
    return ZIP_Path

def Upload(ZIP_Path):
    session = ftplib.FTP(FTP_HOSTNAME, FTP_USERNAME, FTP_PASSWORD)
    file = open(ZIP_Path, 'rb')
    session.storbinary('STOR ' + DATESTRING+".zip", file)
    filename = DATESTRING+".zip"
    if filename in session.nlst():
        file.close()
        session.quit()
        return (True)
    else:
        return (False)



BACKUP_FILE=BackupDB()
ZIP_FILE=ZipFile(BACKUP_FILE)
UPLOAD_STATUS=Upload(ZIP_FILE)

if UPLOAD_STATUS==True:
    print ('File Uploaded Successfully')
else:
    print ('Upload failed')