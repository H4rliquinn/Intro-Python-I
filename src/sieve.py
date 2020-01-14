import math

# Get user number
print("Gimme Number")
# user_input = 300000
user_input = input()

# Find highest prime that could be a factor
# highest_val = int(math.sqrt(int(user_input))//1)
# highest_val = user_input

# Create Sieve
primes = [2, 3, 5, 7]
sieve = [x for x in range(int(user_input)+1) if x > 1 and x %
         2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0]

# Process Sieve
while len(sieve) > 0:
    new_prime = sieve.pop(0)
    primes.append(new_prime)
    for x in range(int(user_input)+1//new_prime):
        if new_prime*x in sieve:
            sieve.remove(new_prime*x)
# print(highest_val, sieve, primes)
print(primes)

if int(user_input) in primes:
    print("PRIME!")
else:
    print("NOT PRIME!")
