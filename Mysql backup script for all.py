import os
import os.path
from datetime import datetime

datestring = datetime.strftime(datetime.now(), '%d%m%Y')
hostname =input("Host Address")
database =input("Database name")
username =input("database username")
password =input("Database password")
location=input("location to save (Eg:C:\\Users\\webserver\\Downloads)")


os.system("mysqldump -u %s  -p%s -h %s  %s >%s\\%s.sql" %(username,password,hostname,database,location,datestring))
print("Database Backup Completed successfully Your backup located at %s\%s.sql"%(location,datestring))
