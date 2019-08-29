def name_value(my_list):
	final_score = []
	for index in range(len(my_list)):
		word = my_list[index]
		word_score = 0
		for letter in word:
			if letter != " ":
				word_score += ord(letter) - 96
		final_score.append(word_score * (index + 1))
	return final_score

print(name_value(["abc","abc abc"]))