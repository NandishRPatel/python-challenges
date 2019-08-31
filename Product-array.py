def product_array(numbers):
	final_list = []
	for i in numbers:
		final_list.append(multiply(numbers)/i)
	return final_list

def multiply(list_numbers):
	multi = 1
	for i in list_numbers:
		multi *= i
	return multi