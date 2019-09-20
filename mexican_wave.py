def wave(str):
	final_list = []
	if str == "": return list(str)
	else:
		for i in range(len(str)):
			if str[i] != " ":final_list.append(str[:i] + str[i].upper() + str[i+1:])
		return final_list