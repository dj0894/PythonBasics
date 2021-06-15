# define basic function
def func1():
    print('I am functioon')

# functions that take arguments


def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that return a vale


def cube(x):
    return x*x*x

# function with default value for an argument


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result

# function with variable number of arguments


def multi_add(*args):  # taking variable number of arguments
    result = 0
    for x in args:
        result = result+x
    return result


# calling functions
func1()
print(func1())
print(func1)  # function as object
func2(10, 20)
print(func2(10, 20))
print(cube(4))
print(power(2))  # not giving value for x so default value will be taken
print(power(2, 3))  # provided value for x. so x=3 not 1.
# it works python interpreter identifies the variable with values
print(power(x=3, num=2))
print(multi_add(1, 2))
print(multi_add(1, 2, 3))
