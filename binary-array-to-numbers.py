def binary_array_to_number(arr):
	count = 0
	summ = 0 
	for i in arr[::-1]:
		summ += (2**count) * i
		count += 1
	return summ

print(binary_array_to_number([0,0,0,1]))
print(binary_array_to_number([0,0,1,0]))
print(binary_array_to_number([1,1,1,1]))
print(binary_array_to_number([0,1,1,0]))