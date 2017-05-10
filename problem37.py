import math
import re

with open("primes1.txt") as file:
    primes = set([int(i) for i in re.findall(r'[0-9]+', file.read())])

not_truncatable_primes = set([2, 3, 5, 7])
truncatable_primes = set()

def is_truncatable_prime(n):
    s = str(n)
    l = len(s)
    if n not in not_truncatable_primes:
        for i in range(1, l):
            if (int(s[i::]) not in primes) or (int(s[0:i]) not in primes):
                not_truncatable_primes.add(n)
                return False
        return True
    else:
        return False        
                
for i in primes:
    if(is_truncatable_prime(i)):
        truncatable_primes.add(i)
        #print(i)
    if len(truncatable_primes) > 10:
        break
    
print(truncatable_primes)
print(sum(truncatable_primes))
