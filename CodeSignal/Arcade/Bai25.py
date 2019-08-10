def evenDigitsOnly(n):
    if n <= 0:
        return True
    a=n%10
    print(a)
    if a%2 != 0:
        return False
    n = int(n/10)
    print(n)
    return evenDigitsOnly(n)

print(evenDigitsOnly(248622))