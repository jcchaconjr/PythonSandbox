class Person:
  def __init__(this, fname, lname):
    this.firstname = fname
    this.lastname = lname

  def printname(this):
    print(this.firstname, this.lastname)

class Student(Person):
  def __init__(this, fname, lname, year):
    super().__init__(fname, lname)
    this.graduationyear = year

  def welcome(this):
    print("Welcome", this.firstname, this.lastname, "to the class of", this.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printname()
x.welcome()

