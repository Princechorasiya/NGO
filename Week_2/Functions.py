# a block of code needed to be executed multiple times leads to long codes.
# a subprogram which specifies one or more actions for the larger program is called functions.

# defining a function

# file in another package


from functools import reduce
import cmath
from readline import set_completer


def function_name(parameters):  # parameters are not necessary
    """docstrings if we want"""  # to print docstrings function.__doc__ attribute is used dont wite the brackets while writing the function
    statement(
        d)  # one or multiple statement can be in a program return statement is optional

# code in the fucntion is runned when it is called.


"""Return statement in a function :
The return statement is used to quit a function it is executing and to pass the control back to the statement from where it was called. The syntax of the return statement is as below.

return [expression_list / value]"""


a = 3
b = 5


def add():
    c = a+b
    f = a-b
    return (c)
    # return(f)
#double return doesnt work if you want to get more than two values use


a = 3
b = 5


def add():
    c = a+b
    f = a-b
    d = [c, f]
    return d


print(add()[0])  # gives c


# python doesnt uses pass by reference or pass by reference but pass by object reference
# # variable consists of object  if value passed is mutable it will change else not
# memory address remain same during the execution
# id(var) gives the memory location
# # mutable list set
# # or immutable   string tuple


# Arguments are specified after the function name, inside the parentheses.


def my_function(fname):  # fname is parameter
    print(fname + " Refsnes")


# if we use parameter while defining function we have to give
my_function("prince")
# parameter  value=argument  while calling the function

"""From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called."""


def my_function(fname, lname):  # two parameters
    print(fname + " " + lname)


my_function("a", "b")

# my_function("email") # gives error we need two arguments but we gave only one argument


# when no of arguments to be entered is unknown
def my_function(*kids):  # *argument     stored in tuple
    print("The youngest child is " + kids[0])
    # arguments passed this are packed into tuple we can convert it in to list and change the arguments


my_function("Emil", "Tobias", "Linus")

# key=value format


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Email", child2="Tobias", child3="Linus")


# If the number of keyword arguments is unknown, add a double ** before the parameter name:
# if we want the arguments to be only keyword arguments then we define the function with * as the first parameter.

def my_function(**kid):  # stores data in dictionary form.
    # we can access them in the function and modify them too
    print("His last name is " + kid["lname"])


# unpacking opertor * also packing ooperator as well
values = (1, 2, 3, 4, 5)


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print(total)
    return total
# add_numbers(values) # this gives error because we pass tuple and *args stores data in tuple no += on tuples


# values iterates over values passing each number of tuple value
add_numbers(*values)

details = ('1', 'Aryaman', 'Computer Science')


def func(roll_no, name, branch):
    print(
        f'Roll number {roll_no} is {name} from {branch} branch of Engineering.')


func(*details)
# but the size of tuple mustbe equal to required parameters

# one function can call other function if needed
my_function(fname="Tobias", lname="Refsnes")

lambda used
# filter(f,list)  to filter out required
# map(function,list)  to apply required operation on list
# reduce comes from functools  to reduce a list into single value
numbers = [1, 2, 3, 4, 5, 6]
sum = reduce((lambda x, y: x+y), numbers)
print(sum)


# default parameter value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()

# required parameter argumentsw without default value


# * is to iterate over a iterable
carCompany = ['Audi', 'BMW', 'Lamborghini']
print(*carCompany)
techStackOne = {"React": "Facebook",
                "Angular": "Google", "dotNET": "Microsoft"}
# techStackTwo = {"dotNET": "Microsoft"}
mergedStack = {**techStackOne}
print(mergedStack)


# ** is ot iterate over a dictionay
# once we have a default argument, all the arguments to its right must also have default values.
# This means Non-default arguments cannot follow default arguments
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# function definitions cannot be empty,
# but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.


def my_function():
    pass


# recursions python accepts recursions
# a defined function can call itself. be careful not to get infinite looping.


def tri_recursion(k):
    if k > 0:
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return (result)


tri_recursion(3)


# pascals series in row 1 row below other
n = int(input("n:"))
for i in range(1, n+1):
    C = 1
    for j in range(1, i+1):
        print(f"{C}", "", sep=" ", end="")
        C = C*(i-j)//j
    print()

# when multiple arguments are taken ex:


def mySum(*args):
    c = sum(args)    # each variable is depicted by args.
    return (c)


print(mySum(2, 3, 4, 5, 6, 6, 7))

# finding greatest number in given multiple arguments


def largestNumber(*numbers):
    c = sum(numbers)
    large = 0
    for i in range(c):
        if i in (numbers):
            large = i
        else:
            pass
    print(large)


