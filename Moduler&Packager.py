# # # import datetime

# # # class Moduler:
# # #     Date_time = "%Y-%m-%d %H:%M:%S"

# # #     def _get_timestamp(self):
# # #         return datetime.datetime.now().strftime(self.Date_time)

# # # print("====================================\n")
# # # print("Welcome to Multi-Utility Toolkit")
# # # print("====================================\n")

# # # while True:
# # #     print("Choose an option: ")
# # #     print("1. Datetime and Time Operations")
# # #     print("2. Mathematical Operations")
# # #     print("3. Random Data Generation")
# # #     print("4. Generate Unique Identifiers (UUID)")
# # #     print("5. File OPerations (Custom Module)")
# # #     print("6. Explore Module Attribtes (dir())")
# # #     print("7. Exit")

# # #     print("==========================")


# # #     choice = input("Enter your choice: ")

# # #     while True:
# # #         print("Datetime and Time Operations:")
# # #         print("1. Display current date and time")
# # #         print("Calculate difference between two dates/times")
# # #         print("3. Format date into custom fomat")
# # #         print("4. Stopwatch")
# # #         print("5. Countdown Timer")
# # #         print("6. Back to Main Menu")

# # #         choice = input("Enter your choice: ")   
        
# # #         print(f"Current Date and Time: %Y/%m/%d %h:%m:%s")

# # # ================================
# # # Multi-Utility Toolkit (Single File)
# # # ================================

# # import datetime
# # import time
# # import math
# # import random
# # import string
# # import uuid

# # # ================================
# # # Datetime & Time Functions
# # # ================================

# # def show_datetime():
# #     print("\nCurrent Date and Time:",
# #           datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# # def date_difference():
# #     d1 = input("Enter first date (YYYY-MM-DD): ")
# #     d2 = input("Enter second date (YYYY-MM-DD): ")
# #     date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
# #     date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
# #     diff = abs(date2 - date1)
# #     print("Difference:", diff.days, "days")

# # def stopwatch():
# #     input("Press Enter to start stopwatch...")
# #     start = time.time()
# #     input("Press Enter to stop...")
# #     end = time.time()
# #     print("Elapsed Time:", round(end - start, 2), "seconds")

# # def countdown():
# #     seconds = int(input("Enter countdown seconds: "))
# #     while seconds > 0:
# #         print(seconds)
# #         time.sleep(1)
# #         seconds -= 1
# #     print("Time's up!")

# # def datetime_menu():
# #     while True:
# #         print("\nDatetime and Time Operations:")
# #         print("1. Display current date and time")
# #         print("2. Calculate date difference")
# #         print("3. Stopwatch")
# #         print("4. Countdown Timer")
# #         print("5. Back")

# #         ch = input("Enter your choice: ")
# #         if ch == "1":
# #             show_datetime()
# #         elif ch == "2":
# #             date_difference()
# #         elif ch == "3":
# #             stopwatch()
# #         elif ch == "4":
# #             countdown()
# #         elif ch == "5":
# #             break
# #         else:
# #             print("Invalid choice!")

# # # ================================
# # # Mathematical Functions
# # # ================================

# # def factorial():
# #     n = int(input("Enter a number: "))
# #     print("Factorial:", math.factorial(n))

# # def compound_interest():
# #     p = float(input("Enter principal amount: "))
# #     r = float(input("Enter rate of interest (%): "))
# #     t = float(input("Enter time (years): "))
# #     amount = p * (1 + r / 100) ** t
# #     print("Compound Interest:", round(amount, 2))

# # def trigonometry():
# #     angle = float(input("Enter angle in degrees: "))
# #     rad = math.radians(angle)
# #     print("Sin:", math.sin(rad))
# #     print("Cos:", math.cos(rad))
# #     print("Tan:", math.tan(rad))

# # def area_circle():
# #     r = float(input("Enter radius: "))
# #     print("Area of Circle:", round(math.pi * r * r, 2))

# # def math_menu():
# #     while True:
# #         print("\nMathematical Operations:")
# #         print("1. Calculate Factorial")
# #         print("2. Compound Interest")
# #         print("3. Trigonometry")
# #         print("4. Area of Circle")
# #         print("5. Back")

# #         ch = input("Enter your choice: ")
# #         if ch == "1":
# #             factorial()
# #         elif ch == "2":
# #             compound_interest()
# #         elif ch == "3":
# #             trigonometry()
# #         elif ch == "4":
# #             area_circle()
# #         elif ch == "5":
# #             break
# #         else:
# #             print("Invalid choice!")

