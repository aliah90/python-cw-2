# write your code here
my_name=input('your name')
my_age=input('your age')
print(f"My name is {my_name} and I am {my_age} years old")

first_number=2
second_number=4
operation=input()
if "+" in operation:
    print(first_number + second_number)
elif "-" in operation :
    print(first_number - second_number)
elif "*" in operation :
    print(first_number * second_number)
elif "/" in operation:
    print(first_number / second_number)
else:
    print("the operation is not valid")

num=eval(input("enter number between 1 and 12"))
noun=input('plural')
name=input("enter your name")
statment=input("write your statment")
verb=input('verb')
print(f'it was {num} am when my {noun} is arrive and my name {name} was on it , {statment} and it is {verb} ')