# Object Oriented Programing Example
class MyClass:
    def __init__(self, param1, param2) -> None:
        self.param1 = param1
        self.param2 = param2

    def MyClassMethod1(self):
        # perform some action
        print(self.param1)

    def MyClassMethod2(self):
        # perform some action
        print(self.param2)


# Create new instance of Class
Myobjectclass = MyClass(10, 20)
Myobjectclass.MyClassMethod1()


class Sample():

    def_name = 'amin'
    def_age = '39'

    def __init__(self, name='amin',age=39):
        self.def_name = name
        self.def_age = age
    
    def method_print_All(self):
        print('Name :',self.def_name,' Age :',self.def_age)

MyClass1 = Sample()
MyClass1.method_print_All()

MyClass2 = Sample('Ali',40)
MyClass2.method_print_All()
