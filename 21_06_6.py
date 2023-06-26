def find_prime_factors(x):
    ls= []
    i = 1
    while x >= i:
        if x % i == 0   :
            ls.append(i)
            i +=1
        x -=1
    return ls


print(find_prime_factors(36))

#[1, 2, 3, 4, 5, 6, 7, 8, 9]





