class Student:
  name = "john doe"
  weekday= True
  
  def __init__(self,name,weekday):
    self.name =name
    self.weekday =weekday
    
  def morning(self):
    if self.weekday:
      return "wakes up"
    else:
      return"sleeps"

    
Fatma = Student("Fatma moha",True)
judith = Student("judith mueni",weekday=False)
print("Fatma:",Fatma.morning())
