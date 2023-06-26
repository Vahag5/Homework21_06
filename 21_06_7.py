num1 = int(input("Greq arajin tiv@: "))
num2 = int(input("Greq arajin tiv@: "))
gorc = input("please select +, -, / or *: ")
if gorc == '+' :
    sum = num1 + num2
elif gorc == '-':
    sum = num1 - num2
elif gorc == '*': 
    sum = num1 * num2
elif gorc == '/' and num2 != 0:
    sum = num1 // num2 
else :
        sum = "Haytararum chi karox linel 0"
print(sum)






