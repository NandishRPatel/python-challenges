def solve(string):
	vowels = "aeiou"
	values = []
	temp_string = ""
	for letter in string:
		if not letter in vowels:
			temp_string += letter
		else:
			if temp_string != "":
				values.append(get_score(temp_string))
				temp_string = ""
	return max(values)

def get_score(string):
	score = 0
	for letter in string:
		score += ord(letter) - 96
	return score

print(solve("zodiacs"))