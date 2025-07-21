class a():
    def func1(self):
        print('func1')
    def func2(self):
        print('func2')
class b(a):
    def func3(self):
        print('func3')
    def func4(self):
        print('func4')
class c(b):
    def func5(self):
        print('func5')
a1=a()
a1.func2()
a1.func1()
b1=b()
b1.func3()
c1=c()
c1.func5()
