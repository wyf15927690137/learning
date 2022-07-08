fun1 = lambda x: x ** 2
print(fun1(4))

list1 = [lambda a: a ** 3, lambda b: b * 5]
print(list1[0](5))
print(list1[1](6))

my_list = [(1, 2), (3, 1), (4, 0), (11, 4)]
my_list.sort(key=lambda x: x[1])
print(my_list)