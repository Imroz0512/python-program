#tuple
my_tuple = (1,3,4,6,8,2)
print(my_tuple[3])

# or we can find the value exest in my tuple

print(4 in my_tuple)

#we can used tuple as a car booking system like ubar for a user pickup or drop location of user becaus longitudnal or letiludnal loction not be change

#we can creat a new tuple everytime when a user requst a new pickup or drop location 

# we also used tuple as a dictionary key becaus it as immutable
user = {
  (1,2) : [1,4,6],
  "age" : 32,
  "hi" : "imroz",
}
print(user[(1,2)])

# we also do in this way 
user = {
  (1,2) : [1,4,6],
  "hi" : "imroz",
  "age" : 32,
}
print(user[(1,2)])