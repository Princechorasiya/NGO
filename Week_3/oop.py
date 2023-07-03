# pytohn is oop based
# list tuple dictionary set are objects fo their particular clasess


# classes and objects are two main asxpets of oop

# user defined bueprits that helps us create an object

# object are instances of particular class copies of class with values

# class car and its objects may be hynundai ford or any other carv


# creating an object is called instantiation  object shares all the attributes,methods  of the class


# class has
# state attributes
# identity  every and every object must be unique in its own
# behaviour  shows the methods of teh class


# AFTER CREATING CLASS we create instances of the class called objects

# object_name = class_name(arguments/parameter)


import functools
from dataclasses import dataclass
from time import time, sleep
from math import pi
from abc import ABC, abstractmethod, abstractproperty


class Prince:
    a = 10
    b = 23
    c = 50


obj1 = Prince()
print(obj1.a)

# functions inside objects are called classes


class Prince_1:
    def __init__(self, name):
        self.name = name

    def new(self):
        print(self.name)


obj2 = Prince_1("prince")
obj2.new()

# __init__ method is similar to constructor in c++/java
# statement during creation of the object
# first argument must be  self

# we can modify the values declared in class

# deleting object properties with del
del obj1.a

del obj1

# the name of the object by which it is bound is deleted but the value remains inthe memeory which gets deleted later by garbage collector
# for deleting complete class

# oop object oriented programming.
# C++ java
# an oop should support
# 1) encapsulation ability to abstract real world
# objects (attributes and behaviours(methods) and hide unnecessary info.)
# 2)Inheritance ability to create sub-classes.

# 3)Polymoerphism - Ability of an object to adapt the code to the type of data it is processing.
# java 1990 sunmicro system
# programming paradigm defines the methodolgy of desigining and implementing the code.
# Procedural programming
# linear top-sown approach  c uses procedural programming language.
# Better for small programs efficent written for specific purpose
# small changes require very high changes in the code

# object based programming some features of oop but not all. no inheritence and polymorphism
# javascript,Visual basic

# oop based on objects
# data known as atributes
# code(functions) in form of methods.
# Class represents real-world things and we create objects based on these classes.
# class is a blueprint or design which stores
# data - atrributes and
# code which gives data - methods
# object is a specimen of a class instance specififc object created from a particular class
# creating an object is called is called instantiation


class Car():
    def __init__(self, name, color):
        """Initializing name,color, and model atributes"""
        self.name = name
        self.color = color

    def get_speed(self):
        """Seting the speed of the car"""
        print("Top speed of"+self.name+"is 150 km/hr")


honda_city = Car("Honda City", "Red")
honda_city.get_speed()

# class is combination of the members and member function

# encapsulation idea of bundling data and method that work on the data
# within inre unit restricting access to some objects  components (variables and methods)
# Class is an example of encapsulation
# enscapsulation = Abstraction +Information Handling
# Abstraction identify all essentials while omit those unimportant things.
# infroamaion hiding hiding all unnecessary inforamtion

# members into private,protected and public
# only public members are visible while others remain hidden
# abstraction hides data.

# class has 4 key members
# 1) constructors __init__(self)  invoked automatically when a new object of class is instantiated.
# 2) class variables or class attributes  information shared by all objects of the class.
# 3)instance variable attribute created per object.
# 4) methods functions can acess any of these variables.
# pass statement is used syntactically when needed but no action needs to be performed


class Student:
    pass


stud_2 = Student()
stud_1 = Student()
stud_1.name = input("s1 name:")
stud_2.name = input("s2 name:")
print(stud_1.name)
print(stud_2.name)


class Class_Name:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def method(self, arg1, arg2):
        pass

    def method1(self, arg1, arg2):
        pass

# Self variables inside the __init__ part associates with self.
# Using self argument we can access the attributes and the methods of the class.
# self refers to the current instance of the class.
# even when creating a method in class we use self as the first number.
# self is not a key word


class Car:
    def setDetails(self, model, regno):
        self.model = model
        self.regno = regno

    def getModel(self):
        return self.model

    def getRegno(self):
        return self.regno


Hyundai = Car()
model = "123"
regno = "234"
Hyundai.setDetails(model, regno)
print(Hyundai.getModel())

