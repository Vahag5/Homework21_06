def print_pattern(x):
    i = 1
    while i <= x:
        j = 1
        while j <= i:
            print(j, end=" ")
            j += 1
        print()
        i += 1





x = 5
print("Input number is:", x)
print_pattern(x)

'''Input number is: 5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''

