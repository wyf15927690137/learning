def IfContain(s1,s2):
    print(s1.upper())
    print(s2.upper())

    if s1.upper() in s2.upper():
        print("yes")
    else:
        print("no")

    return
s1= "sww"
s2= "TTTsssWWWf"
IfContain(s1,s2)