# Constructors
# specific method for Initializing variables in class or to setup tasks that needs to be doen when an instance of a class is created.
# defining constructors( __init__(self))  when we create a class without a constructor python creates a __init__(self) that doesn't do anything  instantiates the object.
# construcotrs can be overloaded based on the number of arguments.Always write self as the first argument.

# methods
# function doesnt need to be a part of the class while method has to be a part of the class.
# <bound·method·Student.getname·of·< __main__.Student·object·at·0x7f74b77370b8>>
# you are actually not execting your function add () after the function.

# Overloading is the abiltity of a function to behave in a different way based
# that are passed to the function

# Method overloading means the abillity to have multiple methods with same naem which vary in their parameters
# Python doesn't allow overloading concept of polymorpehsim.

# In python we specify the total number of parameters and depending on teh method we call it with zero,one or more arguments.
# Body of the  method contains the logic on case any parameter is missing


class Gretting:
    def sayhello(self, name=None, wish=None):
        if name is not None and wish is not None:
            print("Hello"+name + wish)
        elif name is not None and wish is None:
            print("Hello"+name)
        else:
            print("Hello")


greet = Gretting()
greet.sayhello()
greet.sayhello("Ram")
greet.sayhello("Ram", "Good Morning")


# abstraction is used to hide the internal functionalities classes formo the users


# it reduces complexitity of the code

# makes powerful run easily


# users are familiar with class usage but not with how it solves the problems


# we cannot create abstract classes directly in python


# Abstract methods force the child classes to give the implementation of these methods in them


# from Shape import Shape


# syntax


# abstract classes used to create classes but the method doesnt contain implementaion
# classes from which objects cannnot be created


# by using abstract classes we make sure that subclasses use the same structure and same method names for the task


class DemoAbstract(ABC):

    @abstractmethod
    def abstract_method_name(self):
        pass


class Shape(ABC):

    def __init__(self, shape_name):

        self.shape_name = shape_name

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):

    def __init__(self):

        super().__init__("circle")

    @property
    def name(self):
        return self.shape_name

    def draw(self):

        print("drawing a circle")


circle = Circle()
print("The shape name is:{}".format(circle.name))

# abstract property

# @abstractproperty
# we cannot intanitate objects from abstract class gives error


# we can pass a abasic implementaion in abstract method and deliver its work as required  Concrete class

# concrete class a class that has defination for all its methods and no abstract methods
# concrete class can use  super() to class base abstract methods


class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name

    @abstractmethod
    def draw(self):
        print("Preparing the Canvas")


class Circle(Shape):
    def __init__(self):
        super().__init__("circle")

    def draw(self):
        super().draw()
        print("Drawing a Circle")


# we can also have concrete method along with abstract classes

class Animal(ABC):

    # concrete method
    def sleep(self):
        print("I am going to sleep in a while")

    @abstractmethod
    def sound(self):
        print("This function is for defining the sound by any animal")
    pass


class Snake(Animal):
    def sound(self):
        print("I can hiss")


class Dog(Animal):
    def sound(self):
        print("I can bark")


class Lion(Animal):
    def sound(self):
        print("I can roar")


class Cat(Animal):
    def sound(self):
        print("I can meow")


# encapsulation bundling similar data and functions in single class .
# also helps in data hiding
# ensures that objects are self sufficent functioning pieces and can work indpendently

# user want the final product not the extra data about how its made

# encapsulation facilitates abstraction

# wrap up both data and methods into one single unit
# the way data and methods are organized doesn't matter to the user


# class  >>>>>method and variable in a capsule

# well defined and readable code
# prevents Accidental modification or deletion
# encapsulation provises security done through access modifiers


# Access modifiers         own class                 derived class            object
# public members              yes                         yes                     yes

# private members                yes                         no                      no

# protected members               yes                         yes                    no

# public members nothing to be done
# all thing declared are public if nothing is done


# using private members
# start with __ before the var name to make it private

class Rectangle:
    __length = 0  # private variable
    __breadth = 0  # private variable

    def __init__(self):
        # constructor
        self.__length = 5
        self.__breadth = 3
        # printing values of the private variable within the class
        print(self.__length)
        print(self.__breadth)

