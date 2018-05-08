class Triangle:
  base = 0
  height =0 
  hypotenuse = 0
  
  # def (self, base, height, hypotenuse):
  #   self.base = base
  #   self.height = height
  #   self.hypotenuse = hypotenuse
    
  def area(self):
    return 0.5 * self.base * self.height
    
  def perimeter(self):
    return(self.base + self.height + self.hypotenuse)
    
    
small = Triangle(4,8,4)
large = Triangle(5000,70000,6000)
print("base and height of smaller {} and {}". format(small.base,small.height))
print("smaller area",small.area())
print("larger area",large.area())

print("base, height and hypotenuse of smaller {}, {} and {}".format(small.base,small.height,small.hypotenuse))
print("smaller perimeter",small.perimeter())
print("larger perimeter",large.perimeter())
