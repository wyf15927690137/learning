def func1(a, b):
    print("this is func1")
    print(a + b)


def func2():
    print("this is func2")
    func1(3, 4)


def func3():
    print("this is func3")
    func2()


print("start debug")
func3()
print("debug over")
