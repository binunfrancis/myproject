import os
import sys
import zipfile
import ftplib
import os.path

# Other required imports

def BackupDB():
    if os.path.exists('binu.txt'):
        os.remove('binu.txt')
    try:
        file = open("./binu.txt", "w")
        file.write("This is a sentence")
    except Exception:
        print("Writing Failed")
    else:
        print("Writing success")
        file.close()
    if os.path.exists('binu.txt'):
        print('File Ready For Zip')
    else:
        print ("File Not Ready For Zip")
    d=os.path.join(os.getcwd(),"binu" + "." + "txt")

    return (d)
    # Backup procedure
    # Use error handling mechanism using Try...Except block
    # Check the file already exists.  If exists, delete the file
    # Create new backup file
    # Validate the process
    # return FullPath_of_Backup_File (Eg: c:\Users\user1\Documents\DBBackup.SQL)
    #pass

def ZipFile(SourceFile):
    if os.path.exists('binu.zip'):
        os.remove('binu.zip')

    try:
        jungle_zip = zipfile.ZipFile('./binu.zip', 'w')
        jungle_zip.write(SourceFile, compress_type=zipfile.ZIP_DEFLATED)
    except IOError:
        print("not zipped")
    else:
        print("File zipped successfully")
        jungle_zip.close()
    if os.path.exists('binu.zip'):
        print ('File Ready For Upload')
    else:
        print ('File Not Ready For Upload')


    f=os.path.join(os.getcwd(),"binu" + "." + "zip")


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