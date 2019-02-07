#!/usr/bin/python
from xml.dom import minidom
doc = minidom.parse("callforprogrm.xml")

name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

staffs = doc.getElementsByTagName("callforprogrm.xml")
for staff in staffs:
	sid = satff.getAttribute("id")
	nickname = staff.getElementsByTagName("nickname")[0]
	salary = staff.getElementsByTagName("salary")[0]
	print("id:%s, nickname:%s, salary:%s" %
		(sid, nickname.firstChild.data, salary.firstChild.data))
