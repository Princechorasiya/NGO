# string is a continous nsequence of unicode characters.
# computer stores 0 and 1  smallest unit 1 bit either 1 or 0.
# to represent characters we need a 16 bit system.
# unicode   system of storing various things
# index o to n-1
# if length is 1 then it treated as a character
# immutable


# we have 5 types of operations which can be performed on strings.
# 1)indexing
# 2)slicing
# 3)Concatentation
# 4)repetiton
# 5)Membership
a = "Python"
print(a[5:2:-1])  # -1 defines the direction if from right to left
# null string.
del a  # to delete the string

# slicing a string
# 1)slice(stop) or slice(start,stop,step) # inbuilt
# string[statr:stop:step]  step != 0;


# #reversing a string:
# str1[-1::-1]
# in to search the presence of a char/other string in it
# strings in python are immutable they cannot be changed after they are created
# deleting a character in python is not possible directly but we can del complete string by
"""del str"""

# built in string methods
"""string.methodname()"""       # way to utilize these strings
# 1) """capitalize()"""         used to capatilaize first letter of the string

# 2) """upper()"""           used to change the entire the string to upper case.
# 3) """lower()             it lowers teh string  or    casefold() it returns the string""" used to change the string to lower case
# 4) """title()"""          first word of all words are capialized
# 5)"""swapcase()"""        change upper case into lower and vice-versa
# 6)"""split()"""           change each word seperatedd by space into list
# 7) """
# b = "Python"
# print(b.center(10, '*'))           # will print result as follows
# '**Python**'
# """ 10  is width no of characters filled are  width-len(string) filled in both sides

# count(substring,start,end)            start and end are optional returns the count of substring in a string

# string.encode(encoding="UTF-8",errors = "strict")  for encoding
# replace(old,new,count)               replaces all old substings with new subsrings
# count how many occureences to replace  default all

# str.endswith(suffix,start,end)       //string or tuple to be verified
# str.startswith(prefix,start,end)         //to check if string start with

# str.find(substring,statr,end)           //return the first occureence of substring not found -1  start end optional
s1 = "hello\tworld\t!"
# print(s1.expandtabs(tabvalue))      //tab ssize optional \t into spaces

# format()
# //positional arguments
s2 = 'Hello {0} World {1}'
print(s2.format('beautiful', 'good morning'))

# //keyword para

s3 = 'Hello {name},good {timeofday}!'
print(s3.format(timeofday='afternoon', name='prince'))

greet = {
    'name': 'prince',
    'timeofday': 'morning',
}
print(s3.format_map(greet))
# //similar to format but works with dict

# str.index(substr,start,end)      //start and end are optional  returns first index;
# str.rindex(sustr,start,end) // highest found index is returned


# str.join(collection)                returns the string concatenated with the elements of an iletrable
# collecton can be list,set(random join set is unordered) ,tuple,dictionary(join key not value)


# str.ljust(width,fillchar) // left justified string of given width
# fillchar to fill remaining spaces  optional

S = 'Hello world'
x = S.ljust(20)
x = S.ljust(20, "#")
print(x)
y = S.rjust(20, "$")
print(y)  # right justified

# str.lstrip(charactertobestripped)   removing those characters from left  default = " "
# str.rstrip(charactertobestripped)   removing those characters from right  default = " "
# str.strip(charactertobestripped)   removing those characters from both side multiple character can be considered eg '.w'  default = " "

# str.maketrans(x,y,z)
# one character    dictionary with 1:1 map
# two char  make sure x and y are of equal length  every letter of x is every letter of y
# three char  every letter of z is deleted from the string
s = "hey,how are you?"
x = s.maketrans("h", 'z')
print(s.translate(x))

S = 'How are you? How have you been?'
x = S.partition('are')  # splits/parts on the basis of this parameter
print(x)
y = S.partition('you')  # first partition
print(y)
z = S.rpartition('you')  # last partition
print(z)
# gives (tuple with before separator,separator,after separator)
# if no occurrence is found then (string,'',"")

S = 'stop,look,go,stop,look,go'
x = S.rsplit(',', 3)  # right to left
# left to right(4 is max split determines how many splits we perform)
y = S.split(',', 4)
print(x)
print(y)


S = ''
x = S.splitlines()  # splits at line breaks
y = S.split()
print(len(x))
print(len(y))

