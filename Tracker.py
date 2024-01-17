import json

def load_data():
    try:
        with open('budget_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': 0, 'expenses': []}

def save_data(data):
    with open('budget_data.json', 'w') as file:
        json.dump(data, file)

def add_income(data, amount):
    data['income'] += amount

def add_expense(data, category, amount):
    data['expenses'].append({'category': category, 'amount': amount})

def calculate_remaining_budget(data):
    total_expenses = sum(item['amount'] for item in data['expenses'])
    remaining_budget = data['income'] - total_expenses
    return remaining_budget

def main():
    budget_data = load_data()

    print("Welcome to the Budget Tracker!")

    while True:
        print("\n1. Add Income\n2. Add Expense\n3. View Budget\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            income_amount = float(input("Enter income amount: "))
            add_income(budget_data, income_amount)
        elif choice == '2':
            expense_category = input("Enter expense category: ")
            expense_amount = float(input("Enter expense amount: "))
            add_expense(budget_data, expense_category, expense_amount)
        elif choice == '3':
            remaining_budget = calculate_remaining_budget(budget_data)
            print(f"\nRemaining Budget: {remaining_budget}")
            print("Expense Breakdown:")
            for item in budget_data['expenses']:
                print(f"{item['category']}: {item['amount']}")
        elif choice == '4':
            save_data(budget_data)
            print("Budget data saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()