import math

friends = 5
friends = friends + 1
#augmented assignemnt it works to different arithmetic functions
#friends +=1

friends = friends **2
#friends **=2

remainder = friends % 5

print(friends)
print(remainder)
print()

x = 9.1
y = -4
z = 5

result = round(x)
result1 = abs(y)
result2 = pow(4,3)
result3 = max(x,y,z)
result4 = min(x,y,z)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(math.pi)
print(math.e)

#you have to import math first to use this
result5 = math.sqrt(9)
result6 = math.ceil(x) #round up
result7 = math.floor(x) #round down
print(result5)
print(result6)
print(result7)

radius = float(input("Enter the Radius of a circle: "))
circumference = 2*math.pi*radius
area = math.pi*pow(radius,2)
print(f"The circumference of the circle is {round(circumference,2)}")
print(f"The area of the circle is {round(area,2)}")
