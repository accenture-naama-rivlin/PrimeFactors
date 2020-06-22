class PrimeNumber:

    def factorize(self, number):

        prime_numbers =[]

        for n in range(2, number + 1):
            if number % n == 0:
                for element in range(2, n+1):
                    if element % n == 0 and element != number:
                        prime_numbers.append(n)
                        number /= n
                    if element == number:
                        prime_numbers.append(n)

        return prime_numbers