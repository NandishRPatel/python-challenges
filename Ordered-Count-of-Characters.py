def ordered_count(input):
	final_list = []
	for i in input:
		tup = (i,input.count(i))
		if not tup in final_list:final_list.append(tup)
	return final_list

print(ordered_count("Code Wars"))