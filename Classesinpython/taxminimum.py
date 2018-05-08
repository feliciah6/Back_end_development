class Taxpayer:
  income = 0
  name = "jane doe"
  
  def __init__(self,name,income):
    self.income = income
    self.name = name
  
    self.validateIncome()
    self.validateName()
    self.validateMinimum()
    
    
  def validateIncome(self):
    if self.income.isnumeric()==False:
      raise ValueError("the income {} is not a numeric".format(self.income))
   
   
  def validateName(self):
    if self.name.isnumeric():
      raise ValueError("the name {} is not a string".format(self.name))
      
  def calculate_tax(self):
     return float(self.income) * 0.3
  
  
  def validateMinimum(self):
    if self.income < 100001:
      raise ValueError("below mimimum wage".format(self.minimum))
     
income = input("what is your income")
name = input("what is your name?")
employee = Taxpayer(name,income)
print(employee.calculate_tax())