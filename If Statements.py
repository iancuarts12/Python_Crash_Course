#Condition statements

age = int(input("Enter Your Age: "))

if age > 100:
    print("You are Too Old to Create an Account")
elif age < 0:
    print("You haven't been born yet.")
elif age >18:
    print("You are Qualified to Create an Account")
else:
    print("You are Too Young to Create and Account.")

response = input("Would you like some food?: ")

if response == "Y":
    print("Have some.")
else:
    print("No Food for You then.")