def welcome_student(name):
  welcome_str = "Hi {} welcome to akirachix"
  return welcome_str.format(name)
  
name = input("enter student name:")
print(welcome_student(name))
print(welcome_student("julia"))
print(welcome_student("maureen"))
print(welcome_student("felicia"))