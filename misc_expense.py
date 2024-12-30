from decimal import Decimal

special_tool_expense_list = []
def equipment_special_tool_expense():

    while True:
        special_tool_expense = str(input("""Do you have any special tool or equipment expense 
        designated to this job soley? 
            "Yes or No? """).lower())
        if special_tool_expense == "yes":
            while True:
                try:
                    cost_of_tool = input("What is the exact cost in USD? ")
                    break  # Exit loop if valid input
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
            itemized_tool = input("Name the tool or expense we are itemizing. ")
            print(f"The addition of {itemized_tool} adds an additional ${Decimal(cost_of_tool)}")
            special_tool_expense_list.append({
                "name": itemized_tool,
                "cost": cost_of_tool
            })
        elif special_tool_expense == "no":
            break
        else:
            print("You need to answer Yes or No. ")
    expense = __name__
    total_cost = sum(['cost'] for expense in special_tool_expense_list)
    return total_cost

def equipment_listed():
    # Check if the list is empty
    if not special_tool_expense_list:
        print("No special tools or equipment expenses have been added.")
        return 0
    else:
        print("\nSpecial Tool or Equipment Expenses:")
        # Loop through the list and print each item
        for index, expense in enumerate(special_tool_expense_list, start=1):
            print(f"Item {index}: {expense['name']} - ${expense['cost']:.2f}")
        list_of_expenses = sum(expense['cost'] for expense in special_tool_expense_list)

