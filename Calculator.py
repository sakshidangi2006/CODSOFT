def calculator():
    print("___Simple Python Calculator___")
    print("Select an operation: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit (e)")

    try:
        while(True):

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            choice = input("Enter the operation (1/2/3/4/5) or the symbol (+,-,*,/,e): ")

            if choice in ('1','+'):
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")

            elif choice in ('2','-'):
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")

            elif choice in ('3','*'):
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")

            elif choice in ('4','/'):
                if num2 != 0:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
                else:
                    print("Error: Division by zero is not allowed!")

            elif choice in ('5','e'):
                print("Thank you for using our calculator.")
                break

            else :
                print("Invalid input. Please select a valid operation")

    except ValueError:
        print("Error: Please enter numeric values for the numbers.")

if __name__ == "__main__":
    calculator()