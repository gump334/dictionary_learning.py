# Dictionary is use to map key, value pair
first_dict = {"terrell": "male", "kim": "female", "jan": "female"}
print(first_dict)

#dict comprehensions
test = {x: x**2 for x in (5, 10, 15)}
print(test)

#looping through keys
for k in first_dict.keys():
  print(k)
  if k == "kim":
    print("i found you")

#looping through keys
for v in first_dict.values():
  print(v)
  if v == "kim":
    print("i found you")

#looping in dictionary in a dictionary
users = {
  "tjackson": {
  "first": "terrell",
  "last": "jackson",
  "location": "alabama"
  },
  "djackson": {
    "first": "dionna",
    "last": "jackson",
    "location": "new york"
  },
}

for username, userinfo in users.items():
  print(f"\nUsername: {username}")
  full_name = f"{userinfo['first']} {userinfo['last']}"
  location = userinfo["location"]
  print(f"\t Full name: {full_name}.title()")
  print(f"\tLocation: {location.title()}")