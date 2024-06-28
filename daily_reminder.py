task= str(input("Enter your task:"))
choice= str(input("Priority (high/medium/low):"))
bound= str(input("Is it time-bound?"))
if choice == "high" and bound == "yes":
    print("'Finish project report' is a high priority task that requires immediate attention today!")
elif choice == "low" and bound =="no":
    print("Read a book' is a low priority task. Consider completing it when you have free time")
else:
    print("pleas try again")