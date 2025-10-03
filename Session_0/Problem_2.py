def even_fib_sum(limit):
    a, b = 1, 2   # Starting values
    total = 0
    while a <= limit:
        if a % 2 == 0:   # Check if even
            total += a
        a, b = b, a + b
    return total

print(even_fib_sum(4000000))
