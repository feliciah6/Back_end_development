class Student:
  name = "john doe"
  
  def __init__(self,name):
    self.name =name
    
  def get_name(self):
    return self.name

      
  def welcome(self):
    return"welcome {} to Akirachix".format(self.name)
    
Fatma = Student("Fatma moha")
judith = Student("judith mueni")
print(Fatma.welcome())
print(judith.welcome())