# # # ================================
# # # Random Data Functions
# # # ================================

# # def random_number():
# #     print("Random Number:", random.randint(1, 100))

# # def random_list():
# #     print("Random List:", random.sample(range(1, 50), 5))

# # def random_password():
# #     length = int(input("Enter password length: "))
# #     chars = string.ascii_letters + string.digits + "!@#$%"
# #     password = "".join(random.choice(chars) for _ in range(length))
# #     print("Generated Password:", password)

# # def random_otp():
# #     print("Generated OTP:", random.randint(100000, 999999))

# # def random_menu():
# #     while True:
# #         print("\nRandom Data Generation:")
# #         print("1. Generate Random Number")
# #         print("2. Generate Random List")
# #         print("3. Create Random Password")
# #         print("4. Generate OTP")
# #         print("5. Back")

# #         ch = input("Enter your choice: ")
# #         if ch == "1":
# #             random_number()
# #         elif ch == "2":
# #             random_list()
# #         elif ch == "3":
# #             random_password()
# #         elif ch == "4":
# #             random_otp()
# #         elif ch == "5":
# #             break
# #         else:
# #             print("Invalid choice!")

# # # ================================
# # # UUID Function
# # # ================================

# # def generate_uuid():
# #     print("Generated UUID:", uuid.uuid4())

# # # ================================
# # # File Operations
# # # ================================

# # def create_file():
# #     name = input("Enter file name: ")
# #     open(name, "w").close()
# #     print("File created successfully!")

# # def write_file():
# #     name = input("Enter file name: ")
# #     data = input("Enter data: ")
# #     with open(name, "w") as f:
# #         f.write(data)
# #     print("Data written successfully!")

# # def read_file():
# #     name = input("Enter file name: ")
# #     with open(name, "r") as f:
# #         print("\nFile Content:")
# #         print(f.read())

# # def append_file():
# #     name = input("Enter file name: ")
# #     data = input("Enter data to append: ")
# #     with open(name, "a") as f:
# #         f.write("\n" + data)
# #     print("Data appended successfully!")

# # def file_menu():
# #     while True:
# #         print("\nFile Operations:")
# #         print("1. Create File")
# #         print("2. Write File")
# #         print("3. Read File")
# #         print("4. Append File")
# #         print("5. Back")

# #         ch = input("Enter your choice: ")
# #         if ch == "1":
# #             create_file()
# #         elif ch == "2":
# #             write_file()
# #         elif ch == "3":
# #             read_file()
# #         elif ch == "4":
# #             append_file()
# #         elif ch == "5":
# #             break
# #         else:
# #             print("Invalid choice!")

# # # ================================
# # # dir() Exploration
# # # ================================

# # def explore_module():
# #     name = input("Enter module name to explore: ")
# #     try:
# #         module = __import__(name)
# #         print("\nAvailable attributes:")
# #         print(dir(module))
# #     except ImportError:
# #         print("Module not found!")

# # # ================================
# # # Main Menu
# # # ================================

# # def main():
# #     while True:
# #         print("\n==============================")
# #         print("Welcome to Multi-Utility Toolkit")
# #         print("==============================")
# #         print("1. Datetime and Time Operations")
# #         print("2. Mathematical Operations")
# #         print("3. Random Data Generation")
# #         print("4. Generate Unique Identifiers (UUID)")
# #         print("5. File Operations")
# #         print("6. Explore Module Attributes (dir())")
# #         print("7. Exit")

# #         choice = input("Enter your choice: ")

# #         if choice == "1":
# #             datetime_menu()
# #         elif choice == "2":
# #             math_menu()
# #         elif choice == "3":
# #             random_menu()
# #         elif choice == "4":
# #             generate_uuid()
# #         elif choice == "5":
# #             file_menu()
# #         elif choice == "6":
# #             explore_module()
# #         elif choice == "7":
# #             print("\nThank you for using the Multi-Utility Toolkit!")
# #             break
# #         else:
# #             print("Invalid choice!")

# # # ================================
# # # Program Entry Point
# # # ================================

# # if __name__ == "__main__":
# #     main()



# import datetime
# import time
# import math
# import random
# import string
# import uuid

# # ================================
# # Datetime & Time Functions
# # ================================

# def show_datetime():
#     print("\nCurrent Date and Time:",
#           datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# def date_difference():
#     d1 = input("Enter the first date (YYYY-MM-DD): ")
#     d2 = input("Enter the second date (YYYY-MM-DD): ")
#     date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
#     date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
#     diff = abs(date2 - date1)
#     print("Difference:", diff.days, "days")

