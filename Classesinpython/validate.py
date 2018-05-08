class Rectangle:
  length = 0 
  width = 0 
  def __init__(self, length, width):
    self.length = length
    self.width = width
    self.validateLength()
    self.validateWidth()
    
  def areaa(self):
    return self.length * self.width
    
  def perimeter(self):
    return 2*(self.length + self.width)
    
    
  
  def validateLength(self):
    if self.length.isnumeric() ==False:
      raise valueError("the length {} is not a numeric".format(self.length))
       
      
  def validateWidth(self):
    if self.width.isnumeric() ==False:
      raise valueError("the width {} is not a numeric".format(self.width))
      
length =input("what is the length")
width =input("what is the width")
invalid = Rectangle("fixe",5)
print(invalid.area())
      
      
    