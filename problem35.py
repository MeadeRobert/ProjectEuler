import math
import re

with open("primes1.txt") as file:
    primes = set([int(i) for i in re.findall(r'[0-9]+', file.read())])
    
def is_circular_prime(n):
    values = set([])
    digits = [int(i) for i in str(n)]
    for i in range(0, len(digits)):
        values.add(int(''.join([str(j) for j in (digits[i::] + digits[:i:])])))
    for i in values:
        if i not in primes:
            return False
    return True
# print(is_circular_prime(142))
# print(is_circular_prime(197))

n = 0
for i in primes:
    if is_circular_prime(i):
        n += 1
        print(i)
print(n)
