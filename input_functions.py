#input functions
user_name = input("What's your name ?: ")
age = input("How old are you?: ")

age = int(age) #typecasting to use the next line
age = age+1

print(f"You are {age} years old. ")
print(f"Hello {user_name}")
print()

#Exercise 1 Rectangle Area Calc
length = float(input("Enter the Desired Lenght: "))
width = float(input("Enter the Desired Width: "))

area = length * width

print(f"The Total Area is {area}cm²")
print()

#Exercise 2 Shopping Cart
item = input("What would you like to buy?: ")
price = float(input("How much is it?: "))
quantity = int(input("How many would you like?: "))
total = quantity * price

print(f"You bought {quantity} X {item}/s")
print(f"Total: ${total}")