"""b = '.'
L1 = ["www", "codetantra", "com"]
print(b.join(L1)) # will print result as follows
'www.codetantra.com'"""
"""print(len("%%Strings are immutable%%"))
str2 ="@"
print(str2.join(str1))"""
# gives @ after every word.

# isupper() to check if  all upper text case
# islower() to check if all lower case
# isalpha() to check if string contains only alphabetic letters only alphabets is true others are false
# isalnum() check alphanumeric characters alhabets and numbers
# space " " is considerd special character
# isdigit() check if all in the srings are digits.
# isspace() check if all are spaces
# istitle() check if the string is a title
# isdecimal()      checks for decimal

# subscripts and superscripts are digits
# fractions currency numerator fractions  are numeric not decimal

# a.find("value") returns lower index value
# a.rfind("value") returns higher index value.
# isprintable true if all characters are printable
# printable characters include alphabets,digits,symbols,punctuations and white spaces.


# escaoe characters ae used to solve the problem of using special characters inside a string
# "\n" new line
# "\" represent backslash
"""print("hello\\how are you")  # will print result as follows
hello\how are you"""


"""print("It\'s very powerful") # will print result as follows
It's very powerful
"""

# "\t" used to provide a tab space
"""r""
R""
repr(str1)"""
# three different method to say the complete statement inside is a string including any special characters.
# startswith(substring) checks if the main string starts with given substring
# endswith(substring) checks whether the strings ends with the substring
# find(substring() returns index of substring if found else -1
# len(a) lenght of the string
# min(a) returns the minimum characters in the string
# max(a) reurns the maximum character in the string


"""
import string
puncuations = string.punctuation
result = " "
str = "list -[]\n tuple - ()\n Dictionary - {}\n Comment - #\n Multiply -*\n not - !\n and - &\n or - |\n format specifier - %\n String - " " $ : : ' / + ="
for i in str:
    if i not in puncuations:
        result += i
print(result)
"""


# take a string split it into two alternate values and get back the original string fromt hem
# use the for loop or while loop while splitting the string
# and for getting the word back use the while loop.first[i] + second[j] i+=1 and j+=1 and i and j less than len of those words.

# Take string as input from the console using input() function. Write a program to find how many times each character is repeated in a given string.
# Print each character in the string in sorted order with a number of times it is repeated as shown in the example.
"""
str: Hello Python!
' '	1
'!'	1
'H'	1
'P'	1
'e'	1
'h'	1
'l'	2
'n'	1
'o'	2
't'	1
'y'	1
[' ', '!', 'H', 'P', 'e', 'h', 'l', 'n', 'o', 't', 'y']
"""
# use while loop and use replace on on str1 each time loop condition len(str1)>0


# string formatting 
# way to insert variable ora string in a predefined string.
# % operator takes tuple of variableas input and places them in specific places

# string  %s
# char   %c
# float     %f
# flaoting point exponent  %e
# signed integer Decimal  %d

my_code = 1113
my_name = "prince"
my_id = 23

# format using format()
# working woth default arguments  no need for number there just {}
# working with positional arguments
my_str = "variable is {2} and code of {0} is {1}".format(
    my_code, my_id, my_name)


# working with keyword arguments
mystr = "variable {my_code} {my_id} {my_name}".format(
    my_code=my_code, my_id=my_code, my_name=my_name)
print(mystr)
print(my_str)


# number formatting using format
my_num = -1234.34
my_str = "my number is  {}".format(my_num)
print(my_str)

# alignment using format  can be used with strings as well
# here default is space we can aslo use {:@<10} or any other symbol  //padding
mystr = "left aligned{:<10}.".format(my_num)
print(mystr)
mystr = "right aligned {:>10}.".format(my_num)
print(mystr)
mystr = "center aligned {:^10}.".format(my_num)
print(mystr)

mystr = "trunc aligned {:.5}.".format(my_name)  # trunc works on string decimal
print(mystr)

length = 20
# making it dynamic
mystr = 'dynamic {:>{}}..'.format(my_name, length)
print(mystr)

# in case output length is less than string length output is not alligned or padded but it canbe truncated


# using fstring
mystr = f"prince is {my_name}"
print(mystr)

# using %

mycode = input("Code od %c is" % (my_code))
print(mycode)



