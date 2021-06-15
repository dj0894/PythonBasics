# Example of loops in python

def main():
    x = 0
# while loop
    print("Executing while loop")
    while(x < 5):
        print(x)
        x = x+1

# for loop
    print("Executing for loop")
    for x in range(5, 10):
        print(x)
# for loop over collection
    print("Executing or loop over collection")
    days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
    for d in days:
        print(d)
# use the break and continue statements
    print("Executing break and continue")
    for y in range(5, 10):
        if(y == 7):
            break
        print(y)
    for z in range(11, 15):
        if(z == 12):
            continue
        print(z)


# using the enumerate() function to get index
print("Executing enumerate() function to print index as well as value in counter")
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
for i, d in enumerate(days):
    print(i, d)

main()
