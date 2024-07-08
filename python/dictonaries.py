dict1 = {"name":"Prajwal","age":23,"city":"Mumbai"}

print(dict1)

my_dict = dict(name="Harvey",age=40,city="NewYork")
print(my_dict)

print(my_dict["name"])
print(dict1["city"])

my_dict["email"] = "harvey234@gmail.com"
print(my_dict)

del my_dict["age"]
print(my_dict)
dict1.pop("age")
print(dict1)

if "name" in my_dict:
    print(my_dict["name"])

try:
    print(my_dict["name"])
except:
    print("error")

for key in my_dict:
    print(key)


for key in my_dict.keys():
    print(key)

for v in my_dict.values():
    print(v)

for k,v in my_dict.items():
    print(k,":",v)


mydict_cpy = dict(my_dict)
print(mydict_cpy)
mydict_cpy["Role"]="Developer"
print(mydict_cpy)
print(my_dict)


dict2 = {"name":"Max","age":27,"email":"max3491@gmail.com"}
dict3 = dict(name="Mike",age=30,city="Newyork")

dict2.update(dict3)
print(dict2)


dict4 = {3:9,4:16,9:81,10:100}

print(dict4)
print(dict4[10])

my_tup = (9,97)
mydict = {my_tup:108}
print(mydict)

# tuples are possible but list is not.
