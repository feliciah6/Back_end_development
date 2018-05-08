class Student:
  
  def __init__(self, names, email):
    self.names = names
    self.email = email
    self.validateEmail()
    self.validateName()
    
    def validateEmail(self):
      # search if the string has an @sign
      
      pass
    def validateName(self):
      if type(self,names)is not str:
        raise valueError("{} is not a valid name".format(self.name))