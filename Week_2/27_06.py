# # # string = "hello {0} {1}"

# # # print(string.format("prince", "good evening"))

# # # digit 01234
# # # alphabets a bc
# # # upper
# # # special symbols

# # # print(" ".isalnum())
# # # alphanum means alphabets + number

# # # print("Prince".isalpha())
# # # print("Prince123".isalpha())


# # # print("1".isdigit())

# # # print("A".isupper())

# # # isupper
# # # islower
# # # isprintable
# # # isspace
# # # isdigit
# # # isalpha
# # # print("".isprintable())

# # # join
# # # p = ""
# # # list_string = ["rock", "paper", "scissor"]
# # # print(p.join(list_string))
# # # print("   ".isspace())


# # # len
# # name = "hhhhhhhhhdjfidjkgj"
# # # print(len(name))

# # # character code
# # # a  "97"
# # # 0
# # # 127
# # # print(ord("a"))
# # # print(ord("b"))


# # # print(min(name))
# # # print(max(name))
# # # print(name.find("h"))


# # # user_Score=0 and comptuer_Score =0

# # # while(user_Score <10 and computer_score<10){
# # #   #code

# # #   if(computer_wins){
# # #     computer_score +=1
# # #   }
# # #   if(user_wins){
# # #     user_Score +=1
# # #   }
# # # }


# # # functions

# # # definition

# # # calling out function


# # # functions type
# # # user defined and pre-defined

# # a = 2
# # b = 4
# # c = 0


# # def sum1():
# #     global c
# #     c = a + b
# #     # return a+b


# # def sum2():
# #     # global c
# #     # c = a + b
# #     return a+b
# #     c = 9

# # # runfun <sum2


# # # c = sum2()

# # # print(c)

# # # parameters and arguments
# # def sayHello(fname):
# #     print("Hello", fname)


# # name = "prince"
# # # sayHello(name)


# # def Greetings(fname, greet):
# #     print(fname, greet)


# # greet = "good evening"

# # Greetings(name, greet)


# # 22_8

# from functools import reduce


# def showName(fname, lname):
# #     print(fname+" "+lname)


# # showName("a", "b")

# # showName()
# # showName

# def funcTwo(*args):
#     print(args)
#     # print(args[0])
#     # if (len(args) >= 1):
#     #     print(args[1])

#     # print(args[2])


# # args = (1, 2)
# # args[0]
# # args[3]  error
# # index out of bound


# # funcTwo("prince")
# # funcTwo("a", "b")
# # funcTwo("a", "b", "c")


# # showName(lname="b", fname="a")  # keyword arguments
# # showName("b", "a")


# def funcThree(name="a"):
#     print(name)


# # funcThree()
# # funcThree("b")


# def funcFour(**args):
#     print(args)


# # my_dict = {
# #     "key": "value"
# # }

# # funcFour(fname="a", lname="b")

# # funcFour(fname="b")


# list1 = [1, 2, 3, 4, 5, 6]

# # define a func
# # to calculate the sum of a list


# def listSum(list):
#     sum_list = 0
#     for i in list:
#         sum_list += i

#     return sum_list


# # print(listSum(list1))
# sum_list = listSum(list1)
# # print(sum_list)


# # Scope

# # visibility
# # global
# # local

# global_Var = "i am global"


# def defineLocal():
#     local_var = "i am local"
#     print(global_Var)


# # print(global_Var)
# # defineLocal()
# # print(local_var)

# # lambda function
# # anonymous functions
# # def sum(x, y): return x+y
# # sum = lambda x,y:x+y


# # print(sum(2, 3))
# list_map = [1, 2, 34, 5, 6]
# # //map


# squared_list = map(lambda x: x**2, list_map)
# # print(list_map)
# # print(list(squared_list))

# # reduce
# # from functool import reduce
# # import functool
# # sum = reduce((lambda x, y: x+y), list_map)

# # print(sum)
# # //even number remainder by 2 =0
# filtered_list = filter(lambda x: x % 2 == 0, list_map)
# print(list_map)
# print(list(filtered_list))


# # recursion
# # function calling itself

# # def funcRec():
# #     funcRec()

# # # factorials

# # while(True)
# # Infinite loop

# # memory primary

# # recursions
# # stack memory (limited  )
# # stackoverflow

# # recursion
# # base condition
# # function call as the function calls itself

# def reverse(n, x):
#     if n == 0:
#         return x
#     else:
#         x = n % 10 + x * 10
#         return reverse(n // 10, x)  # reverse(1,3)  reverse(0,31)


# # reversing a number
# # finding the remainder 10 \
#   # // quotient


# print(reverse(13, 0))


# # gcd hcf

# def gcd(a, b):
#     c = max(a, b)  # 23 32
#     for i in range(1, c+1):
#         if c % i == 0:
#             if min(a, b) % i == 0:
#                 gcd = i
#     return (gcd)


# def gcd1(a, b):
#     if a == b:  # 23  4
#         return a
#     elif a < b:
#         return gcd(b, a)  # 4 19  1  4 15 4 11
#     else:
#         return gcd(b, a - b)  # 19 4   15 4  11 4


# print(gcd1(56, 28))


# # lcm * hcf = a * b

# # one more example and important math


# def fibb(n):
#     if n <= 1:
#         value = n

#         return value
#     else:
#         value = fibb(n-1) + fibb(n-2)
#     return value


# n = int(input("n: "))
# for i in range(0, n):
#     print(fibb(i))


# 0 1 1 2 3 5 8 13 21

# list
# set
# # dictionary

# oop 3-4
# file handling error handling
# math lib

# print(pow(2, 5))
# print(max(34, 54))
# print(min(34, 54))
# print(abs(-34))
# print(round(3.4))


# import math
# sum1 = 0.003 + 0.003 + 0.003 + 0.003 + 0.003 + 0.003 + 0.003 + 0.003 + 0.003 + 0.003+0.003 + 0.003 + 0.003 + 0.003 + \
#     0.003 + 0.003 + 0.003 + 0.003 + 0.003 + 0.003+0.003 + 0.003 + \
#     0.003 + 0.003 + 0.003 + 0.003 + 0.003 + 0.003 + 0.003 + 0.003
# print(sum1)

# 0.003 *30 = sum1

# floats are representation of the number


# list
list1 = list()
# print(list1)

list1.append(1)
# print(list1)
# list1.append([1, 2, 3])

# print(list1)
list1 += [4, 5]
# print(list1)

list1.extend([6, 7])
# print(list1)

list1.insert(0, 8)
# print(list1)

print(list1.pop())

# list2 = [1, 2, 3]
# list2.clear()
# print(list2)

print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)


# nested_list = [1, [23, [45455, [454]]],]

list1[0] = 89
print(list1)


# comphrensions

list_comp = [i for i in range(1, 23) if i % 2 == 0]

# for i in range(1, 23):
#     list_comp[i-1] = i
print(list_comp)

# print(3 in list_comp)
new_list = list_comp[1:5:1]
print(new_list)

new_list = list_comp[1:7:3]
print(new_list)
