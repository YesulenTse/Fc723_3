# link to github repository:
# https://github.com/YesulenTse/Fc723_3


# pseudocode:
# Function RecursiveEuclideanAlgorithm(n1, n2)
#     If n2 == 0 Then
#         Return n1
#     Else
#         Return RecursiveEuclideanAlgorithm(n2, n1 MOD n2)
#     End If
# End Function


# application
# define the function
def euclidean_algorithm(n1, n2):
    # base case is when n2 becomes 0, assuming n1 will always be greater
    if n2 == 0:
        # when n2 becomes 0, n1 is the gcd
        return n1
    else:
        # repeat with n2 and the remainder of n1 divided by the n2
        return euclidean_algorithm(n2, n1 % n2)


if __name__ == "__main__":
    try:
        # ask the user for input numbers
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))

        # check for valid input (both numbers should be positive integers)
        if n1 <= 0 or n2 <= 0:
            raise ValueError("Input numbers must be positive integers.")

        # call the function to calculate the gcd
        gcd = euclidean_algorithm(n1, n2)
        print("The GCD is", gcd)

    except ValueError as ve:
        # handle invalid input error
        print("Error:", ve)



# another extension could be to state all the prime divisors
# of the gcd, which could provide more info abt the numbers.

# the pseudocode would be :

# Function PrimeFactorsOfGCD(a, b)
#     gcd = EuclideanAlgorithm(a, b)  // Compute the GCD using the standard Euclidean Algorithm
#
#     // Initialize an empty list to store the prime factors of the GCD
#     prime_factors = []
#
#     // Iterate from 2 to the square root of the GCD
#     for i from 2 to floor(sqrt(gcd))
#         // Check if i is a factor of the GCD
#         while gcd % i == 0
#             // If i is a factor, add it to the list of prime factors
#             prime_factors.append(i)
#             // Divide the GCD by i
#             gcd = gcd / i
#
#     // If the GCD is still greater than 1, it is a prime factor itself
#     if gcd > 1
#         prime_factors.append(gcd)
#
#     // Return the list of prime factors of the GCD
#     return prime_factors
# End Function