import math
def decomp(n):
	final_string = ""
	total = math.factorial(n)
	final = total
	i = 2
	while final > 1:
		if is_prime(i):
			print(i)
			times = 0
			while final % i == 0:
				final = final / i
				print(final)
				times += 1
			if times > 1:final_string += str(i) + "^" + str(times) + " * "
			elif times == 0: final_string += ""
			else: final_string += str(i) + " * "
		i += 1
	return final_string.strip(" * ")

def is_prime(n):
	if n <= 3: return n > 1
	elif  n % 2 == 0 or n % 3 == 0:
		return False
	i = 5
	while i <= int(n ** 0.5):
		if n % i == 0 or n % (i + 2) == 0:
			return False
		i += 6
	return True

print(decomp(79))