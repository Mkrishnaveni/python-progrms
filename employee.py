#!/usr/bin/python
class Employee:
	'Common base class for all empployees'
	empCount = 0
	def __init__(self, name ,salary, age):
		self.name = name
		self.salary = salary
		self.age = age
		Employee.empCount += 1
	def displayCount(self):
		print "Total Employee %d" % Emplyee.empCount
	def displayEmployee(self):
		print "Name : ", self.name, ", Salary: ", self.salary , "age : ", self.age
"this would create first object of employee class"
emp1 = Employee("zara", 2000, 23)
"this would create second object of employee class"
emp2 = Employee("mani", 500, 34)
emp1.displayEmployee()
emp2.displayEmployee()
print "total Employee %d" % Employee.empCount
