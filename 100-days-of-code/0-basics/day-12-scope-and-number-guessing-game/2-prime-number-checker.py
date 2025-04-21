def is_prime(num):
    is_prime = True
    counter = 2
    if num < 0:
        num = num*(-1)
    while is_prime == True and counter < num:
        if num%counter == 0:
            is_prime = False
        counter += 1
    return is_prime

print(is_prime(73))
