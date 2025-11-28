print("Welcome to the Data Analyzer and Transformer Program")

while True:
    print(" Main Menu: ")
    print("1. Input Data")
    print("2. Disply Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = int(input("Enter your choice [1 to 7]:"))

    if choice == 1:

        array_input = input(" Enter data for a 1D array (seperated by spaces) : \n")
        arr = list(map(int , array_input.split()))

        print("Data has been stored successfully!!")
        print("")

    elif choice == 2:

        print("\nData Summary: ")
        print("- Total element :" , len(arr))
        print("- Minimum value :" , min(arr))
        print("- Maximum value :" , max(arr))
        print("- Sum of all value :" , sum(arr))
        print("- Average value :" , sum(arr) / len(arr))
        print("")

    elif choice == 3:

        fact = int(input("Enter a number to Calculate its factorial :"))
        def factorial(fact):
            if fact == 1:
                return 1
            else : 
                return fact * factorial(fact-1)
        print(f"Factorial of {fact} is : ", factorial(fact))
        print("")

    elif choice == 4:

        num = int(input("\nEnter a threshold value to filter out data below this value:\n"))
        filtered_data = list(filter(lambda x: x >= num, arr))
        print(f"Filtered Data (values >= {num}):")
        print(*filtered_data, sep=", ")

        print("")  


    elif choice == 5:

        print("Choose sorting option :")
        print("1. Ascending")
        print("2. Descending")

        num = int(input("Enter your choice : "))
        
        if num == 1:
            sorted_arr  = sorted(arr)
            print("Sorted data in Ascending order :" , sorted_arr)
            print("")

        elif num == 2:
            sorted_arr = sorted(arr , reverse = True)
            print("sort by descending order :" , sorted_arr)
            print("")

        else:
            print("Invalid choice! Please Enter right choice [ 1 - 2 ]!!!")
            print("")

    elif choice == 6:

        print("Dataset Statistics :")

        print("- Minimum value :" , min(arr))
        print("- Maximum value :" , max(arr))
        print("- Sum of all value :" , sum(arr))
        print("- Average value : " , sum(arr) / len(arr))
        print("")

    elif choice == 7:
        print("\nThank you for usingthe Data Analyzer and Transformer Program. Goodbye!!")
        print("")
        break