largestNumber(1, 2, 6, 4)


# anonymous function a function without a name
# lambda argument : expression
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2)) format of lambda function
def my_function(n):
    return lambda a: a * n


mydoubler = my_function(2)
print(mydoubler(11))


def my_function(n):
    return lambda a, b: a * n + b


mydoubler = my_function(2)
print(mydoubler(11, 3))


# lambda function can have many arguments but one expression.
# Expression is evaluated first and value is returned

# the map(f, sequence) function applies function f to each element of sequence and returns a transformed list.

def squares(x):
    return x ** 2


list1 = [1, 2, 3, 4, 5]
print(map(squares, list1))
print(list(map(squares, list1)))

print(list(map(lambda x: x ** 2, list1)))

print([x ** 2 for x in list1])

# the filter(f, sequence) function applies the function to each element in the sequence and reutrns an ireator satisfies the condition in the function f.

a = [1, 2, 3, 5, 7, 9]
b = [2, 3, 6, 7, 9, 8]

# filter function
print(list(filter(lambda x: x in a, b)))

print([x for x in a if x in b])

seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))


# fruitfaul function:a function which returns a value. have a return statement if not then output is none

# scope is a textual region of a python program where a namespace is directly accessible

# order of search  local >enclosed>global >builtin
# we work in global scope
# non locall keyword for nested function similar to global keyword


# local variables declared inside a function.only statement inside a function can access it.
# global variable is visible to every function and can be used by any piece of code.
# when using a global variable inside a function, that variable needs to be declared as global,else a local variable of same name will be created.

globvar = "Hello"


def test1():
    global globvar
    globvar = "Good Morning"  # Here the global variable is updated


def test2():
    globvar = "Good Evening"  # Here a new local variable is created


# Main program
print(globvar)  # Before updating global variable value is printed
test1()  # Updated global variable value
test2()
print(globvar)  # updated global variable value "Good Morning" is printed

# function  composition return value of 1st function is passed as argument for second function.
# composition of f_1 and f_2 is given by f_1(f_2(x)).


# for composing multiple functions.
def compose(*functions):
    def inner(arg):
        for f in reversed(functions):
            # arg in f is the argument of the last function in compose order.
            arg = f(arg)
        return arg
    return inner


# recursive functions


# recursion may be faster but can be space consuming
# a normal function will be invoked by other functions,
# while recursive functions are invoked by directly or indirectly as long as the given condition is satisfied.
# conditions for a well defined recursive function:
"""
1)Base criteria: condition at which the recursion stops.
2) Recursive steps:each time a recursive call is made it comes closer to the base criteria.
"""
# types of recursion functions:
"""
1)direct recursion: one function is involved function calls itself directly.
tail recursion last recursive execution is function call
not tail recursive  recursive execution is not last step (n * (funciton(n-1))) seems tail recursive but its not
# head recursion after recursive statement other statement are there to be executed 
2) indirect or circular: two or more functions can be involved eg fun1 calls fun 2 fun2 calls fun3 and fun3 calls fun1.
"""
# carefully define exit condition so it doesn't lead to infinite loop.
# only user defined functions can be used in recursion,library functions dont have their source code visible.
# all recursive calls are pushed onto stack until end condition is detected it may cause stack overflow if depth is too high(>16000)

# conditon for chcecking divs by 7
# 10 a +b number a can be anything   a -2b is divisible by 7


# reversing a number using recursion
def reverse(n, x):
    if n == 0:
        return x
    else:
        x = n % 10 + x * 10
        return reverse(n // 10, x)


print(reverse(13, 0))


def gcd(a, b):
    c = max(a, b)
    for i in range(1, c+1):
        if c % i == 0:
            if min(a, b) % i == 0:
                gcd = i
    return (gcd)


print(gcd(3, 6))


# gcd using recursion
def gcd(a, b):
    if a == b:
        return a
    elif a < b:
        return gcd(b, a)
    else:
        return gcd(b, a - b)


a = 25
b = 45
print(gcd(a, b))

# lcm(a,b) using recurison and non recursion
# lcm(a,b) * gcd(a,b) = a*b


def find_lcm(a, b):  # user-defined function
   # choose the greater number
    if a > b:
        greater = a
    else:
        greater = b

    while (True):
        # find LCM
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


def find_gcd(a, b):
    if (b == 0):
        return a
    else:
        return find_gcd(b, a % b)

# find gcd and then a*b/gcd(a,b)


# odd even using recursion:
def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))


n = int(input("Enter number:"))
if (check(n) == True):
    print("Number is even!")
else:
    print("Number is odd!")


# fibbonacci series
# without recursion


