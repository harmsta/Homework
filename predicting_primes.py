import sympy

lower_limit = 2
upper_limit = int(input('What is the upper limit? '))

prime_count = 0

for number in range(lower_limit, upper_limit):
    if sympy.isprime(number):
        prime_count += 1

print(prime_count)
