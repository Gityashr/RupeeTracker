salary = int(input("Enter the take home pay"))
loan_amt = int(input("Enter the loan amount: "))
interest_rate = int(input("Enter the interest rate: "))
years = int(input("The no. of years"))
yearly_loan_amt = loan_amt / years
total_amt = (years * yearly_loan_amt) + (years * yearly_loan_amt * (interest_rate/100))
total_int = years * yearly_loan_amt * (interest_rate/100)
monthly_amt = total_amt / (years * 12)
print("Total amount to be paid:")
print(total_amt)
print("Total interest:")
print(total_int)
print("Monthly amount to be paid:")
print(monthly_amt)

rem_sal = salary - monthly_amt
saving = rem_sal * 0.2
spend_lim = rem_sal - saving
warning_threshold = spend_lim * 0.8
amt_spent = int(input("Enter the amount spent"))
if amt_spent >= warning_threshold:
    print("You are close to the monthly spending limit, be careful")
else:
    print("You don't have to worry yet")
input()