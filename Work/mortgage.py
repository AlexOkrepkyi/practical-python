# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05

payment = 2684.11
extra_payment = 1000
high_payment = payment + extra_payment

current_month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108

total_paid = 0.0

while principal > 0:

    if current_month in range(extra_payment_start_month, extra_payment_end_month + 1):
        principal = principal * (1 + rate / 12) - high_payment
        total_paid = total_paid + high_payment
        print(f'extra | M {current_month} | TP: ${round(total_paid, 2)} | P: ${principal}')
        current_month += 1
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment
        print(f'M {current_month} | TP --> ${round(total_paid, 2)} | P --> ${principal}')
        current_month += 1


print(f'Total paid (amends for the negative balance) --> '
      f'${round(total_paid + principal, 2)} after {current_month} months')
