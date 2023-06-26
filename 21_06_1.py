def find_factorial(n):
    if n == 0:
        pass
    else:
        factorial = 1
        while n > 0:
            factorial *= n
            n -= 1
        return factorial


x = int(input())
factor =  find_factorial(x)
print(factor)


