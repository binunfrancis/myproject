import MySQLdb
conn = MySQLdb.connect("127.0.0.1","root","root","mysql")
c = conn.cursor()
c.execute("SELECT * FROM user")
rows = c.fetchall()
for eachraw in rows:
    print(eachraw)