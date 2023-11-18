import os
def calculate_monthly_instalment(principal, interest_rate, loan_term):
    monthly_interest_rate = interest_rate / 12 / 100
    total_payments = loan_term * 12
    monthly_payment = principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** total_payments) / (((1 + monthly_interest_rate) ** total_payments) - 1)
    return monthly_payment

def calculate_total_payment(monthly_payment, loan_term):
    total_payment = monthly_payment * loan_term * 12
    return total_payment

def calculate_dsr(monthly_income, monthly_debt_commitments):
    dsr = (sum(monthly_debt_commitments) / monthly_income) * 100
    return dsr

def display_loan_details(loan_details):
    if not loan_details:
        print("No previous loan calculations.")
    else:
        print("Previous Loan Calculations:")
        for idx, details in enumerate(loan_details, start=1):
            print(f"Loan {idx}:")
            print(f"Principal: ${details['principal']}")
            print(f"Monthly Instalment: ${details['monthly_payment']:.2f}")
            print(f"Total Payment: ${details['total_payment']:.2f}")
            print(f"DSR: {details['dsr']:.2f}%")
            


