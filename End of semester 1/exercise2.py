class Person:
  name= "john doe"
  
  def __init__(self,name):
    self.name = name
    
  def get_name(self):
    return(self.name)
    
  def printName(self):
    return " Name of the person: {}".format(self.name)
    
Fatma = Person("feliciah")
print(Fatma.printName())
