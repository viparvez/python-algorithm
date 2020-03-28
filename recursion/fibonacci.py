def fibonacci(n):
    if n==0: return 0
    if n==1: return 1

    fib1 = fibonacci(n-1)
    fib2 = fibonacci(n-2)

    result = fib1+fib2

    return result

if __name__ == "__main__":
    print(fibonacci(10))