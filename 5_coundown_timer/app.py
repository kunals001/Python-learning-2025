print("\nCountdown Timer")

while True:
    seconds = int(input("Enter the number of seconds: "))

    if seconds < 0:
        print("Invalid input. Please enter a positive number.")
        continue

    for i in range(seconds, 0, -1):
        print(f"{i} seconds remaining...")
        import time
        time.sleep(1)

    print("Time's up!")

    again = input("Do you want to run the timer again? (yes/no): ").lower()
    if not again.startswith("y"):
        print("Goodbye!")
        break
