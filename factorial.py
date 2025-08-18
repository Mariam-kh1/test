def factorial(n):
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    return fact

print(factorial(5))
