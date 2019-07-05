def removNb(n):
	final_list = []
	summ = int(n * (n + 1) / 2)
	lower =int(((n - 1) * n / 2) / (n + 1))
	upper = int((summ+1)**.5) - 1 
	a = upper
	while(a >= lower):
		b = (summ - a) // (a+1)
		if a * b == summ - a - b:
			final_list.append((a,b))
			final_list.append((b,a))
		a -= 1

	return sorted(final_list)

print(removNb(26))