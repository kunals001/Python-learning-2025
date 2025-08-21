print("Character checker")

text = input("Enter your text here: ")

if text.isalpha():
    print("This is a string")

elif text.isdigit():
    print("This is a number")

else:
    print("This is a special character")