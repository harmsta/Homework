def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


if __name__ == "__main__":
    a = 1345456
    b = 2134
    print("gcd(", a, ",", b, ") = ", gcd(a, b))
