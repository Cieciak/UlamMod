import prime_test, generator_test

flag = lambda x: 'passed' if x else 'failed'

print('Testing primes.')
print(flag(prime_test.check_primes()))

generator_test.check_generator()