# Tail Recursion

def tail(n):
    if n == 0:
        return

    # do some operation
    print(n)

    tail(n - 1)

def head(n):

    if n==0:
        return

    head(n-1)

    #do something
    print(n)

#call main
if __name__ == "__main__":
    head(5)
