#Dictionary keys
"""
Dictionary key needs to be immutibale it will be 
be a unique  key vlue

A key can not change

The dictionary key will be a str,bool,tupal,int,float but it not a list because it will be a mutble and it will be change

The 99% times a key fora dictionary is usually
something descriptive like a string 
"""
dictionary = {
  '123':[2,3,4],
  True : 'hello',
  #[100]: True,# It not be a key of dictionary because it will a list
  4.66:"imroz"
}
print(dictionary[4.66])