# def stopwatch():
#     input("Press Enter to start stopwatch...")
#     start = time.time()
#     input("Press Enter to stop...")
#     end = time.time()
#     print("Elapsed Time:", round(end - start, 2), "seconds")

# def countdown():
#     sec = int(input("Enter countdown seconds: "))
#     while sec > 0:
#         print(sec)
#         time.sleep(1)
#         sec -= 1
#     print("Time's up!")

# def datetime_menu():
#     while True:
#         print("\nDatetime and Time Operations:")
#         print("1. Display current date and time")
#         print("2. Calculate difference between two dates")
#         print("3. Stopwatch")
#         print("4. Countdown Timer")
#         print("5. Back to Main Menu")

#         ch = input("Enter your choice: ")
#         if ch == "1":
#             show_datetime()
#         elif ch == "2":
#             date_difference()
#         elif ch == "3":
#             stopwatch()
#         elif ch == "4":
#             countdown()
#         elif ch == "5":
#             break
#         else:
#             print("Invalid choice!")

# # ================================
# # Mathematical Functions
# # ================================

# def factorial():
#     n = int(input("Enter a number: "))
#     print("Factorial:", math.factorial(n))

# def compound_interest():
#     p = float(input("Enter principal amount: "))
#     r = float(input("Enter rate of interest (in %): "))
#     t = float(input("Enter time (in years): "))
#     amount = p * (1 + r / 100) ** t
#     print("Compound Interest:", round(amount, 2))

# def trigonometry():
#     angle = float(input("Enter angle in degrees: "))
#     rad = math.radians(angle)
#     print("Sin:", math.sin(rad))
#     print("Cos:", math.cos(rad))
#     print("Tan:", math.tan(rad))

# def area_circle():
#     r = float(input("Enter radius: "))
#     print("Area of Circle:", round(math.pi * r * r, 2))

# def math_menu():
#     while True:
#         print("\nMathematical Operations:")
#         print("1. Calculate Factorial")
#         print("2. Solve Compound Interest")
#         print("3. Trigonometric Calculations")
#         print("4. Area of Circle")
#         print("5. Back to Main Menu")

#         ch = input("Enter your choice: ")
#         if ch == "1":
#             factorial()
#         elif ch == "2":
#             compound_interest()
#         elif ch == "3":
#             trigonometry()
#         elif ch == "4":
#             area_circle()
#         elif ch == "5":
#             break
#         else:
#             print("Invalid choice!")

# # ================================
# # Random Data Functions
# # ================================

# def random_number():
#     print("Random Number:", random.randint(1, 100))

# def random_list():
#     print("Random List:", random.sample(range(1, 50), 5))

# def random_password():
#     length = int(input("Enter password length: "))
#     chars = string.ascii_letters + string.digits + "!@#$%"
#     pwd = "".join(random.choice(chars) for _ in range(length))
#     print("Generated Password:", pwd)

# def random_otp():
#     print("Generated OTP:", random.randint(100000, 999999))

# def random_menu():
#     while True:
#         print("\nRandom Data Generation:")
#         print("1. Generate Random Number")
#         print("2. Generate Random List")
#         print("3. Create Random Password")
#         print("4. Generate Random OTP")
#         print("5. Back to Main Menu")

#         ch = input("Enter your choice: ")
#         if ch == "1":
#             random_number()
#         elif ch == "2":
#             random_list()
#         elif ch == "3":
#             random_password()
#         elif ch == "4":
#             random_otp()
#         elif ch == "5":
#             break
#         else:
#             print("Invalid choice!")

# # ================================
# # UUID
# # ================================

# def generate_uuid():
#     print("Generated UUID:", uuid.uuid4())

# # ================================
# # File Operations
# # ================================

# def create_file():
#     name = input("Enter file name: ")
#     open(name, "w").close()
#     print("File created successfully!")

# def write_file():
#     name = input("Enter file name: ")
#     data = input("Enter data to write: ")
#     with open(name, "w") as f:
#         f.write(data)
#     print("Data written successfully!")

# def read_file():
#     name = input("Enter file name: ")
#     with open(name, "r") as f:
#         print("\nFile Content:")
#         print(f.read())

# def append_file():
#     name = input("Enter file name: ")
#     data = input("Enter data to append: ")
#     with open(name, "a") as f:
#         f.write("\n" + data)
#     print("Data appended successfully!")

# def file_menu():
#     while True:
#         print("\nFile Operations:")
#         print("1. Create a new file")
#         print("2. Write to a file")
#         print("3. Read from a file")
#         print("4. Append to a file")
#         print("5. Back to Main Menu")

