# Write	is_prime(n) that returns True/False	for	whether	n is prime.

def is_prime(n) :
    flag = True
    for i in range(2,n) :
        if n > 1 :
            if n % i == 0 :
                flag = False
                break
        else :
            return False
    return flag

n = int(input("Enter number : "))

if is_prime(n) :
    print(f"{n} is a Prime")
else :
    print(f"{n} is not a prime")