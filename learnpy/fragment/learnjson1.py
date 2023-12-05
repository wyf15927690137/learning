import json

print("-----------")
test_dict = {'one':1, 'two':{2.1:['a', 'b']}}
print(test_dict)
print(type(test_dict))
#dumps : change data of any type to string
json_str = json.dumps(test_dict)
print(json_str)
print(type(json_str))

# loads: parse json data
new_dict = json.loads(json_str)
print(new_dict)
print(type(new_dict))
