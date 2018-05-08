def welcome_student(name):
  welcome_str = "Hi {} welcome to akirachix"
  return welcome_str.format(name)


def welcome_all(*args):
  for student in args:
    print(welcome_student(student))

welcome_all("julia","felicia","assue","taspin","juddie","evelyn","jane","mauren","leah")