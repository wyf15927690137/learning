import pandas as pd

# pandas version
print(pd.__version__)

# pandas series
# the index begin from 0
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)

print("the third num in this serie: %d" %myvar[2])

# set index for a serie
a = ["Google", "Runoob", "Wiki"]
myvar1 = pd.Series(a, index = ["x", "y", "z"])
print(myvar1)
print(myvar1["y"])

# use key-value to create serie
sites = {"a": "Google", "b": "Runoob", "c": "Wiki"}
myvar2 = pd.Series(sites)
print(myvar2)

# specify index
myvar3 = pd.Series(sites, index = ["a", "c"])
print(myvar3)