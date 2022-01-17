# Euler Challenge 3
# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def sieve_of_eratosthenes():
    sieve = [0] * 775147
    count = 2
    for i in sieve:
        if i % count == 0:
            sieve[i] = "c"
        else:
            pass
        count += 1
    primes = []
    for m in sieve:
        if sieve[m] == "c":
            pass
        else:
            primes.append(m)
    print(primes)

if __name__ == "__main__":
    sieve_of_eratosthenes()
