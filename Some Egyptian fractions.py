def decompose(string):
	flag = 1
	if '/' in string:
		num, denum = [int(i) for i in string.split("/")]
		if (num >= denum) and (num % denum) == 0:return [str(num//denum)]
		else:
			final_list = []
			while num > 0:
				target = str(-(-denum // num))
				if target == "1":final_list.append("1")
				else: final_list.append("1/" + target)
				temp_num = (-denum) % num
				temp_denum = denum * -(-denum // num)
				num, denum = temp_num, temp_denum

			return final_list

	elif '.' in string: 
		before , after = string.split(".")
		if before == 0:num = after
		else:num = before + after

		denum = 10 ** len(after)
		print(num + "/" + str(denum))
		return decompose(num + "/" + str(denum))

	else:
		if int(string) == 0: return []
		else: return [string]


print(decompose(input("Input fraction string : ")))