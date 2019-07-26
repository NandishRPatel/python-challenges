def row_sum_odd_numbers(n):
	sum_odd = 0
	for i in range(n * (n-1) + 1, n * (n+1)):
		if i%2 != 0 :
			sum_odd += i
	return sum_odd

print(row_sum_odd_numbers(5))