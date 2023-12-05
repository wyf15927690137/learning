import pandas as pd

# dataframe
# pandas.DataFrame( data, index, columns, dtype, copy)
data = [['Google',10],['Runoob',12],['Wiki',13]]
df = pd.DataFrame(data,columns=['Site','Age'],dtype=float)
print(df)

data1 = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
df1 = pd.DataFrame(data1,dtype=int)
print (df1)
print("the first row:")
print(df1.loc[0])
print("the second row:")
print(df1.loc[1])

data2 = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df2 = pd.DataFrame(data2)
print (df2)