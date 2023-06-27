def find_prime_factors(x):
    ls= []
    i = 2
    while x >= i:
        if x % i == 0   :
            ls.append(i)
            x = x //i
        else :
            i += 1
    return ls


print(find_prime_factors(36))

#[2, 2, 3, 3]





