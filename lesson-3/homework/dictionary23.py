dict1 = {"id": 1, "name": "Ali", "age": 20}
dict2 = {"name": "Laylo", "grade": "A", "age": 22}


keys1 = set(dict1.keys())
keys2 = set(dict2.keys())


common_keys = keys1.intersection(keys2)

print(bool(common_keys)) 