# we cannot access this outside the class Attribute error

# protected members

# we use _ to for protecting var
# only class and derived class can acess it


class details:
    _name = "Jason"
    _age = 35
    _job = "Developer"


class pro_mod(details):
    def __init__(self):
        print(self._name)
        print(self._age)


# data hiding

# over the years oop has evolved to overcome the limitations of the proceddral
# programming Data is given high priority in oop. Data is hidden to avoid irrelavant usage of the function to avoid accidental usage.
# Data Abstraction refers to the act of representing esssential features without including details and explainations
# data enscapsulation is the way of generating both data and functions that operate on the data under a single unit.
# data is not accessible to the outside world directly it can be only accessed through the member function. the insulation of data from the direct acess by the program is called data hiding


# Abstraction and Encapsulation are complementary
# concepts, where abstraction focuses upon the observable behaviour of an object and encapsulation focuses upon the implementation that gives rise to this behaviour.

# private variables:
# starts with __ eg __engineno, __modelname


class Prince:
    def __init__(self, name):
        self.name = name

    def __name(self):
        print(self.name)


prince = Prince("prince")

prince.name
# here name is visible as it is not followed by__


class Prince:
    def __init__(self, name):
        self.__name = name

    def __name(self):
        print(self.name)


prince = Prince("prince")

# prince.
# here name is not visible as it hidden using the __
# if we try to print hidden variable or use hidden methods we get attribute errors


class Prince1:
    def __init__(self, name):
        self.__name = name

    def name1(self):
        print(self.__name)


prince = Prince1("prince")
prince.name1()
# print(prince.name) #gives attribute error
# public variable can be accesed anywhere
# private variable and methods can not be used bu the derived class


class Prince:
    def __init__(self, name):
        self.__name = name

    def name1(self):
        print(self.__name)


class King(Prince):
    def __init__(self, __name):
        super().__init__(__name)

    def hello(self):
        print(self.__name)


# inheritence
# allows us to access data of previous classses without creating them from scratch

# classes dont occupy any computational storage but objects created from it do

# inheritence
# modularity The act of dividing a program into individual components
# is called modularity.
# it reduces its complexity to some degree.
# It creates a number of well defined,documented boundaries within the program.
# modularity in c++ or java is implemented by writing the code seperately in fiels called classes and organinzing them into
# different namespaces or packages.


# Inheritance is the process by which an object of one class aquires the properties of another class.

# polymorpehsim can be defined as the ability of a single entity to behave differently depending on the context.
# may exhibit different forms in different behaviours.

# inheritence is implemented by creating a derived class that have the features of the base class in addition to having features of its own.

# in real time it is more like a parent child relationship.
# car  base class
# Honda Accord is derived class

# base class is just like regular class.
# A derived class is created by passing the baseclass name as parameter to teh derived class.

# basee class can be inside a  same module or different module.

class derivedClassName(BaseClassName):
    statement1
    statement2
    statementn


class derivedClassName(unit1.BaseCLassName):
    statement_1
    statement_2


class Car:
    def setenginemodel(self, engine):
        self.engine = engine

    def getenginemodel(self):
        print(self.engine)


class Honda(Car):
    def setcarmodel(self, model):
        self.model = model

    def getcarmodel(self):
        print(self.model)


mycar = Honda()
mycar.setcarmodel("Ek-1")
mycar.setenginemodel("V6")
print("cardetails")
mycar.getenginemodel()
mycar.getcarmodel()

# python supports mutliple inhertience a derived class can have features of multiple classes


# Floats are an approximation to the number they represent
x = 0.23  # float
# python saves this as 0.2300000000000000000000123 kind of like this

# print(0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23 +
#   0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23 == 6.9)
# 0.23 add 30 times we get 6.90000000000000006 or someting
# the answer should have been true but gives false
# Why does this happen

