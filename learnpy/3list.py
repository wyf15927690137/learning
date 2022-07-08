l=[2,0.2,'python']
print(l[0]*l[2])

l.append('wyf')

del l[1]

print(l)

l.append('d')
l.append('d')
l.append('d')
print(l)
print(l.count('d'))

print(l.index('wyf'))
# rm the first mathed element
l.remove('d') 
print(l)

l.sort()
print(l)

t=(2,3,"lsaf")
print(t)
t=(3,2,"faf")
print(t)