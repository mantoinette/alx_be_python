Task= str(input("Enter your task:"))
Priority= str(input(" (high/medium/low):"))
Time_Bound= str(input("Is it time-bound?"))
if Priority == "high" and Time_Bound == "yes":
    print("'Finish project report' is a high priority task that requires immediate attention today!")
elif Priority == "low" and Time_Bound =="no":
    print("Read a book' is a low priority task. Consider completing it when you have free time")
else:
    print("pleas try again")