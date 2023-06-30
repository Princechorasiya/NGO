list1 = [1, 3, 4, 5, "data"]
# belong to class list

# list(var) // var can be string dict,tuple number,set
# list is a constructor
# two list are equal if both have same order of elements
# list are mutable


# list methods

# append()           add elements the end

# extend()             extend by adding specified iterable

# insert(index,element)                insert at defined index

# pop()                     Returns and removes an item from the list from the specified index position

# clear()                 removes all the elements

# count()                 return the number of item passes as an argument


# # sort()                sort in ascendiing order

# reverse()               reverses the list

# copy()                  returns a copy of list

# index()                 index of the item

# # nesting list list inside list
# index 0 to n-1 or
# -n to -1   floats as index gives error


# slicing
# list_name[start:stop:step]

# changing element
#  list[i] = newvalue

# adding 2 list + gives [list+list2]

# print(list*4)  repeats the list

# deleting item
# del list[i]


# list comprehension
mul_list = [i*2 for i in range(1, 6)]  # if for can also be included

even_squares = [i for i in range(1, 23) if i % 2 == 0]


# built in list functions
# max(list)
# min(list)
# len(list)
# list(seq)
# sum(list)

# reduce()     reduces the list into single expression
# numbers = [1, 2, 3, 4, 5, 6]
# sum = reduce((lambda x, y: x+y), numbers)
# print(sum)

# any()          true if any item of list is true

# map()             map function  to iterable
# all()               true if all true
# cmp(list1,lsit2)        compares list1 and list2

# membership operation

# in

# iterating through list
# car in list
