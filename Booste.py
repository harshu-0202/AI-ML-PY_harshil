print("Welcome to the Interactive Personal Data Collector")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("Thank you! Here is the information we collected: ")

print("name:" , name , "type:" , type(name) , "Memory Address:" , id(name))
print("age:" , age , "type:" , type(age) , "Memory Address:" , id(age))
print("height:" , height , "type:" , type(height) , "Memory Address:" , id(height))
print("Favourite Number:" , fav_number , "type:" , type(fav_number) , "Memory Address:" , id(fav_number))

birth_year = 2025 - age
print("Your birth year is approximately:" , birth_year)

print("Thank you for using the personal Data Collector. Goodbye")