#!/usr/bin/python
import MtSQLdb
# open dtatbase connection
db = MYSQLdb.connect("localhost","testuser","test123","TESTDB")
cursor =db.cursor()
cursor.execute("SEELCT VERSION()")
data =cursor.fetchone()
print "Database version : %s " % data
db.close()#!/usr/bin/python
print "Set-Cookie:UserID = XYZ;\r\n"
print "Set-Cookie:Password = XYZ123;\r\n"
print "Set-Cookie:Expires =Tuesday, 31-Dec-2007 23:12:40 GMT";\r\n"
print "Set-Cookie:Domain = www.zippyops.com;\r\n"
print "Set-Cookie:Path = /per1;\n"
print "Content-type:text/html\r\n\r\n"
