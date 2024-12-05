"""
Name:Lotoya Willis
Date:01/21/2024
Assignment:Module1:Mersenne Primes
Due Date:01/21/2024
About this project: This script calculates the Mersenne Primes up to a
user entered number.
Assumptions: NA
All work below was performed by Lotoya Willis """


def find_primes():
    range_max = input('Please enter in a positive number or -99 to quit ')

    # Prevents errors if a non-integer is entered
    try:
        range_max = int(range_max)
    except ValueError:
        range_max = 2

    # Stops loop if -99 is entered
    while range_max != -99:
        if range_max >= 3:  # Mersenne Primes begin after limits 3 or greater
            n = 3
            prime = (2 ** n) - 1
            prime_numbers = [3]  # This list contains all the prime numbers that are Mersenne Primes

            # The Lucas-Lehmer Primality Test is used in this program to figure out
            # if a number that can be written as 2**n - 1 is also prime, since that
            # is the definition of a Mersenne Prime
            while prime <= range_max:
                a = 4 % prime

                for i in range(n - 2):
                    a = (a**2 - 2) % prime

                if a == 0:
                    prime_numbers.append(prime)

                n = n + 1
                prime = (2 ** n) - 1

            print('Mersenne Primes')
            print(prime_numbers)  # Displays the Mersenne Primes

            range_max = input('Please enter in a positive number or -99 to quit ')

            # Prevents errors if a non-integer is entered
            try:
                range_max = int(range_max)
            except ValueError:
                range_max = 2
        elif range_max < 0:  # Negative numbers cannot be used to find Mersenne Primes
            range_max = input('Please enter in a positive number or -99 to quit ')

            # Prevents errors if a non-integer is entered
            try:
                range_max = int(range_max)
            except ValueError:
                range_max = 2
        else:  # No Mersenne Primes are less than 3
            print("There are no Mersenne Primes for this upper limit")
            range_max = input('Please enter in a positive number or -99 to quit ')

            # Prevents errors if a non-integer is entered
            try:
                range_max = int(range_max)
            except ValueError:
                range_max = 2


def main():
    find_primes()


if __name__ == '__main__':
    main()
