'''def sum_dig_pow(a, b):
	final_list = []
	for i in range(a,b+1):

		if len(str(i)) == 1: final_list.append(i)
		else:
			string = str(i)
			num = 0
			
			for j in range(0, len(string)):
				num += int(string[j]) ** int(j+1)
			
			if num == i:final_list.append(i)
	return final_list
'''


def sum_dig_pow(a, b):
	final_list = []
	for i in range(a,b+1):
		sum_num = sum(int(k)**j for j,k in enumerate(str(i),1))
		if i == sum_num: final_list.append(i)
	return final_list

print(sum_dig_pow(89,135))