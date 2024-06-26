# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate projected annual savings with 5% interest
annual_savings = monthly_savings * 12 * (1 + 0.05)

# Print results
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Projected annual savings after one year with 5% interest: ${annual_savings:.2f}")
