# the first element does not count
# the jump begins with [0]

def fib(n, price:list):
    A = [-1,0]+[0] * n
    for i in range(0, n+1):
        A[i] = min((A[i-1] + price[i]), (A[i-2] + price[i]))
    return A[n]
    
    
