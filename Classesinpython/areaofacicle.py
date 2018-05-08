class Circle:
  radius = 0
  def __init__(self,radius):
    self .radius = radius
    
  def area(self):
    return 3.14 * float(self.radius * self.radius)
      
  def perimeter(self):
    return 3.14 * float(2 * self.radius)
      
radius= int(input("what is the radius"))
circle= Circle(radius)
print("Area of the Circle is",circle.area())
print("Perimeter of the Circle is",circle.perimeter())