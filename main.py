# #Decorator In python
#
# def function1():
#     print("Subscribe Now")
#
# # Note no Parathesis Here
#
# function2 = function1
#
# # Note here we deleted the main function
# # But still the function 2 will work as a copy is already being made
# del function1
#
# function2()

# def funcret(num):
#     if num == 0:
#         return print
#
#     if num == 1:
#         return sum
#
# a = funcret(0)
# print(a)

# def executor(func):
#     func("this")
#
# executor(sum)

# Decorators In Python

def decorator1(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexec




def anotherFunction():
    print("I Am jainam shroff")

tempVar = decorator1(anotherFunction)

# it is useful when we have to work/modify more than one function at once
# we use decorator to do so


tempVar()