# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))

# if a==b and b==c:
#     print("All are same")
# else:
#     if a>b:
#         if a>c:
#             print("a is max")
#         else:
#             print("c is max")
    
#     else:
#         if b>c:
#             print("b is max")
#         else:
#             print("c is max")

# wap to create a Fast food Order Cafe.

while True:
    print("Press 1 for Sandwich 🥪")
    print("Press 2 for Pizza 🍕")
    print("Press 3 for Burger 🍔")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("="*22)
            print("You ordered a 🥪 Sandwich")
            print("="*22)

        case 2:
            print("Press 1 for Fresh Dough Pizza 🍕")
            print("Press 2 for Thin Crust Pizza 🍕")
            print("Press 3 for Cheese Burst Pizza 🍕")
            type = int(input("Enter your Pizza type: "))

            match type:
                case 1:
                    print("="*22)
                    print("You ordered a Fresh Dough Pizza 🍕")
                    print("="*22)

                case 2:
                    print("="*22)
                    print("You ordered a Thin Crust Pizza 🍕")
                    print("="*22)

                case 3:
                    print("="*22)
                    print("You ordered a Cheese Burst Pizza 🍕")
                    print("="*22)

                case _:
                    print("Invalid Pizza Type....")

        case 3:
            print("="*22)
            print("You ordered a Burger 🍔")
            print("="*22)

        case 0:
            break
        case _:
            print("Invalid Choice....")