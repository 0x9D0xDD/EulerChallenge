# Euler Challenge 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.Multiples of three or five

def three_or_five(end):
    sum_total = 0
    for i in range(1, end):
        if i % 3 == 0 or i % 5 == 0:
            sum_total += i
        else:
            pass
    print(sum_total)

if __name__ == "__main__":
    three_or_five(10)