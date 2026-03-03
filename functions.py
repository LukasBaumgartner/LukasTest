def add(a, b):
    return a + b
print(add(2,3))

def rec_factorial(n):
    """
    Input: n (integer)
    This function calculates the factorial of n using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * rec_factorial(n-1)

print(rec_factorial(4))
