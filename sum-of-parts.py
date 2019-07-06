def parts_sums(ls):
    final_list = [sum(ls)]
    for i in range(0,len(ls)):
    	final_list.append(final_list[i] - ls[i])
    return final_list

print(parts_sums([0, 1, 3, 6, 10]))