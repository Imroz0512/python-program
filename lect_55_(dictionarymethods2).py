user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
# It is a way to look the item in dictionary and it is same as list we used (in) methord
print("size" in user)

#There is some dictionary method which used in dectionary

#.Key()
#It is used to simply find the key in dictionary
user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
print("name" in user.keys())

#.Value()
##It is used to simply find the value in dictionary
user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
print("Imroz" in user.values())

#.items()
user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
print(user.items())

#.clear()
user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
print(user.clear())

#.copy()
user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
print(user.copy())

#we also do as that way
user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
user2 = user.copy()
print(user.clear())
print(user2)

#.pop()
#It remove key or returns the value of the key from the dictionary
user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
print(user.pop("age"))
print(user)


#.popitems() it importent for some case
#Is used to remove the some pair or randamle pops some thing and some time it  remove the last key value
user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
print(user.popitem())
print(user)

#.update
#It will be updat the dictionary
user = {
  "baskit": [3,4,5],
  "name" : "Imroz",
  "age"  : 21,
}
print(user.update({"No" : 765203456}))
print(user)