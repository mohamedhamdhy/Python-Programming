user = {
    "name": "Ram",
    "age": 25,
    "isMarried": True
}
print(user)
print(type(user))
print(user["name"])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())
for x in user:
    print(x," ",user[x])
for x in user.values():
    print(x)
for x in user.keys():
    print(x)
for x,y in user.items():
    print(x,y)
if "gender" in user:
    print("Present")
# Changing Values
user.update({"gender":"male"})
print(user)
user["age"]=35
print(user)
user.pop("age")
print(user)
user.clear()
print(user)
users={
    "user1": {
        "name": "Ram",
        "age": 25,
        "isMarried": True
    },
"user2": {
        "name": "SAm",
        "age": 35,
        "isMarried": False
    }
}
print(users)
for user in users:
    print(user["name"])