
print("Welcome to JebWise!")
print()

expenses = []

while True:
    amount = float(input("Enter Expense Amount: ₹"))
    expense = input("Enter expense category: ").strip().title()

    print("\n--- Your Expense ---")
    print(f"Amount: ₹{amount:.2f}")
    print(f"Category: {expense}")

    expenses.append([amount, expense])

    cont = input("\nWant to continue (Yes/No)? ").strip().lower()

    if cont == "no":
        break

print("\n--- All Transactions ---")

for i, exp in enumerate(expenses, start=1):
    print(f"{i}. {exp[1]} — ₹{exp[0]:.2f}")

total = 0

for exp in expenses:
    total += exp[0]

print(f"\nTotal Spending: ₹{total:.2f}")

category_totals = {}

for exp in expenses:
    amount = exp[0]
    category = exp[1]

    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

print("\n--- Category-wise Spending ---")

for category, amount in category_totals.items():
    print(f"{category}: ₹{amount:.2f}")

print("\nThank you for using JebWise!")
