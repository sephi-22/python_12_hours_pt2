#Develop a function that checks if all rotations of a number's digits are prime
#Hint: Generate all rotations of the number and check each one for primality.

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def is_circular_prime(x):
    str_x = str(x)
    for i in range(len(str_x)):
        if not is_prime(int(str_x[i:]+str_x[:i])):
            return False
    return True

print(is_circular_prime(113))