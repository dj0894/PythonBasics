# example of if else
def main():
    x = 10
    y = 11
    output = ""

    if(x < y):
        output = "x is smaller"
    elif(x > y):
        output = "x is greater"
    else:
        output = "equal"
    print(output)


main()

# conditional statement similar to ternary operators
x1 = 100
y1 = 101
st = "x is less than y" if(x1 < y1) else "x is greater"
