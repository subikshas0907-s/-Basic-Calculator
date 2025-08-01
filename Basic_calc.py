def calculator():
    print("Basic Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            choice = input("Enter operation (1/2/3/4/5): ")
            
            if choice == '5':
                print("Exiting calculator. Goodbye!")
                break
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Invalid input! Please try again.")
        
        except ValueError:
            print("Error: Please enter valid numbers!")

# Run the calculator
calculator()
