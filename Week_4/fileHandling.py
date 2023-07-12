# filehandling   opening racing appending deleting
# need to store daat for future reference

# open(filenmae, mode)

# modes
# r    read only
# rb      read in binary
# r++   open for reading and writing  (pointer at first line)
# rb+    same as r++ but binary
# w        open for writing         overwrites it if the file is not present creates one
# wb            writing binary
# w+                        open for reading and writing ,other things same as w
# wb+     w+ but binary
# a    append pointer at the end  of the file
# ab         append binary
# a+           reading and appending
# ab+     same as a+ binary

# file = open('text.txt', "r")  # to open the file
# file.close()  # to close the file
# file.closed()  # to check if file si closed


# mode default is read mode
# maintain file in same directory or provide the full path of the file


# we can use with statemetn makes it easier no need to close the file
import pathlib
import shutil
import os
with open("file.txt", "r") as f1:
    # a = f1.read()  # to read the file
    # print(a)  # all the lines
    b = f1.readlines()  # to read the file as a list each line is a new element
    print(b)

with open("file.txt", "a") as f:
    f.write("append prince")  # appending

with open("file.txt", "r") as f1:
    c = f1.read()
    print(c)
 # no need to close the file

# text file  terminating character is \n
# binary file no terminating character

# r for raw no special character are present  \t or \n etc
file_object = open(r"file.txt", "r", encoding="utf-8")

file_object.close()  # close the file

# a better way to open this is

try:
    file_object = open(r"file.txt", "r", encoding="utf-8")
finally:
    file_object.close()  # close the file


# it is recommended to add encoding too

file_obj = open('file.txt', 'r', encoding='utf-8')
# print(file_obj.read())  # //to read all
# print(file_obj.read(5))  # first 5 characters
print(file_obj.tell())  # tells the cursor position

# file_obj.seek(14)  # points to 14 th char
print(file_obj.tell())      # now we can read form 14


# reads a single line  we can add n characters if we need
# print(file_obj.readline())

print(file_obj.readlines())       # returns the list


# working with binary files choose specific mode
# return type is binary string not text string


# writing a file in python
# write()      function to add in a single line
# next write statement adds to next line if we have to keep previous
# content we need to use append mode

# writelines()
# line = ['line', 'line2', 'line3']  # list of lines
# f.writelines(line)

# working with binary
# arr= [1,23,4]
# arr1 = bytearray(arr)  #convert into byte
# f.write(arr)
# f.close()

# deleting a file
# three ways
# os
# shutil
# pathlib

# filepath = <file_path >
# if os.path.isfile(file_path):
#     os.remove(filepath)
# else:
#     print('file does not exist')

# clear a directory
os.rmdir('directory')  # same dir relative path is fine else complete path
# dir must be empty

# shutil      high level file operaton module

shutil.rmtree('path')  # dir doesn't need be empty cannot delete a single file


p_obj = pathlib.Path('path')
p_obj.unlink()
# deletes the file
p.rmdir()  # toremove directory  empty file needed here

# with statement
# file is opened data is stored in buffer temporary
# buffer place to sotre something temporarily

# we open perform operation but forget to close the file

# no changes occur to file our progress is lost
# this has 2 way to deal
# try finally
# or
# with statement(__exit__ to close the file i with)
# __enter__ is executed first then
# __exit__  three arguments
# execution_type  class exception
# execution_value       type of exception
# traceback   is a traceback object  no exception  all three(none,none,none)
