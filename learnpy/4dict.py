l={('name','wyf'),('age',24)}
d=dict(l)

print(d.get('name'),"and",d.get('age'))

d['age']=18
print(d['age'])

x = dict(reversed(list(d.items())))
print(x)
