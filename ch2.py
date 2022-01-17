# Euler Challenge 2
# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def generate_fibbonaci():
    sequence = [1,2]
    limit = False
    while limit is False:
        new_val = sequence[len(sequence)-1] + sequence[len(sequence)-2]
        if new_val < 4000000:
            sequence.append(new_val)
        else:
            limit = True
    return sequence

def even_fib_sum(n_seq):
    num_sum = 0
    for i in n_seq:
        if i % 2 == 0:
            num_sum += i
        else:
            pass
    print(num_sum)

if __name__ == "__main__":
    n_seq = generate_fibbonaci()
    even_fib_sum(n_seq)
