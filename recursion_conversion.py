#implementation of conversion between head recursion and tail recursion

def factorial(n):

    if n==1:
        return 1
    return n*factorial(n-1)

def factorial_accumulator(n,accumulator=1):

    if n==1:
        return accumulator

    return factorial_accumulator(n-1,n*accumulator)

if __name__ == "__main__":
    print(factorial_accumulator(5))
