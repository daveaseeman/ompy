me = {"name": "Dave", "age": 25}

print(me)
print("{} is {} years old".format(me["name"],me["age"]))

for key, value in me.items():
    print(key,value)
