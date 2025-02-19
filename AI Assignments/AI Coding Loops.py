def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_sequence(n):
    return [fib(i) for i in range(n)]

num_terms = int(input("Enter the number of Fibonacci terms: "))
print("Fibonacci Sequence:", *fib_sequence(num_terms))
