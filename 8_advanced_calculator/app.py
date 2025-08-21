print("\n== Advanced Calculator ==");
print("\nWhat are you trying to do?")



def add(x,y):
    return x+y;

def sub(x,y):
    return x-y;

def div(x,y):
    if y<0 :
        print("Invalid number")
    else:
        return x/y;

def mul(x,y):
    return x*y;

def ave(x,y):
    return x+y/2;

def rem(x,y):
    if y<0:
        print("Invalid number")
    else:
        return x%2
    



def main():
    print("1. Subtraction");
    print("2. Addition");
    print("3. Divide");
    print("4. Multiply");
    print("5. Average");
    print("6. Remeinder");

    while True:
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice not in ('1', '2', '3', '4', '5','6'):
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
        print(f"Subtration is {sub(num1,num2)}")
    elif choice == '2':
        print(f"Addition is {add(num1,num2)}")
    elif choice == '3':
        print(f"Divide is {div(num1,num2)}")
    elif choice == '4':
        print(f"Multeply is {mul(num1,num2)}")
    elif choice == '5':
        print(f"Average is {ave(num1,num2)}")
    elif choice == '6':
        print(f"Reminder is {rem(num1,num2)}")
    
    again = input("Do you want to run the timer again? (y/n): ").lower()
    if not again.startswith("y"):
        print("Goodbye!")
    else :
        main()


main();



