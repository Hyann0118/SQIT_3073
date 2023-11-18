import os
def calculate_monthly_instalment(principal, interest_rate, loan_term):
    monthly_interest_rate = interest_rate / 12 / 100
    total_payments = loan_term * 12
    monthly_payment = principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** total_payments) / (((1 + monthly_interest_rate) ** total_payments) - 1)
    return monthly_payment

def calculate_total_payment(monthly_payment, loan_term):
    total_payment = monthly_payment * loan_term * 12
    return total_payment

def calculate_dsr(monthly_income, debt_commitments):
    dsr = (sum(debt_commitments) / monthly_income) * 100
    return dsr

def display_loan_details(loan_details):
    if not loan_details:
        print("No previous loan calculations.")
    else:
        print("Previous Loan Calculations:")
        for idx, details in enumerate(loan_details, start=1):
            print(f"Loan {idx}:")
            print(f"Principal: RM{details['principal']}")
            print(f"Monthly Instalment: RM{details['monthly_payment']:.2}")
            print(f"Total Payment: RM{details['total_payment']:.2}")
            print(f"DSR: {details['dsr']:.21}%")

os.system("cls")
loan_details = []

while True:
    print("\n Main Menu")
    print("1. Calculate New Loan")
    print("2. Display Previous Loan Calculations")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        principal = float(input("Enter the principal loan amount: RM"))
        interest_rate = float(input("Enter the interest rate (%): "))
        loan_term_years = int(input("Enter the loan term in years: "))
        monthly_income = float(input("Enter the monthly income: RM"))
        num_other_commitments = int(input("Enter the number of other monthly financial commitments: "))

        other_commitments = []
        for i in range(num_other_commitments):
            commitment = float(input(f"Enter the amount for commitment {i + 1}: RM"))
            other_commitments.append(commitment)

        monthly_instalment = calculate_monthly_instalment(principal,interest_rate, loan_term_years)
        total_payment = calculate_total_payment(monthly_instalment, loan_term_years)
        total_debt_commitments = other_commitments + [monthly_instalment]

        dsr = calculate_dsr(monthly_income, total_debt_commitments)
        loan_details.append({
            'principal': principal,
            'monthly_payment': monthly_instalment,
            'total_payment': total_payment,
            'dsr': dsr})
        print("\nLoan Calculation Summary:")
        print(f"Monthly Instalment: RM{monthly_instalment:.2f}")
        print(f"Total Payment: RM{total_payment:.2f}")
        if dsr <= 70:
            print("Congratulations! You are eligible for the loan.")
        else:
            print("Sorry, you are not eligible for the loan due to high DSR.")

    elif choice == '2':
        if not loan_details:
            print("No previous loan calculations.")
        else:
            display_loan_details(loan_details)

    elif choice == '3':
        print("Thank you!")
    

    else:
        print("Invalid choice. Please enter a valid option.")