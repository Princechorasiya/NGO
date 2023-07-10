# # # tuple
# # my_tuple = (1, 2)
# # print(my_tuple[0])


# # print(my_tuple)
# # print(my_tuple[-1])
# # my_tuple_2 = my_tuple[0:1:1]
# # print(my_tuple_2)

# # my_tuple = (1, 2, 3, (1, 3), [12, 34, 4], "strings")
# # del my_tuple_2


# # my_tuple_2 = tuple([1, 3])
# # print(my_tuple_2)


# # # set
# # my_set = {1, 2, 3, 2}
# # print(my_set)


# # my_set.add(4)
# # my_set.remove(1)
# # my_set.discard(2)

# # print(my_set)


# # dict

# my_dict = {1: 2, 3: 4,
#            "name": "prince"}

# print(my_dict)
# print(my_dict["name"])

# my_dict[1] = 56
# my_dict[90] = "abc"


# for i in my_dict:
#     print(i, "\t", my_dict[i])

# my_dict_2 = dict()
# print(my_dict_2)

# 4/7/23


# oop
# class

# object
# car engine seats company

class Prince:

    # def __init__(self):
    def __init__(self, name):
        self.name = name

    def showName(self):
        print(self.name)


obj1 = Prince("prince")
obj2 = Prince("abc")

obj1.showName()
obj2.showName()


print(0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23 +
      0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23+0.23 == 6.9)
