
# Declare a variable and initialize
f = 0
print(f)

# Redeclaring a variable works
f = 'abc'
print(f)

# Error as different data type
# print('hello'+123)  #Not allowed

# Global variable
f1 = 10

# Local variable


def somefunction():
    f1 = 123
    print(f1)


somefunction()
