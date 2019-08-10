def spin_words(sentence):
	final_string = ""
	words = sentence.split()
	for word in words:
		if len(word) >= 5:
			final_string += word[::-1] + " "
		else:
			final_string += word + " "
	return final_string.strip()


print(spin_words("Welcome"))