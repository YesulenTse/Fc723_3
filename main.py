# define function, we are using recursion
def eaclidean_algorithm(n1, n2):
    # find the min
    gcd = min(n1, n2)
    # implement recursion
    while gcd:
        # base case is when there is no remainder when divided by 2 numbers
        if n1 % gcd == 0 and n2 % gcd == 0:
            break
        # minus one if have not found the base case, repeat until found
        gcd -= 1
    # return the found gcd
    return gcd

# give values, and print result
gcd = eaclidean_algorithm(39, 120)
print("The GCD is", gcd)