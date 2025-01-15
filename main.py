#this is the first step in the tutorial
print("Hello, I love Pizza")
print("I know right? It's really good.")

#variables are used as container for values

#strings mostly texts
first_name = "Adrian"
last_name = "Cuarteros"
food = "Buttered Shirmp"

print(f"Hello {first_name}")
print(f"You like {food} right?")

#Integers mostly filled with numbers
age = 25
quantity = 3

print(f"You are {age} years old")
print(f"You are buying {quantity} of items.")

#float are commonly used for decimals
price = 10.99
gpa = 1.325
print(f"The price is ${price}")
print(f"Your GPA is around {gpa}")

#booleans contains moslty true or false
is_student = True

if is_student:
    print("You are a Student.")
else:
    print("You are not a Student.")

#to check the type of variable
print(type(first_name))

#to convert gpa to a integer from 1.325 to 1
gpa = int(gpa)
print(gpa)

#if string function was turned into bool it will show true if there is something inside ""
name = bool(first_name)
print(name)

