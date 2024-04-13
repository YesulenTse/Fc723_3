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
