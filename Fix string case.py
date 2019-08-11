def solve(word):
	count_lower, count_upper = 0,0
	for letter in word:
		if letter.islower():
			count_lower += 1
		else:
			count_upper += 1
	if count_upper > count_lower:
		return word.upper()
	else:
		return word.lower()



print(solve("coDE"))