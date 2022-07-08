str1 = 'studypython'
print(str1.find('d'))
print(str1.find('y'))

str2 = str1.title()
print(str2)

str3 = str1.upper()
print(str3)

str4 = str3.lower()
print(str4)
print('----------------------')
str5 = '    start to study python     '
str6 = str5.split(' ')  # use space as a separator
str66 = str5.strip().split(' ')

print(str6)
print(str66)
print('----------------------')
str7 = 'test1\ttest2'
str8 = 'test1\rtest2'
str9 = 'test1\ntest2'
str6 = str5.split(' ')  # use space as a separator
print(str7)
#   \r:move the cursor to the beginning of this line
print(str8)
#   \n:move the cursor to the beginning of next line
print(str9)

print('----------------------')
str10 = "\t\r\n   learn python\n  "
print(str10)
print("over")
print(str10.strip())
print("over")
