def factorial(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
n=5
factorial_e=factorial(n)
print(f"the factorial of {n} is {factorial_e}")
