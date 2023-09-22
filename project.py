username=input("what is your username?")
pasward=input("what is your password?")

pasward_length=len(pasward)
hiden_pasward = '*' * pasward_length

print(f'{username}, your password,{hiden_pasward}, is {pasward_length}letters long')