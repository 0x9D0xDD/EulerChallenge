# Euler Challenge 4
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    num = str(num)
    num_r = num[::-1]
    return num == num_r

def palindrome_sums(n_seq):
    palindromes = []
    for i in range(0,n_seq):
        if is_palindrome(i):
            palindromes.append(i)
        else:
            pass
    print(palindromes[len(palindromes)-1] +
          palindromes[len(palindromes)-2])

if __name__ == "__main__":
    palindrome_sums(1000)
