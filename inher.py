class employee:
	num_employee=0
	raise_amount=1.04
	def __init__(self, first, last, sal):
		self.first=first
		self.last=last
		self.sal=sal
		self.email=first + '.' + last + '@company.com'
		employee.num_employee+=1
	def fullname (self):
		self.sal=int(self.sal *vraise_amount)
class developer(employee):
	pass
emp_1=developer('aayushi', 'jan', 100)
print(emp_1.email)
