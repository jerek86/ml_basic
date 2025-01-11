def is_even(number) :
    return number & 1 == 0

def is_prime(number) :
    if number < 2 :
        return False

    if number == 2 :
        return True

    if is_even(number) :
        return False

    for i in range(3, number) :
        if number % i == 0 :
            return False

        if i*i > number :
            break

    return True

print('is_prime(17):', is_prime(17))
print('is_prime(20):', is_prime(20))
print('is_prime(23):', is_prime(23))