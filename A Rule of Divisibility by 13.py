def thirt(n):
	prev_n = 0
	div_list = [1, 10, 9, 12, 3, 4]
	while(prev_n != n):
		length_d = 0
		temp_var = 0
		l = len(div_list)
		for i in str(n)[::-1]:
			if length_d >= l:
				length_d = 0
			temp_var += int(i) * div_list[length_d]
			length_d += 1
		prev_n = n
		n = temp_var
	return n

print(thirt(1234567))