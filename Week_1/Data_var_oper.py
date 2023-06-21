"""unit 1
"""
"""Python is an interpreted high level programming language for general programming purpose"""
# the set of instructions given to computer for performing a task is called program.
# python 1980 released python 0.9.0 feb 1991 python1 1994 python2.0 2000 python3.0 2008
# save python file with .py
"""
two types of errors:
1) syntax error wrong 


2)runtime error incorrect algorithm or invalid values.
 python easy to learn 2)emendable(python in c or c++ program 3)extensible (c or c++ can be added)
 """
# adding comments in python.#sign or'''and """can be used to add comments in a python file
# docstring comments after a string """ or''' are used to create docstring.

import keyword # We have to import keyword module
print("hello world")
print(1/0)

print(object(s), sep="/", end="\n", file=file, flush=False)
# sep how to separate the object inside the same parameter
# end          prints something after all values are printed
# file is where to display the file  default sys.stdout (screen)

# flush default false sends data to buffers true flushes the buffer


# an identifier is a name used to identify a variable,function,class,module or object.eg name or age
# python is case-sensitive. an identifier can start with _but not with numbers.Keywords cannot be used as identifiers.
# Special symbols are not allowed in identifiers._name  private variable __name strongly private
"""Keywords"""
# python 2 32 python 3.5 33(nonlocal)

# Here 'and' is a keyword so it prints True as output
print(keyword.iskeyword('and'))


# variable reserved memory location used to store data = sign t a variable can store one value no more
#
# associating a variable with a value is binding.
#
# python allows us to assign a single value to multiple variables.is used to assign the variable.Python interpreter automatically

my_var = 12
# determines the data type acccording to data assigneed to it. at a momen
value1, value2, value3 = 1, 2.5, "Ram"


# indentation
"""while defining things four spaces or 1 tab is indented."""


# // datatypes

# Data types
"""
Number
String
List
Tuple
Set
Dictionary"""

variable_name = "hi"
type(variable_name)  # returns the variable data type.
# numbers
"""1)int
2)float
3)complex a+bj format"""
# string data type
"""1)' ' 
2)"" 
3)''' '''  """
# the computer doesn't see letters each number we enter is a number in memory python use unicode encoding for character representation.
# an individual character within string is accessed with index index 0 to n-1 where n is no of characters
# -1 means last number while -2 refers the last second number.
# we use triple double quotes  to create multiple line string.


# list data type multiple value of different data types.
a = 2
list = [1, 1.3, "one", a]
print(list)
"""index 0 to n-1 n is no of items in the list -ve index means from the end -1 corresponds to 
last element in the list."""
print(list[0])  # for printing elements of the list.
# slicing  a list  used to access a subset of a list
# value at index 3 is not included. if starting index or stopping index is not mentioned then it is considered s 0  or end of the list.
print(list[1:3])
# + is used as concatenation and * is used as repetition operator
print(list+list)
print(3*list)

# nested list
list1 = [2, 3, 4, 5]
list2 = [list, list1, 2, 3, [2, 3, 4]]
print(list2)
# to print the nested list use index  to print elements from that list use another index
print(list2[1][0])

# set mutable unordered collection of items.
# every element is unique and must be immutable but set itself is mutable.
# mutable data type like list,set ,set and dictionary can not become part of a set.
# empty curly braces doesn't make an empty set but an empty dictionary
set1 = {1, 2, 3, 4, 5}
print(set1)
myset = set()  # creates an empty set
# myset1=set(1,2,3,4) this doesn't work

# tuple are placed btw () and their elements are immutable can be only said to read only lists
tuple1 = tuple()  # empty tuple
mytuple = (1, 2, 3, 4, "Data types")
print(tuple1)
print(mytuple)
# trailing cooma is mandatory for the one element tuple,or else it prints data type of thee element entered.


# dictionary
# a dictionary has a key:value pair  keys should be unique while values may change.
# immutable data type are used for key while any data type can be used for value.
a = "prince"
dictionary = {"hyderabad": 27, "chennai": 34, a: 354}
print(dictionary)
mydict = dict(hyderabad=20, Delhi=30)
print(mydict)
# st2cap[state] = capital
# adding new elements in a dictionary

# Data type conversion
# int(x=0,base=10) format default=10
s = "0011"
print(int(s, 2))  # string to int using base 2)
print(int(s))

# float
a = "12.34"
print(float(a))

# ord used to get integer representing a unicode character
# if the length of the string is greater than 1 then ord() prints type error
print(ord("a"))


