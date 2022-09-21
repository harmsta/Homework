import random

total_charge_dollars = random.randint(1, 100)
total_charge_coins = (random.randint(1, 100))/100

total_charge = total_charge_dollars + total_charge_coins
print(f'The total charge was: ${total_charge}')

user_payment = random.randint(1, 100) + (random.randint(1, 100)/100) + total_charge
print(f'the user payed in :${user_payment:.2f}')

customer_change = user_payment - total_charge
print(f'Customer change is ${customer_change:.2f}')

working_change_value = customer_change

while 100 <= working_change_value:
    print('you can give back a hundred dollars')
    working_change_value -= 100
    print(f'You still owe the customer {working_change_value:.2f}')

while 50 <= working_change_value:
    print('you can give back a $50')
    working_change_value -= 50
    print(f'You still owe the customer {working_change_value:.2f}')

while 20 <= working_change_value:
    print('you can give back a $20')
    working_change_value -= 20
    print(f'You still owe the customer ${working_change_value:.2f}')

while 10 <= working_change_value:
    print('you can give back a $10')
    working_change_value -= 10
    print(f'You still owe the customer ${working_change_value:.2f}')

while 5 <= working_change_value:
    print('you can give back a $5')
    working_change_value -= 5
    print(f'You still owe the customer ${working_change_value:.2f}')

while 1 <= working_change_value:
    print('you can give back a $1')
    working_change_value -= 1
    print(f'You still owe the customer ${working_change_value:.2f}')

while .25 <= working_change_value:
    print('you can give back $.25')
    working_change_value -= .25
    print(f'You still owe the customer ${working_change_value:.2f}')

while .10 <= working_change_value:
    print('you can give back $.10')
    working_change_value -= .10
    print(f'You still owe the customer ${working_change_value:.2f}')

while .05 <= working_change_value:
    print('you can give back $.05')
    working_change_value -= .05
    print(f'You still owe the customer ${working_change_value:.2f}')

while .01 <= working_change_value:
    print('you can give back $.01')
    working_change_value -= .01
    print(f'You still owe the customer ${working_change_value:.2f}')

if 0 <= working_change_value:
    print('You have given all the change')
