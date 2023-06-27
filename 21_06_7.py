while True:
    num1 = int(input("Greq arajin tiv@: "))
    num2 = int(input("Greq ekrord tiv@: "))
    gorc = input("please select +, -, /, * or Q(For quit): ")
    if gorc == '+' :
        sum = num1 + num2
    elif gorc == '-':
        sum = num1 - num2
    elif gorc == '*': 
        sum = num1 * num2
    elif gorc == '/' and num2 != 0:
        sum = num1 / num2
    elif gorc == 'Q' :
        break
    else :
        sum = "Haytararum chi karox linel 0"
    print(sum)
    


    









