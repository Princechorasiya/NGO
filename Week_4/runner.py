# # score user
# # we can use database

# # file as storage unit
# # read data from file write data from file update data
# # file = open("text.txt", "w")
# # file.write("afkgfkjg")
# # file.close()


# # r
# # w
# # r++
# # w+
# # a
# # a+


# # open the file in the required mode
# # process the data

# # close the file


# # with open("text.txt", "r") as f1:
# #     # a = f1.read()
# #     # print(a)
# #     b = f1.readlines()
# #     print(b)

# # with open("text.txt", "w") as f1:
# #     f1.write("add")


# with open("text.txt", "a") as f1:
#     f1.write("56")   # 40sec
# # buffer  ->>> rom after program execution

# # a  b
# # 10  5
# # 10  15   25


# with open("text.txt", "r") as f1:
#     a = f1.read(2)
#     print(a)


# # '\n' new  line
# # djfk

# # fkjjjgjfgksfgkjhkfkghkshkjgshfj

# # line
# # line2
# # line3


# # buffer ram   rom(harddisk)/


# errors synatx error ///compile time


# run time error /
# error
# compile time syntax ,indentation error

# run time zero division error


def divide(a, b):
    return a/b


# print(divide(3, 0))
# print(divide(3, 4))


# try

# except
# try:
#     print(divide(3, 0))
# except Exception as e:
#     print("error", e)

# # indexError list list[0] 5  6  01 234

# print(divide(3, 4))

# try:
#     a = int(input("enter a: "))
#     b = int(input("enter b: "))
#     print('after division', divide(a, b))
#     a = [1, 2, 3]

#     print(a[3])

# except (IndexError, TypeError):
#     print('index error or type error')

# except (ZeroDivisionError):
#     print('zero division')

# def isempty(a):

#     if (type(a) != str):
#         raise TypeError('a has to be a String')
#     if (not a):  # a= null
#         raise ValueError('a cannot be null')
#     a.strip()
#     if (a == ""):
#         return True
#     return False


# try:
#     a = "     "
#     print('is empty', isempty(a))
# except ValueError as e:
#     print('value error', e)
# except TypeError as e:
#     print('Type error raised:', e)


# no exception is raised

# try:
#     b = 10
#     c = 0
#     a = b/c
#     print(a)
# except:
#     print('exception rasied')
# else:
#     print('no exception rasied')


# try:
#     temp = [1, 2, 3]
#     print(temp[0])
# except Exception as e:
#     print('in exception block', e)
# else:
#     print('in else block')
# finally:
#     print('in finally block')



# uses of the try catch block 
try:
    f1= open()
    #more code
except Exception as e:
    #some code 
finally:
    f1.close()


# other code 

# connect to a database
# file database 

# connection to the db 
# try:
#     #connect 
# except :

# finally:
#     # close the connection 
    
# fetch data  

# datbases fetch 

# line 1   fetch data taking time 5sec -10sec till loading 
# try:
    
# luen 
# djgkdhg

# fghjf

# fgfh
# gkfjg
# manipulate data 

# syntax error 
# list =[]
# runtime index out of range zero  type value  
# c 
# malloc realloc 
# array size is fixed  dynamic memory  
 

# 500
# 1000


