print("Step Counter")

daily_goal = int(input("Enter your daily step goal: "))
curent_step = int(input("How many steps did you take today: "))

remaining = daily_goal - curent_step

if remaining > 0:
    print(f"You have {remaining} steps remaining today.")

else:
    print(f"you have {abs(remaining)} steps over your daily goal.")