# hex() converts an integer to hexadecimalstring
print(hex(45))
# to remove 0x from the printed value. float in hex is gives type error
print(hex(45).replace("0x", ""))

# oct(x) integer to octal
print(oct(34))
print(oct(34).replace("0o", ""))

# complex()
print(complex(3, 4))

# str(x)  format=str(object=b'',encoding='utf-8', errors='strict')
print(str(2))


# eval(str) runs the python code wtihin the program
a = 100
b = 3
print(eval("a+b"))


# chr() returns a string from an integer (unicode value of the character)
print(chr(343))  # range(0,1114111)


# tuple() converts any  tuple
str = "python"
print(tuple(str))

# set() converts any data type to set
print(set(str))

# list(0
str = "python"
e = str.split()  # converts it to set

print(e)
print(e[0][1])

s = "pyt hon"
x = [i for i in s]
print(x)


# dict(d) used to create tuple but d must be a  tuple of order(key,value)
mytuple = ((1, 'a'), (2, "b"))
print(dict(mytuple))
print(dict((y, x) for x, y in mytuple))
list1 = [1, 2, 3, 4]
list2 = ["a", "b", "c", "d"]
mydict = zip(list1, list2)
# print(set(mydict)) #if both used together we get some errors.7
g = set(mydict)
print(sorted(g))


print(format(10.345, "10.2f"))
x = float(input("Enter the value:"))
print(round(x, 2))
# format to round off
y = float(input("Enter the value:"))
print(format(y, ".2f"))
print("{0:.2f}".format(y))
print(format(67.987, "10.2%"))
print(format(y, ".2%"))
print(format(20, "10x"))  # hexa decimal
print(format(20, "10o"))  # octal
print(format("Hello python", "25s"))
print(format("Hello python", ">25s"))
print(format("Hello python", "<25s"))


#


# operators
# 1)arithmetic operators

# operators
a = 17
b = 3
print(a+b)  # addition
print(a-b)  # subtraction
print(a*b)  # multiplication
print(a/b)  # division
print(a % b)  # modulus or remainder
print(a//b)  # gives the quotient(integer)


# 2)comparison operators
# gives result in true or false
"""
== equalto
!= not equalto
< less than
> greater than
<= less than equal to
>= greater than equal to
comparison operators works on strings also it compares there unicode value
"""


# augmented assignment
a = 12
b = 3
a += b  # a=a+b similarly +=,-=,*=,/=,%=
print(a)

# 3)assignment operator += and others.


# bitwise operator
"""
1) << (left shift) mutliply 12 in bit 1100 """
print(12 << 2)

# 2 >> (right shift)
print(12 >> 2)
# 3 & (and)
print(3 & 5)


# bit wise operators
# bitwise AND  Find common values in their bits
# 128.64.16.8.4.2.1
# 0011  3 in binary
# 0101 5  in binary
# 0111 7
print(3 & 5)  # prints common in them
print(4 & 5)
# bitwise OR | #union common factor+uncommon factors.
print(3 | 5)
# bitwise XOR ^  #same values output =0 differnet value=1
print(3 ^ 7)  # 0101 output in bits
# bitwise NOT ~
print(~5)  # returns one complement of the number -6 is the output
# right shift >> 4=0100 shfit>>2 takes the value of 4 to two palces right.
print(4 >> 2)
print(8 >> 1)

# left shift << 4=0100 shift<<2 takes the value 2 palces left
print(4 << 2)


# Logical operators either true or false
"""
1 stands for true 0 stands for False
1) and true when both conditions are true
2) or the result is true if any of them is true.
3) not the result negates the operand"""


gender = input("M or F: ")
age = int(input("age: "))
if gender == "M" and age >= 65:
    print(234)


# The function abs(num) computes the absolute value of a number.


# member ship operators.
# in and not in operator right hand side can be string list tuple set or dictionary.
# left hand side can be any string/number
print("3" in "345")


# Identity operator

# is operators


# list of operators.

"""

** Exponent

~ + - Complement, plus and minus(unary)

* / % // Multiply, divide, modulo and floor division

+ - Addition and subtraction

>> << Right and left bitwise shift

& Bitwise 'AND'

^ | Bitwise 'XOR' and regular 'OR'

<= < > >= Comparison operators

== != Equality operators

= %= /= //= -= += *= **= Assignment operators

is and is not are Identity operators

in and not in Membership operators

not, or, and are Logical Operators"""


# taking inputs
a = input("Enter your name: ")
b = int(input("Enter the number: "))
