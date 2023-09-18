# name = input("What is your name? ")
# if name == "Angel":
#     print("Hello " + name)
# elif name == "Silvia":
#     print("Hi " + name)
#     print("How are you today?")
# else:
#     print("Hello, " + name + '.' + " You are not Angel!")
#     print("Please call Angel")
# print("Have a nice day!")

####______________________________________________________
firstnum = input("Please enter a number: ")
firstnum = int(firstnum) # firstnum = int(float(firstnum))
secondnum = input("Please enter another number: ")
secondnum = int(secondnum)
if firstnum > secondnum:
    print("Your first number is bigger")
elif firstnum < secondnum:
    print("Your second number is bigger")
else:
    print("Your numbers are equal")