# 2.3 *2.3 = 5.29 precision 2.3 has one decimal point precision =1 (max decimal point)
# if two number have one decimal precision the output also has 1 decimal point this is what happens in computers
# 2.3000000000000000000000123 *2.30000000000000000000000000123 the end number is very small python ignores It
# but while adding 0.23 30 times the ending numbers are not neglible
# but 0.23 *30 gives 6.9 exactly not 6.9000000000000000000006;
# puthon has some intelligence optimization addition ocuurs step by step 0.46000000000000000000000246 + 0.230000000000000000000000000123 new numbers are added each time no optimization as python thinks new numbers are added
# while mutlplicaton is repeated multiplication of the same number optimization is here as python ignores the decimal parts
# class Honda(Car,Type):

# Python is also multiple level inheritence grandfather father child
# base class then derived class that is again the input for ther derived class 2.
# search for method starts the derived class and go upto the base class if the result is not found.

# Be careful while using __init method in these section

# class Vehicle:
#     def __init__(self, name):
#         self.name = name


# class Car(Vehicle):
#     def __init__(self, price):
#         self.price = price


# c1 = Car()

class Vehicle:
    def __init__(self, name, model, regno):
        self.model = model
        self.name = name
        self.regno = regno


class Car(Vehicle):
    def __init__(self, name, model, regno, price):
        super().__init__(name, model, regno)
        self.price = price


class Boat(Vehicle):
    pass


car = Car("p", "q", "r", "5")
print(car.model)
print(car.name)
print(car.price)

boat = Boat("a", "b", "c")
print(boat.name)


class Hover(Car, Boat):
    pass


h1 = Hover("a", "b", "c", "d")
print(h1.name)
# fixing those errors in the code for multiple level inhertience

# Overriding the ability to change the iplementaton of a method provided by
# one of its ancestors(parent/base class)
# conditons for method overriding;
# the concept of inheritence should be preexisting
# redefined method should have same signature as the base class


class Shape:
    def noofsides(self, sides):
        self.sides = sides


class Square(Shape):
    def noofsides(self, sides):
        self.sides = sides
        self.name = "square"


# simple inheritence
#  single derived from single base

# multiple inhetience
# single child from multiple classes inherits from all parents
# if two parents have same methods the class which comes first is given priority

# to find the order of classes visited we  use
# print(child.__mro__)  itself then parents then objects


# multilevel inheritence
# grandparent parent child and its great grand parents as well


# hierachical inheritence 'multiple classes from a single parent '


# hybrid  multiple inheritence with multilevel and hierachical

# methods

# super()   references the parent/base class from ehich the child class is derived

class Parent:
    attr2 = 45

    def __init__(self):
        self.attr1 = 50

    def say_hello(self):
        print("Hello")


class Child(Parent):
    def __init__(self):
        # Parent.__init__(self)  only the variable inside the __init__ of parent needs this
        super().__init__()   # doesnt include the self
        self.attr = 34

    # Method overriding

    def say_hello(self):
        # super().say_hello()  # referencing the parent
        print("Helllo child")
        # super(Child, self).say_hello()      #second way to call the parent class


test1 = Child()
print(test1.attr1)
print(test1.attr2)
test1.say_hello()

print(issubclass(Child, Parent))
print(issubclass(Parent, Child))


# advantages modular codebase
# code reusability
# less development and maintenance

# disadvatages
# decreases the execution classes
# Tightly coupled classes


#  in english we use  a single word for many different uses deppending on the situation

# literal meaning of polymorphesim having different forms
# function having the same name but being used in different  ways and different scenarios

# ability of one function to display multiple functionalities all together .

# operator overloading using operator beyond its pre defined purpose


# +  add for num while concatenate for string example of polymorphism

# class polymorphesim


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Im a cat .myname is %s.I am %d old." % (self.name, self.age))

    def make_sound(self):
        print("Meow")


class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Im a cow.myname is %s.I am %d old." % (self.name, self.age))

    def make_sound(self):
        print("Moo")


cat1 = Cat("Kitty", 2.5)
cow1 = Cow("Fluffy", 4)

