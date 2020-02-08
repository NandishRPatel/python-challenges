def isPrime(n):
    if n in [2, 3, 5]:
        return True
    else:
        if (n + 1) % 6 == 0 or (n - 1) % 6 == 0:
            return True
        else:
            return False



def primeFactors(n):
    i = 2
    s = ""
    count = 0
    while n > 1:
        if isPrime(i):
            while n % i == 0:
                n = n / i
                count += 1
            if count != 0:
                if count > 1:s += "(" + str(i) + "**" + str(count) + ")"
                else:s += "(" + str(i) + ")"
                count = 0
            i += 1
        else:
            i += 1
    return s


print(primeFactors(7775460))