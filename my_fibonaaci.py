def recursive_fibonacci(n):
    if n<=1:
        return n
    return (recursive_fibonacci(n-1)+recursive_fibonacci(n-2))

n = int(input("Non neg number :"))
result = []

for i in range(n+1):
    result.append(recursive_fibonacci(i))

print(result)

#total time complexity is 2^n * O(1) = O(2^n).