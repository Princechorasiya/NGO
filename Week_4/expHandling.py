# errors detected during program execution
# exception halts the program at the steps


# try
# allows us to write the code that is prone to exception  exception occurs except is triggered

# all exceptions are in Exception class

# except runs when try raises exception


def divide(a, b):
    return a/b


try:
    divide(10/0)
except Exception as e:  # to check the type of error /
    print("erroe", e)


# except catches all excptions
# catching specific type of exceptiom

try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print('after division', divide(a, b))
    a = [1, 2, 3]
    print(a[3])  # exception will raise index error

except (IndexError, TypeError):
    print('index error or type error')

except ZeroDivisionError:
    print('zero division error')

# raising custom exceptions  exception that a programmer might raise if they have a requirement ti  break the flow of code in specific scenario


def isempty(a):
    if (type(a) != str):
        raise TypeError('a has to be string')
    if (not a):
        raise ValueError('a cannot be null')
    a.strip()
    if (a == ""):
        return False
    return True


try:
    a = 123
    print('is empty', isempty(a))
except ValueError as e:
    print('value error', e)
except TypeError as e:
    print('Type error raised:', e)


# try except else  run specific code when noo exception occur

try:
    b = 10
    c = 2
    a = b/c
    print(a)
except:
    print('exception rasied')
else:
    print('no exception rasied')

# try finally code inside finally will always run
try:
    temp = [1, 2, 3]
    temp[4]
except Exception as e:
    print('in exception block', e)
else:
    print('in else block')
finally:
    print('in finally block')


# when we need to run some part irespective of anuthing we use finally

# what happens when errors are raised in except block
# finally gives us a chance to handle it
# finally block wont be completed beyond point where exception occurs

# else and finally are optional

# assert keyword  verify logical assumptions  recognixe issue right fof thr bat
# rather than making other operations fail
# assert <condition> ,<error message>
# similar to
if __debug__:
    if not (5 > 1):
        raise AssertioError()

# assert makes the code more readable and we can disable it
assert True
# assert False, "this statement is false."

# assert terrminates the program but what if we dont want ot happen  use it with try-except block

try:
    x = 1
    y = 0
    assert y != 0, 'divison by zero is not possible'
    print(x/y)
except AssertionError as a:
    print(a)

# dont use paraentthesis using
assert uses
# exit()  closes everything  returns integer exit status to os.
# and
# abort()    may not close everything may result in abnormal termination


# assert is mainly used for debugginh purpose not for flaging "file not found error"

# checking parameter type/classes/values
# checking cannot happen situation
# documentaion of understanding     used for documenting the program
