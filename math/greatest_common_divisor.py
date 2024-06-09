
# eculid's algorithm 
# based on the fact that gcd(a, b) = gcd(a-b, b), a >=b
# this is easy to prove:
# consider a = m * k and b = n * k where k = gcd(a, b)
# then gcd(a-b, b) = gcd((m-n)*k, n*k) 
# now suppose gcd((m-n)*k, n*k) != k, that is m-n and n has gcd = t > 1. suppose m - n = g* t; n = h * t => m = (g+h) * t
# then a = (g+h) * t * k, b = h * t * k => gcd (a, b) >= t *k > k, which gives a contradication

def gcd(a, b):
    small, big = (a, b) if a <= b else (b, a) 
    if small == 0:
        return big 
    return gcd(big % small, small)


print(gcd(100, 17))