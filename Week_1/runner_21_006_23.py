# operators/

# Arithmetic operators

# + - * /  // ** %

# a = 3
# b = 2
# print(a+b)  # 5
# print(a-b)  # 1
# print(a*b)   # 6
# print(a/b)  # 1.50
# print(a//b)    # 1
# print(a % b)  # 1
# print(a**b)   # 9


# Augmented operators
# +=  -= *= /=  %=

# a+= b it means
# a = a +b

# a = 3
# b = 2
# a += b
# print(a)
# a -= b
# # a = a-b
# print(a)
# a *= b
# # a = a * b
# print(a)

# a /= b
# # a = a/b
# print(a)

# a **= b
# # a = a ** b
# print(a)

# a %= b
# print(a)


# comparison operators
# < > <= >= == !=
# // True or False

# c = 10
# d = 30

# print(c < d)
# print(c > d)
# # >= <=
# print(c <= 10)

# print(c == d)

# print(c != d)
# # c and d equal then false
# c and d are not equal then true

# logical operators

# and
# condition1 and condition2

# F  and    F     F
# F  and    T     F
# T  and    F     F
# T  and   T      T

# print((2 < 3) and (7 > 6))


# or

# or
# condition1      condition2
# F     F       F
# F     True    T
# T     F      T
# T     T      T

# print((2 < 3) or (5 > 6))


# Shortcicircuiting

# and
# false          false

# or
# true    True

# not
# print(not (True))


# taking input

# my_first_input = input()
# print(my_first_input)
# my_first_input = input("Enter your name: ")
# # print("Your name is", my_first_input, "you")
# print("Your name is"+my_first_input + "you")

# string contact

# b = int(input("Enter your number: "))
# print(b)

# b = float(input("Enter your float: "))
# print(b)


b = eval(input("Enter anything: "))


print(b)
