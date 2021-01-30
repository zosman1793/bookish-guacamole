print("hello world")
you= input("Put a number in ")
try:
    you = int(you)
except: 
    raise Exception ("Wrong type of input")
if  you == ValueError:
    print("wrong type of input")
if you < 10:
    print("your number is lower then 10")
if you > 10:
    print("your number is too high")
else:
    print("please put in a number next time")
