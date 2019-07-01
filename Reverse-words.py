def reverse_words(text):
	words = text.split(' ')
	return " ".join(word[::-1] for word in words)


print(reverse_words("double  spaced  words"))