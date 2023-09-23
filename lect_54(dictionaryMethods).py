# Dictionary methords 1
# we used (.get) methord for not come error in our program or code and it will be help us to run the program if the given output not avlable in tihe code 
user = {
  "imroz":31,
  31:"roll_no",
  "age": 21,
  "M" : True,
}
print(user.get("f"))

# It is another way of impliment the dictionary but we can not used it 
user2 = dict(name = "Imroz")
print(user2)
#if we show pyflakes it mens it show error is called lynching
user2 = dict("name" = "Imroz")
print(user2)