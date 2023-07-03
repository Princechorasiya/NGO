# tuple immutable class tuple
# similar to list
# indexing is there index slicing nesting can be done
# negative indices are availabe

# we can update and redefine the tuple but not update the same tuple

# concating two tuples +
# del temptuple  delete the whole tuple but not the value


# inbuilt functions
# cmp(tuple1,tuple2)
# len(tuple)
# max(tuple)
# min(tuple)
# tuple(seq)
# count()


# slicing start:stop:step
# 


# ordered    retains the order in which data is  added

# unordered no such data is stored


# set collection of distinct objects forming a group
# set cannot contain duplicate elements
# elements of set are immutable
# class set
# elements can be added orremoved but not changed

# set does not maintain the order of insertion


# set of collection of item where every element is unique and immutable however set itself is mutable

# creating set in python
# {} curly braces
# set()  method

evennum = {2, 2, 3, 4}
# only unique values

print(evennum)

list1 = ["a", "v", 'a']
print(set(list1))
# while using set() if we pass dictionary we get a get key in the set
# elements of set are immutable so we cannot enter list as as set element

# no indexing
# add()  single element
# update()  multiple elements takes an iterable as input

# set.remove()    removes element not present gives error
# set.discard(element) // removes element not present remain unchanged
# set.pop()        removes randomly

#  in not in to check membership


# set.clear()        delete all of the set
sorted(set) // return sorted set

# operations

# union  set |set  or set1.union(set2) can be used for multiple set as well set1|set2|set3

# intersection  set &set  or set1.intersection(set2)
# x.intersection_update(y)    update the set calling this method


# difference  a-b means all elements of a removed from a
# set1 - set or set1.difference(set2)
# set1.difference_update(set2)        updates the set calling teh mehod


# syymetric difference   removes items present in both other remain same and get into a single set
# set.symmetric_difference_update(s)       updates the est calling this method
a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)
print(a.symmetric_difference(b))


# frozen set  creates immutable set
z = frozenset(['one', 'two'])
print(z)
# generally used to dictionary key

# looping
for i in z:
    print(i)

# built in functions
len(set)
# x.copy() and = are different  = refers to the same set


# a.isdisjoint(b)    intersection is null
# a.issubset(b)           setb subset of set a
# a.isuperset(b)


# dict 


# key value format
# key are unique key are immutable(string,numbers,tuple)
# value can be anything
# mydict = {}
# dict() used to create dictionary

# dict[key]  gives the value  if key is not present gives key error

# dict[key] = value adding new value(key not present before) or
# updating value(key is present)

# value can be anything (multiple values (any data type )) in a single var

# nesting  value is another dictionary

# deleting dictionary item
# del my_dict[key]
# dict.pop()  value as return
# dict.popitem()     key value from dict random


# my_dict.clear()     //clear the entire dict
# del mydict  deleter entire dict
# dict[key] = value updating the value or adding new value

# zip()  returns iterator of tuples stops when the shortest iterable is exhauseted
# zip(list1,list2)  /dictionary

# dict.get(key) //get value
# membership
# in not in

# dictionary comprehension

# syntax
# {key:value for vars in iterable }]
list1 = [1, 2, 3]
list2 = [1, 2, 3]


# iterating over a dictionary
#  for x in mydict: //gives the keys
# for x in mydict:
#     print(mydict[x]) //iterating values


# for x in mydict.items():
#     print(x)     //(key,value ) tuple

# for x in mydict.values():
#     print(x)  //print values /

# duplicate key is not allowed  key are immutable


# built in functions

# cmp(dict1,dict2)
# len(dict)
# str(dict)
# all(dict)
# any(dict)
# sorted(dict)  //returns soreted dict

# # dict methods
# dict.clear()
# dict.copy()
# dict.pop()        //removes element for specifed key
# dict.setdefault(key)  sets the default for get method
# dict.get()      get value for specified key
# dict.fromkeys(iterable)     key from iterable and value from value from dict

# dict.items()      list of key value tuple pair
# dict.keys()             list of keys
# dict.update(dict2)        add dict 2 to dict
# dict.has_key()         check if key is present or not

# dict1.update(dict2)



# blue ball convert into red dip all at once or one by one

# comprehension  generating new seq from existing seq


# we replace the for loop for simple statement
# red_list =["red" for list_item in blue_list]

# list1 = [i+j for i in range(a) for j in range(b) if i ==b]


# list comprehension
# new_list = [expression for item in iterable if condition]


# dictionary comprehension
# single iterable
# my_dict  = {key:value for item in iterable}
# double iterable
# my_dict = {key: value for (key, value) in zip(iterable1, iterable2)}

# set comprehension
# red_set = {i for i in iterable}


# nested comprehension
# use nested comprehension only when needed as it increases
# # complexicity

# creating 3 *3matrix

import numpy
m = []
for i in range(3):
    m.append([])
    for j in range(3):
        m[i].append(j)
print(m)

# nested comprehension
m1 = [[j for j in range(3)] for i in range(3)]
# can increase complexity in some case

# transposing matrix
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# use while loop
i = 0

m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
while i < len(matrix):
    j = 0
    while j < 4:
        m2[j][i] = matrix[i][j]
        j += 1
    i += 1
print(m2)

# using for loop
for i in range(3):
    for j in range(4):
        m2[j][i] = matrix[i][j]

print(m2)


mt1 = [[matrix[j][i] for j in range(len(matrix))]
       for i in range(len(matrix[0]))]
print(mt1)

t_matrix = zip(*matrix)
print(list(t_matrix))

# using numpy
# matrix1 = [[1, 2, 3], [4, 5, 6]]
# print(numpy.transpose(matrix1))

# mat = [[1, 2], [3, 4]]
# print(numpy.transpose(mat))

# sparse matrices  most of the values are 0
#  less storage and computing time

# aliasing copying