#         ch = input("Enter your choice: ")
#         if ch == "1":
#             create_file()
#         elif ch == "2":
#             write_file()
#         elif ch == "3":
#             read_file()
#         elif ch == "4":
#             append_file()
#         elif ch == "5":
#             break
#         else:
#             print("Invalid choice!")

# # ================================
# # dir() Exploration
# # ================================

# def explore_module():
#     name = input("Enter module name to explore: ")
#     try:
#         module = __import__(name)
#         print("Available Attributes:")
#         print(dir(module))
#     except ImportError:
#         print("Module not found!")

# # ================================
# # Main Menu
# # ================================

# def main():
#     while True:
#         print("\n==============================")
#         print("Welcome to Multi-Utility Toolkit")
#         print("==============================")
#         print("1. Datetime and Time Operations")
#         print("2. Mathematical Operations")
#         print("3. Random Data Generation")
#         print("4. Generate Unique Identifiers (UUID)")
#         print("5. File Operations")
#         print("6. Explore Module Attributes (dir())")
#         print("7. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             datetime_menu()
#         elif choice == "2":
#             math_menu()
#         elif choice == "3":
#             random_menu()
#         elif choice == "4":
#             generate_uuid()
#         elif choice == "5":
#             file_menu()
#         elif choice == "6":
#             explore_module()
#         elif choice == "7":
#             print("\nThank you for using the Multi-Utility Toolkit!")
#             break
#         else:
#             print("Invalid choice!")

# # ================================
# # Program Entry Point
# # ================================

# if __name__ == "__main__":
#     main()




#!/usr/bin/env python3
"""
Multi-Utility Toolkit
A Python-based toolkit that integrates multiple standard modules, custom modules, 
and packages to perform a variety of tasks.
"""

import sys
import time
import datetime
import math
import random
import uuid
import string

