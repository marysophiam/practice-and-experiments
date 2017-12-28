# Getting close, but not quite there yet.

def fibonacci_iterative(n):

    if n <= 1:
        return n

    a = 0
    b = 1
    total = 0

    for i in range(n + 1):
        total = a + b
        a = b
        b = total

    return total


for n in range(10):
    print fibonacci_iterative(n)

    