def fibb(n):
    count = 0
    n0 = 0
    n1 = 1
    print(n0)
    print(n1)
    while count < n - 2:
        count += 1
        sum = n0 + n1
        n0 = n1
        n1 = sum

        print(sum)


fibb(5)

a1 = 0
a2 = 1
n = int(input("n: "))
print(a1)
print(a2)
for i in range(0, n-2):
    sum = a1 + a2
    a1 = a2
    a2 = sum
    print(sum)

# with recursion
# Fibbinnaci series with recursion


def fibb(n):
    if n <= 1:
        value = n

        return value
    else:
        value = fibb(n-1) + fibb(n-2)
    return value


n = int(input("n: "))
for i in range(0, n):
    print(fibb(i))


# Modules:
"""1)module contains a set of classes,functions, variables thaat got together to get a specific set of tasks done.
2) A module can be used by other modules.
3) modules reduces the length of the code
4) python files with  .py extension"""

# a module c=can be used by another module using import statement


# import modulename

# name all the folders with underscores from now
"""import sys
print(sys.path)
sys.path.append("D:\package")
# package.hello()
print(sys.path)
import package
package.hello()"""
# keep auto format off

# from course.mosh.getting_started import *
# import course.mosh.getting_started
"""import os
import sys
sys.path.append("D:\package")
import prince
prince.hello()"""


# from method for importing module
# from modulename import functionname1,functionname2,...
# the function can be used directly without the module name
# as keyword shorten teh length of the function name#
# from modulename import functionname as f1
# To import all the functions, constants, variables of a module use the symbol asterisk *.


# Directories  package is also lnown as directories can have other modules or packages
# each package should have a file called
# __init__.py can be empty but must exist it speco=ifies that the package and its modules can be imported.
# example pack 1 has __init__.py as wellas few modules and is ready to be imported.

# robot package which contains two modules car and house
# importing both modules
# import robot.car, robot.house

# from packagename import modulename
# Now functions can be called directly on module names.

# modulename.functionaname()


# module file containing a python code, code can be any thing classes,functions and lists


# namespaces system taht ensures teh names in program
# are unique and can be used without  used to keep track of variables functions classes etc
"""1) built in """
print(dir(__builtins__))

# builtins namespaces builtin system accessed when file is runned,
# global namespaces for a module each module has its own namespace two variables ina same namespace can not have same name for its
# global variables.Namespaces araae isolated name in one module can be used in another module
#
# regular imports : to differentaite modulename is prefixed before accessing the name.

# using from keyword if we have imported function/variable and defined function/variable in a file
# we go with the defined variable/function user cannot access the imported variable/function
# local namespaces for a function variable or class
# namespace holds names and each name is mapped with an object
# dictionary object type.
# namespace holds names of the current module along with imported modules.


"""scope reffers to a specific area of a program where the variable/names of that namespace doesnot need prefix.
scope provides with isolation inside a module generally current function/variable in which name is located.
"""
# global variable defined inside a module
a = 10  # global variable
# other functions can use the variable name but will have other value


def change():

    global a  # assignning a the global value
    a += 100
    return a


change()  # changest the  global variable
print(a)

"""def change1():
    a+=100
    return a
change1()
print(a)
Gives error
UnboundLocalError: local variable 'a' referenced before assignment
"""
a = 10


def change2():
    b = a + 10
    # function can still access the value of global a but can not modify it

    print(b)


change2()  # local a
print(a)  # global a


# def foo():
#     y = "local"
#     return y
# foo()
# print(y)
# gives error we are accessing a local variable in global space

x = "global "


def foo():
    global x
    y = "local"
    x = x * 2
    return x
    print(y)


foo()
print(x)  # global variable is modified.

# function inside a function local variable becomes global for second function and local of second is called non local


def outer():
    x = "local"

    def inner():
        nonlocal x  # similar to global
        x = "nonlocal"
        print("inner:", x)

    inner()  # changes the value of local variable
    print("outer:", x)


outer()

# local variables can not be accessed outside the function
# types of scope
# 1) local scope scope of a executing function
# 2) module level scope global set_completer
# 3) outer most scope built in scope

# print(str1) searches for str 1 in local scope>global scope>outermost scope.> if nothing found returns Name error.

# A dir() function lists the names of the function. When it is called globally, lists the global names.
print(dir())
# dir in global namespace


def func1():
    greeting = "Good"


print(dir())
print(dir(func1))


# cmath module has same functions as math not allare present but for complex nummbers.
# import cmath
# from import cmath as * doesnt work
a = complex(3, 4)
b = complex(4, 5)
c = cmath.sqrt(a)
print(dir(cmath))
print(c)
