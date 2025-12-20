class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        
    def __str__(self):
        return f"Employee Name: {self.first.capitalize()} {self.last.capitalize()}"
        
        
    @property
    def email(self):
        return f"{self.first.lower()}.{self.last.lower()}@company.com"
        
    @property
    def fullname(self):
        return f"{self.first.capitalize()} {self.last.capitalize()}"
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(" ")
        self.first = first
        self.last = last
        
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None
        
        
employee = Employee("john","smith")
employee.first = 'steven'
employee.fullname = 'Shane Watson'
print(employee.fullname)
print(employee.email)
print(employee)