def display_main_menu():
    """Display the main menu options"""
    print("\n" + "="*40)
    print("Welcome to Multi-Utility Toolkit")
    print("="*40)
    print("Menu:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("="*40)

def datetime_menu():
    """Display datetime operations menu"""
    while True:
        print("\n" + "="*40)
        print("Datetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        print("="*40)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(f"Current Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        elif choice == "2":
            date1 = input("Enter the first date (YYYY-MM-DD): ")
            date2 = input("Enter the second date (YYYY-MM-DD): ")
            try:
                d1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
                d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
                difference = abs((d2 - d1).days)
                print(f"Difference: {difference} days")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
        elif choice == "3":
            date_str = input("Enter date (YYYY-MM-DD): ")
            try:
                date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                print("Available formats:")
                print("1. %Y-%m-%d (2025-01-04)")
                print("2. %d/%m/%Y (04/01/2025)")
                print("3. %B %d, %Y (January 04, 2025)")
                print("4. %A, %B %d, %Y (Saturday, January 04, 2025)")
                
                choice = input("Enter format choice: ")
                formats = {
                    "1": "%Y-%m-%d",
                    "2": "%d/%m/%Y", 
                    "3": "%B %d, %Y",
                    "4": "%A, %B %d, %Y"
                }
                
                if choice in formats:
                    formatted_date = date_obj.strftime(formats[choice])
                    print(f"Formatted Date: {formatted_date}")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
        elif choice == "4":
            print("Stopwatch started. Press Enter to stop.")
            input()  # Wait for user to press Enter
            elapsed = time.time()
            print(f"Elapsed time: {elapsed:.2f} seconds")
        elif choice == "5":
            try:
                seconds = int(input("Enter countdown time in seconds: "))
                print(f"Countdown started for {seconds} seconds...")
                
                for remaining in range(seconds, 0, -1):
                    print(f"{remaining} seconds remaining", end='\r')
                    time.sleep(1)
                
                print("\nTime's up!")
            except ValueError:
                print("Please enter a valid number of seconds.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def math_menu():
    """Display mathematical operations menu"""
    while True:
        print("\n" + "="*40)
        print("Mathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        print("="*40)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                num = int(input("Enter a number: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    result = math.factorial(num)
                    print(f"Factorial: {result}")
            except ValueError:
                print("Please enter a valid integer.")
        elif choice == "2":
            try:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter rate of interest (in %): "))
                time_years = float(input("Enter time (in years): "))
                
                amount = principal * (1 + rate/100) ** time_years
                interest = amount - principal
                
                print(f"Compound Interest: {interest:.2f}")
                print(f"Total Amount: {amount:.2f}")
            except ValueError:
                print("Please enter valid numbers.")
        elif choice == "3":
            print("Trigonometric Calculations:")
            print("1. Sine")
            print("2. Cosine") 
            print("3. Tangent")
            
            choice = input("Enter your choice: ")
            angle_deg = float(input("Enter angle in degrees: "))
            angle_rad = math.radians(angle_deg)
            
            if choice == "1":
                print(f"Sine({angle_deg}°): {math.sin(angle_rad):.4f}")
            elif choice == "2":
                print(f"Cosine({angle_deg}°): {math.cos(angle_rad):.4f}")
            elif choice == "3":
                print(f"Tangent({angle_deg}°): {math.tan(angle_rad):.4f}")
            else:
                print("Invalid choice.")
        elif choice == "4":
            print("Area of Geometric Shapes:")
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                radius = float(input("Enter radius: "))
                area = math.pi * radius ** 2
                print(f"Area of Circle: {area:.2f}")
            elif choice == "2":
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = length * width
                print(f"Area of Rectangle: {area:.2f}")
            elif choice == "3":
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = 0.5 * base * height
                print(f"Area of Triangle: {area:.2f}")
            else:
                print("Invalid choice.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def random_menu():
    """Display random data generation menu"""
    while True:
        print("\n" + "="*40)
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        print("="*40)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            try:
                min_val = int(input("Enter minimum value: "))
                max_val = int(input("Enter maximum value: "))
                random_num = random.randint(min_val, max_val)
                print(f"Random Number: {random_num}")
            except ValueError:
                print("Please enter valid integers.")
        elif choice == "2":
            try:
                length = int(input("Enter list length: "))
                min_val = int(input("Enter minimum value: "))
                max_val = int(input("Enter maximum value: "))
                
                random_list = [random.randint(min_val, max_val) for _ in range(length)]
                print(f"Random List: {random_list}")
            except ValueError:
                print("Please enter valid integers.")
        elif choice == "3":
            length = int(input("Enter password length: "))
            
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            
            print(f"Generated Password: {password}")
        elif choice == "4":
            otp = ''.join(random.choice(string.digits) for _ in range(6))
            print(f"Generated OTP: {otp}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def uuid_menu():
    """Display UUID generation menu"""
    while True:
        print("\n" + "="*40)
        print("Generate Unique Identifiers (UUID):")
        print("1. Generate UUID")
        print("2. Back to Main Menu")
        print("="*40)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            unique_id = uuid.uuid4()
            print(f"Generated UUID: {unique_id}")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

def file_operations_menu():
    """Display file operations menu"""
    while True:
        print("\n" + "="*40)
        print("File Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        print("="*40)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            filename = input("Enter file name: ")
            try:
                with open(filename, 'w') as f:
                    pass
                print(f"File created successfully!")
            except Exception as e:
                print(f"Error creating file: {e}")
        elif choice == "2":
            filename = input("Enter file name: ")
            data = input("Enter data to write: ")
            try:
                with open(filename, 'w') as f:
                    f.write(data)
                print(f"Data written successfully!")
            except Exception as e:
                print(f"Error writing to file: {e}")
        elif choice == "3":
            filename = input("Enter file name: ")
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                print(f"File Content:\n{content}")
            except FileNotFoundError:
                print(f"File not found: {filename}")
            except Exception as e:
                print(f"Error reading file: {e}")
        elif choice == "4":
            filename = input("Enter file name: ")
            data = input("Enter data to append: ")
            try:
                with open(filename, 'a') as f:
                    f.write(data + '\n')
                print(f"Data appended successfully!")
            except Exception as e:
                print(f"Error appending to file: {e}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def explore_module_attributes():
    """Allow users to explore module attributes using dir()"""
    while True:
        print("\n" + "="*40)
        print("Explore Module Attributes:")
        print("Available modules: datetime, time, math, random, uuid")
        print("Enter 'back' to return to main menu")
        print("="*40)
        
        module_name = input("Enter module name to explore: ").lower()
        
        if module_name == "back":
            break
        elif module_name in ["datetime", "time", "math", "random", "uuid"]:
            try:
                module = __import__(module_name)
                attributes = dir(module)
                print(f"\nAvailable Attributes in {module_name} module:")
                print(attributes)
            except ImportError:
                print(f"Module {module_name} not found.")
        else:
            print("Invalid module name. Please try again.")

def main():
    """Main function to run the toolkit"""
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_operations_menu()
        elif choice == "6":
            explore_module_attributes()
        elif choice == "7":
            print("\n" + "="*40)
            print("Thank you for using the Multi-Utility Toolkit!")
            print("="*40)
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()