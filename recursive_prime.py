number_to_check = int(input('What number would you like the prime factors of?'))

def prime_factorization(number_to_check):
    factors = []
    if number_to_check > 1:
        number = 2
        while number_to_check % number != 0:
            number +=1
        factors.append(number)
        factors.extend(prime_factorization(number_to_check // number))
    return factors

print(prime_factorization(number_to_check))
