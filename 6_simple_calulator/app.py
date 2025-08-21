def add(x,y):
    return x+y;

def subtract(x,y):
    return x-y;

def multiply(x,y):
    return x*y;

def divide(x,y):
    if y == 0:
        return "Cannot divide by zero"
    return x/y;

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input")
        else:
            break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input")
        return

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    again = input("Do you want to run the timer again? (y/n): ").lower()
    if not again.startswith("y"):
        print("Goodbye!")
    else :
        main()

        


main()
    