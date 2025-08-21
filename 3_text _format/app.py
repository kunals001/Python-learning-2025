print("App for text formatting")

text = input("Enter your text here: ")
print("1. Uppercase")
print("2. Lowercase")
print("3. Titlecase")
print("4. Capitalize")

choice = int(input("Enter your choice here: "))

if choice == 1:
    print(text.upper())
elif choice == 2:
    print(text.lower())
elif choice == 3:
    print(text.title())
elif choice == 4:
    print(text.capitalize())
else:
    print("Invalid choice")