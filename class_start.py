# Example of working with Python classes
# example of base class
class myClass():
    def method1(self):
        print("method1 function")

    def method2(self, someString):  # self is like this in javascript
        print("method2 function: hello->"+someString)


class myClass2(myClass):  # inheriting myClass, myClass2 is subclass
    def method1(self):
        myClass.method1(self)  # calling method1 of base class
        print("myClass2 method1")

    def method2(self):
        print("myClass2 method2")


def main():
    c = myClass()  # creating object of class
    c.method1()  # calling method1 using object c
    c.method2("deepika")  # calling method2
    d = myClass2()
    d.method1()
    d.method2()


main()
