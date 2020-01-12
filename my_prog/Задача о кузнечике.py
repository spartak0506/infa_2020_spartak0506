def fib(n):
    A = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        A[i] = A[i - 1] + A[i - 2] + A[i - 3]
    return A[n]
