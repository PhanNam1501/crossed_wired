import random
from math import gcd

def factorize(N, e, d):
    k = d * e - 1
    
    while True:
        # Step 2: Try a random g
        g = random.randint(2, N - 1)
        t = k

        # Step 3: Next t
        while t % 2 == 0:
            t //= 2
            x = pow(g, t, N)

            # Step 4: Finished?
            if x > 1:
                y = gcd(x - 1, N)
                if y > 1:
                    p = y
                    q = N // y
                    return p, q

# Example usage
N = 33  # Replace with your RSA modulus
e = 3   # Replace with your public exponent
d = 7   # Replace with your private exponent

p, q = factorize(N, e, d)
print(f"p = {p}, q = {q}")
