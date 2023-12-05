# list derivation
list1 = [2, 3, 4, 3]
list2 = []

for s in list1:
    list2.append(s)
print(list2)

list3 = [s * 3 for s in list2]
print(list3)
