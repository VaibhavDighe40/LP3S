def fibonacci_iterative(n):
    fib_series = [0, 1]
    while len(fib_series) <= n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n + 1]

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Take user input
n = int(input("Enter a non-negative integer (n): "))
if n < 0:
    print("Please enter a non-negative integer.")
else:
    # Non-Recursive (Iterative)
    result_iterative = fibonacci_iterative(n)
    print(f"Fibonacci series up to {n} using iterative approach: {result_iterative}")

    # Recursive (series)
    # result_recursive_series = [fibonacci_recursive(i) for i in range(n + 1)]
    result_recursive_series = []  # Initialize an empty list to store the Fibonacci series
    for i in range(n + 1):       # Iterate through values of i from 0 to n (inclusive)
        result_recursive_series.append(fibonacci_recursive(i))  # Append the result of fibonacci_recursive(i) to the list
    print(f"Fibonacci series up to {n} using recursive approach: {result_recursive_series}")
