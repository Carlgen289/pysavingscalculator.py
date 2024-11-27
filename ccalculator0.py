# want to make a calculator
# helps me with my spending habits and save money

# 1st feature - input my total salary - create input
# 2nd feature - has tax and epf/socso cuts
# create percentage and cut off for tax qualification
# socso percetange = 0.5% (* 0.05)
# 3rd feature - 50:30:20 ratio (* 0.5, 0.3, 0.2)
# 50 - commitments
# 30 - enjoy money
# 20 - savings
# results displays all breakdowns

def ccalculator():
    # input total salary
    salary = float(input("Please enter salary here (Before deduction): "))
    
    # tax rate based on salary brackets
    if salary <= 5000:
        tax_rate = 0
    elif salary <= 20000:
        tax_rate = 0.01
    elif salary <= 35000:
        tax_rate = 0.03
    elif salary <= 50000:
        tax_rate = 0.06
    elif salary <= 70000:
        tax_rate = 0.11
    elif salary <= 100000:
        tax_rate = 0.19
    elif salary <= 400000:
        tax_rate = 0.25
    elif salary <= 600000:
        tax_rate = 0.26
    elif salary <= 2000000:
        tax_rate = 0.28
    else:
        tax_rate = 0.30
    
    #calculate tax and socso deductions
    tax = salary * tax_rate
    socso = salary * 0.005
    net_salary = salary - (tax + socso)

# print deductions and breakdown
print("\nDeductions: ")
print(f"Tax ({tax_rate * 100}%): RM {tax:.2f}")
print(f"socso (0.5%): RM {socso:.2f}")
print(f"Net Salary after deductions: RM {net_salary:.2f}\n")

# budget breakdown (50:30:20 rule)
commitments = net_salary * 0.5
enjoyment = net_salary * 0.3
savings = net_salary * 0.2

print("Budget Breakdown: ")
print(f"Commitments: RM {commitments:.2f}")
print(f"Enjoy Money: RM {enjoyment:.2f}")
print(f"Savings: RM {savings:.2f}")

# run the calculator
ccalculator()
