from math import factorial as fact
from math import gcd
from fractions import Fraction as F

def expand(x, digit):
	target_digit = 1
	power = 1
	target_sum = F(1, 1)
	deci, flag = 0, 0
	if type(x) == float:
		flag = 1
		before, after = str(x).split(".")
		deci = len(after)
		x = int(before + after)
	while target_digit < digit:
		num = x ** power
		if flag:
			denum = ((10 ** deci) ** power) * fact(power)
		else:
			denum = fact(power)
		GCD = gcd(num, denum)
		if GCD != 1:num //= GCD;denum //= GCD
		target_sum += F(num, denum)
		target_digit = len(str(target_sum).split("/")[0])
		power += 1
	
	return [int(i) for i in str(target_sum).split("/")]



print(expand(1.6, 10))
print('####################')
print(expand(1.7, 10))
print('####################')
print(expand(1.7, 12))
print('####################')
print(expand(1.7, 15))
print('####################')
print(expand(1.8, 20))

