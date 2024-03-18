"""
 1. Division Method - h(k) = k % m
 m = prime no. 
"""

"""
 2. Multiplication Method - h(k) = {( a.k )% 2^m } w - r
a = random number
w = no. of bits in k
m = 2^r
"""

"""
 3. Universal Method - h(k) = [ (ak + b) % P] % m

"""

import hashlib


def hash_string(input_string):
    sha256_hash = hashlib.sha256(input_string.encode("utf-8")).hexdigest()
    return sha256_hash


names = [
    "Gaurav",
    "Joshi",
    "Diksha",
]
hash_names = [hash_string(name) for name in names]

for i in range(len(names)):
    print(f"{names[i]}:  {hash_names[i]}")
