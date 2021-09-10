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