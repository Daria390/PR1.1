import math_func
import pyramid_func

while True:
    print("Main menu:")
    print("1. Calculate X")
    print("2. Build pyramid")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print()
        print("Enter values (from 1 to 100):")
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))

            if 1 <= a <= 100 and 1 <= b <= 100:
                result = math_func.calculate_x(a, b)
                print("Result X =", result)
            else:
                print("Error: numbers must be from 1 to 100!")
        except ValueError:
            print("Error: you must enter a number!")
        print()

    elif choice == "2":
        print()
        try:
            n = int(input("Enter integer N (from 1 to 10): "))

            if 1 <= n <= 10:
                print()
                pyramid_func.draw_pyramid(n)
            else:
                print("Error: number must be from 1 to 10!")
        except ValueError:
            print("Error: you must enter an integer!")
        print()

    elif choice == "0":
        break

    else:
        print("Invalid option, try again.")
        print()