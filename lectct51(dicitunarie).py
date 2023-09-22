#dicitnurie
dictionary = {
  'a':3,
  'c':5,
  'd':7,
}
print(dictionary['c'])

#same as we do diffrent data type
dictionary = {
  'a':[2,4,6],
  'c':'imroz',
  'd':True,
}
print(dictionary['a'][2])

#same we do for list
my_list = [
   {
  'a':[2,4,6],
  'c':'imroz',
  'd':True,
},
 {
  'a':[2,4,6],
  'c':'imroz',
  'd':True,
}
]
print(my_list[0]['a'])
print(dictionary['a'][2])