# define the function using recursion
def euclidean_algorithm(n1, n2):
    # base case is when n2 becomes 0, assuming n1 will always be greater
    if n2 == 0:
        # when n2 becomes 0, n1 is the gcd
        return n1
    else:
        # repeat with n2 and the remainder of n1 divided by the n2
        return euclidean_algorithm(n2, n1 % n2)

# provide values and print the result
gcd = euclidean_algorithm(39, 120)
print("The GCD is", gcd)
