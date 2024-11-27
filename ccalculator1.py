# ChatGPT's version












def ccalculator():
    # Input total salary
    salary = float(input("Please enter salary here (Before deduction): "))
    
    # Tax rate based on salary brackets
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
    
    # Calculate tax and SOCSO deductions
    tax = salary * tax_rate
    socso = salary * 0.005
    net_salary = salary - (tax + socso)
    
    # Output deductions and breakdown
    print("\nDeductions: ")
    print(f"Tax ({tax_rate * 100}%): RM {tax:.2f}")
    print(f"SOCSO (0.5%): RM {socso:.2f}")
    print(f"Net Salary after deductions: RM {net_salary:.2f}\n")

    # Budget breakdown (50:30:20 Rule)
    commitments = net_salary * 0.5
    enjoyment = net_salary * 0.3
    savings = net_salary * 0.2

    print("Budget Breakdown: ")
    print(f"Commitments: RM {commitments:.2f}")
    print(f"Enjoy Money: RM {enjoyment:.2f}")
    print(f"Savings: RM {savings:.2f}")

# Run the calculator
ccalculator()
