import csv
from ctypes import CDLL

COMPILED_LIB = CDLL('./bin/libprimes.so')
PRIMES_CSV = './tests/test_data/primes.csv'

def check_primes() -> bool:
    known_primes: dict = {}
    with open(PRIMES_CSV) as file:
        raw_data = csv.reader(file)
        for row in raw_data:
            index, prime = map(int, row)
            known_primes[index] = prime

    for n, prime in known_primes.items():
        if prime != COMPILED_LIB.prime(n): return 0

    return 1