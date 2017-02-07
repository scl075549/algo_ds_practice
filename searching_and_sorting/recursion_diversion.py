# Solving for Fib numbers iteratively, then with the magic of recursion

# Iterative approach
def fib_iterative(n):
    if n == 0 or n == 1:
        return n
    first, second = 0, 1
    next_fib = first + second
    for _ in range(2, n):
        first = second
        second = next_fib
        next_fib = first + second
    return next_fib

# Recursive approach
def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# n = 8, Expected: [0, 1, 1, 2, 3, 5, 8, 13]
print([fib_iterative(x) for x in range(8)])
print([fib_recursive(x) for x in range(8)])
