class -> templates/defination of an instance  do not take memory
object -> functionality,attribute(data) occupy memory 

hastattr(s1,name)
getattr(s1,name)
delattr(s1,name)

s1.__dict__
####### CLASS ATTRIBUTE AND OBJECT ATTRIBUTE #######3
CLASS ATTRIBUTE -> common for all objects 


class Student:
    passins_marks=80   =========> class attribute 


s1=Student()

s1.name=rohit =======> instance attribute


######  STATIC METHOD VS INSTANCE METHOD ######

Class method -> commomn for all object of that class 

Instance method -> use self to access 


class Student:
    passing_mark=80

    def student_details(self):
        self.name=rohit
        self.roll_no=9
        self.percent=80


    @staticmethod
    def welcome():
        print("welcome to learning ")
s1=Student()
s1.welcome()

## init method ##
when object is created init function is called. so here  write default attribute

class Student:
     def __init__(self):
         self.name="abc"
         self.rollno=12

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno


#### Inheritance ####

class Vehicle:
    def __init__(self,color,maxspeed):
        self.color=color
        self.maxspeed=maxspeed

class Car(Vehicle):
    def __init__(self,color,maxspeed,numgears,isconvertible):
        super().__init__(color,maxspeed)
        self.numgears=numgears
        self.isconvertible=isconvertible

    def printcar(self):
        print("color:",self.color)
        print("maxspeed",self.maxspeed)
        print("numgears",self.numgears)
        print("isconvertible",self.isconvertible)

c=Car("red",15,3,False)
c.printcar()


## Inheritance and private members ##

class Vehicle:

    def __init__(self,color,maxspeed):
        self.color=color
        self.__maxspeed=maxspeed

    def get_maxspeed(self):
        return self.__maxspeed

    def set_maxspeed(self,maxspeed):
        return self.__maxspeed==maxspeed

class Car(Vehicle):
    def __init__(self,color,maxspeed,numgears,isconvertible):
        super().__init__(color,maxspeed)
        self.numgears=numgears
        self.isconvertible=isconvertible

    def printcar(self):
        print("color is :",self.color)
        print("maxspeed is :"self.get_maxspeed())
        print("numgears :",self.numgears)
        print("isconvertible",self.isconvertible)

c=Car("red",15,5,True)
c.printcar()






