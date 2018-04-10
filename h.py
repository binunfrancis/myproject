import os
import sys
import os
import zipfile
import ftplib
import os.path

# Other required imports

def BackupDB():
    if os.path.exists('spo.sql'):
        os.remove('spo.sql')
    os.system("mysqldump -u root -proot -h localhost test>./spo.sql")
    if os.path.exists('spo.sql'):
        print ('Backup Completed')
    else:
        print ('Backup Failed')
    d = os.getcwd()+'\spo.sql'

    return (d)
    # Backup procedure
    # Use error handling mechanism using Try...Except block
    # Check the file already exists.  If exists, delete the file
    # Create new backup file
    # Validate the process
    # return FullPath_of_Backup_File (Eg: c:\Users\user1\Documents\DBBackup.SQL)
    #pass

def ZipFile(SourceFile):

    jungle_zip = zipfile.ZipFile('./spo.zip','w')

    jungle_zip.write(SourceFile, compress_type=zipfile.ZIP_DEFLATED)
    jungle_zip.close()
    f=os.getcwd()+'\spo.zip'

    return (f)
    # Zip Procudure
    # Check the zip file is already exists in the path, if exists, remove it
    # Check the SourceFile exists, if exists, do the zip process
    # Return Full_Path_of_ZipFile
    #pass

def Upload(SourceFile):


    import ftplib
    session = ftplib.FTP('192.168.1.142', 'test', '123456')
    file = open(SourceFile, 'rb')
    session.storbinary('STOR ' + 'Ftp.zip', file)
    filename='Ftp.zip'
    if filename in session.nlst():

        file.close()
        session.quit()
        return (True)
    else:
        return (False)




    # FTP Upload procedure
    # Check the zip file exists
    # if exists, upload to ftp
    # Check ftp folder for duplicate
    # return True/False status based on Success or failure
   # pass

# Main script
BACKUP_FILE=BackupDB()
ZIP_FILE=ZipFile(BACKUP_FILE)
UPLOAD_STATUS=Upload(ZIP_FILE)

if UPLOAD_STATUS==True:
    print ('Upload completed')
else:
    print ('Upload failed')