for animal in (cat1, cow1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# polymorphism in python using inheritance
#  child class
# same method as p/arent and inhreit  all mehtod from parent
# now we may need to modify some property this is called method overloading


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am two dimenional shape"

    def __str__(self):
        return self.name


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


shape_circle = Circle(7)
print(shape_circle.name)
print(shape_circle.area)  # parent and child both have same method


# polymorphism with class method
# two different class with same method and different functionalities


#  polymorphesim wiith function and objects

class Beans():
    def type(self):
        print("Vegetable")

    def color(self):
        print("Green")


class Mango():
    def type(self):
        print("Fruit")

    def color(self):
        print("Yellow")


def func(obj):
    obj.type()
    obj.color()


# creating objects
obj_beans = Beans()
obj_mango = Mango()
func(obj_beans)
func(obj_mango)


# iterators in oop we can transverse and they will return their membeber value one by one

# two methods for iterator implementaion
# iter()     ans next()

mySecret = ["i", "love", "ns"]
myIter = iter(mySecret)  # /iter returns the iter object
print(myIter)

print(next(myIter))  # to transverse throught the iter

print(next(myIter))
print(next(myIter))
# if we use a var that is not iterable we get a type error

# making iterators

# dunder /magic methods __init__ and other mehods similar to it
# __iter__()  return iterator object customization can be done
#  and __next__()     return the next item in the sequence


class ModOFTwo:
    def __init__(self, max1=0):
        self.max = max1

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n % 2
            self.n += 1
            return result
        else:
            raise StopIteration


numbers = ModOFTwo(3)  # gives us mod of numbers from 0 to n
i = iter(numbers)


print(next(i))
print(next(i))
print(next(i))
print(next(i))
# one more print and we get error


# __init__ method we intiallized number til which we want ot iterate

# __iter__ has initial value
# __next__  we have the result we return and the next value it goeing to take


# iteraotr  object which has __iter__() an __next__()

# vs
# iterable  anything which we can loop over
# basic for loop
nums = [1, 2, 3, 4]
nums_iter_obj = iter(nums)
while True:
    try:
        print(next(nums_iter_obj))
    except StopIteration:
        break


# infinite iteraotr

class InfiniteIterator:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        result = self.n * 2
        self.n += 1
        return result


multipleOfTwo = InfiniteIterator()
i = iter(multipleOfTwo)
print("Multiples of two are:")
print(next(i))
print(next(i))

print(next(i))
print(next(i))
print(next(i))
# we have no max value so we can iterate infinitely


# decorator is a function that takes another function as an argument and extend  it
#


#  Takeaway:


# A Decorator is a function that takes another function and


# extends the behavior of the latter function without


#  explicitly modifying it.


# function is first class objects.


# has rights as any other var in the language


# we can assign the function to variable pass it to a function and return it from a function


# passing t another as argument


def do_twice(func):
    func()
    func()


def say_hello():

    print("Hello!")


do_twice(say_hello)


# Higher-order function is a function


#  that takes a function as an argument or


#  returns a function.
#

# inner function function inside a function or nested functions


# order in which we define inner function doesn't matter


# The inner functions are locally scoped to the parent. They are not available outside of the parent function.


def decorator(func):

    # for making us print the doc string of the function we are going to decorate
    # and as well

    @functools.wraps(func)
    def wrapper():

        print("This is printed before the function is called")
        func()

        print("This is printed after the function is called")

    return wrapper


def say_hello():

    print("Hello! The function is executing")


say_hello = decorator(say_hello)


say_hello()

# decorator another functiona as input and decoratoes it


# A decorator function modifies a function by wrapping it in a wrapper function


# say_hello ordinary function executed after first step
# to write decorator


# syntatic sugar easier way to write something

# import functools


@decorator
def say_hello1():
    """This function says hello when called"""

    print("Hello! The function is executing")


say_hello1()


print(say_hello1.__name__)


help(say_hello1)


# we can easily decorate a function using the @decorator syntax


# reusing python decorators


# decorator that does work tiwice


def do_twice(func):

    @functools.wraps(func)
    # def wrapper():    #
    #     func()
    #     func()
    # this gives error when we use function with parameter
    # if we single parameter in wrapper we can use the decorator for functions with single parameter
    def wrapper(*args, **kwargs):

        func(*args, **kwargs)

        # func(*args, **kwargs)

        # returning value from decorated functions

        return func(*args, **kwargs)

        # we called the func three times here  fix it by making it two and we return a value from it

    return wrapper


@do_twice
def sayHello(name):

    print(f"Hello!,{name}")

    return name


sayHello("kitty")


name = "prince"


print(sayHello(name))


# decorators with arguments

# we can pass argumetns to decorators itself

#  define the decorator inside another function that accepts argumetns


def repeat(n):

    def decorator_repeat(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            for i in range(n):

                value = func(*args, **kwargs)

            return value
        return wrapper

    return decorator_repeat


@repeat(3)
def sayHello12(name):

    print(name)


sayHello12("liza")


# chaining decorator


def split_string(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs).split()
    return wrapper


def to_upper(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs).upper()
    return wrapper


@split_string
@to_upper
def prince(name):

    return f"Hello, {name}, bye"


print(prince("ns"))


# fancy decorators
# decorators with classes
# decorating a method of a class
# decorating a complete class

# decorating class methods


# @classmethod   create methods bound to the functions not ot thw object of the class


# @staticmethod       cannot modify object state or class state as they dont have

# access to ls or self they are just part of namespace


# @property

# create getters and setters for class attributes


class Browser:

    __NO_OF_WINDOWS = 0  # private member

    def __init__(self, page):

        self.page = page

        self.is_incognito = False

        Browser.__NO_OF_WINDOWS += 1

    @property
    def page(self):  # getter

        return self._page

    @page.setter
    def page(self, new_page):

        if type(new_page) is not str:

            raise TypeError("Pages must be strings")

        self._page = new_page

    @classmethod
    def with_incognito(cls, new_page):

        instance = cls(new_page)

        instance.is_incognito = True
        return instance


# fancy decorators
# decorators with classes
# decorating a method of a class
# decorating a complete class

# decorating class methods


# @classmethod   create methods bound to the functions not ot thw object of the class


# @staticmethod       cannot modify object state or class state as they dont have

# access to ls or self they are just part of namespace


# @property

# create getters and setters for class attributes


class Browser:

    __NO_OF_WINDOWS = 0  # private member

    def __init__(self, page):

        self.page = page

        self.is_incognito = False

        Browser.__NO_OF_WINDOWS += 1

    @property
    def page(self):  # getter

        return self._page

    @page.setter
    def page(self, new_page):

        if type(new_page) is not str:

            raise TypeError("Pages must be strings")

        self._page = new_page

    @classmethod
    def with_incognito(cls, new_page):

        instance = cls(new_page)

        instance.is_incognito = True
        return instance

    @staticmethod
    def get_browser_info():

        return {

            "name": "Google Chrome",

            "version": "96.0.4664.110",

            "OS": "windows"

        }


# class browser

# getter and setter with @property


# with_incognito  factory method which act to create incognito


# staticmethod to check information sasme for all windows users


# decorating a complete class

# same as func but decorator will receive class as argument not a function

# from dataclasses import dataclass
# has dataclass decorator

@dataclass
class User:

    username: str

    password: str

    active: bool


sheldon = User("Sheldon", "make_password", True)

# a data class is a class mainly containing data it has bsic functionalities
# already implemented
# username :str  suggests the dat Type of the username as str and makes suto completion easier


# Classes as decorators

# the __init__ needs to take a function as arguments
# class needs t implement __call__ method

# we use function.update_wrapper instead of @function.wraps

class CounterCall:
    def __init__(self, func):
        functools.update_wrapper(self, func)   # no @before it gic=ves error
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CounterCall
def say_hello12():
    print("Hello")


for i in range(5):
    say_hello12()


# real rorld usage of decorators
# real world use is measure the execution time of function


def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, "took", time()-t)
    return wrapper


@measure
def slppy_function():
    list = [1, 2, 3, 4, 45, 6]
    for i in list:
        print(i)
    print("Hello worls")
    sleep(10)
    print(3+5668596798579635986734958673984576389457983578693475869358386578693573586097683447208 -
          267384576398576039857360985673875877-68567876828462)


slppy_function()


@measure
def sleepy_function(sleep_time):
    sleep(sleep_time)


sleepy_function(0.3)
sleepy_function(0.5)

# other use of decorators

# authoriazton in frameworks like flask and dajngo
# logging and debugging

# validating json
# caching return values of function

# time to measure time and sleep to freeze execution of the function for a given time
