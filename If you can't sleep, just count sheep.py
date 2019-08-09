def count_sheep(n):
	final_string = ""
	for i in range(1,n+1):
		final_string += str(i) + " sheep..."
	return final_string

print(count_sheep(2))