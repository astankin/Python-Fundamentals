deposit_amount = float(input())
length_of_deposit = int(input())
interest_rate = float(input())
interest = (deposit_amount * interest_rate / 100)/12
amount = deposit_amount + length_of_deposit * interest
print(amount)
