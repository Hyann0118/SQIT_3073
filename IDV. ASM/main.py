import os
os.system('cls')
# function for calculate monthly instalment
def monthly_instalment(principal, r, year):
    mon_interest_rate = r / 12 / 100
    n = year * 12
    mon_payment = principal * mon_interest_rate * ((1 + mon_interest_rate) **n) / (((1 + mon_interest_rate) ** n) - 1)
    return mon_payment

# function for calculate total payment
def total_payment(mon_payment,year):
    total_payment = mon_payment * year * 12
    return total_payment

# function for calculate Debt Service Ratio (DSR)
def calculate_dsr(mon_income, total_commitments):
    dsr = (total_commitments / mon_income) * 100
    return dsr

# function for calculate debt commitments
def debt_commitments(other_commitments, monthly_instalment):
    debt_commitments= other_commitments+monthly_instalment
    return debt_commitments

#function to display loan details
def display_loan_details(details):
    if not details:
        print("No previous Loan Detail.")
    else:
        print("Previous Loan Detail:")
        for idx, details in enumerate(details, start=1):
            print(f"Loan {idx}:")
            print(f"Principal: RM{details['principal']}")
            print(f"Monthly Instalment: RM{details['monthly_payment']:.2f}")
            print(f"Total Payment: RM{details['total_payment']:.2f}")
            print(f"DSR: {details['dsr']:.2f}%")
            if details['dsr'] <= 70:
                print("The loan is eligible.")
            else:
                print("Sorry. The loan is not eligible.")
            print("======================")

#Main Program
os.system("cls")
loan_details = []
Selection = ""

while Selection != "4":
        print("\n ====Main Menu====")
        print("Selection 1. Calculate New Loan")
        print("Selection 2. View Previous Loan Calculations")
        print("Selection 3. Delete the Previous Loan Calculation")
        print("Selection 4. Exit")

        Selection = input("Enter your choice: ")
        if Selection == '1':
            principal = float(input("Enter the principal loan amount: RM"))
            r = float(input("Enter the interest rate (%): "))
            year = int(input("Enter the loan term in years: "))
            mon_income = float(input("Enter the monthly income: RM"))
            num_other_commitments = int(input("Enter the number of other monthly commitments: "))

            other_commitments = 0
            for i in range(num_other_commitments):
                commitment = float(input(f"Enter the amount for commitment {i + 1}: RM"))
                other_commitments+=commitment
            monthly_payment = monthly_instalment(principal,r,year)
            tol_payment = total_payment(monthly_payment,year)
            total_commitment = debt_commitments(other_commitments,monthly_payment)
            dsr = calculate_dsr(mon_income,other_commitments)
            loan_details.append({
                'principal': principal,
                'monthly_payment': monthly_payment,
                'total_payment': tol_payment,
                'dsr': dsr})
            print("\nLoan Calculation Summary:")
            print(f"Monthly Instalment: RM{monthly_payment:.2f}")
            print(f"Total Payment: RM{tol_payment:.2f}")
            if dsr <= 70:
                print("Congratulation! The loan is eligible.")
            else:
                print("Sorry.The loan is not eligible.")

        elif Selection == '2':
            display_loan_details(loan_details)
                
        elif Selection == '3':
            if loan_details:
                loan_details.clear()
                print('The records deleted.')
            else:
                print('No records to delete.')
    
        elif Selection > '4':
            print("Invalid choice.")

print("Thank you!")