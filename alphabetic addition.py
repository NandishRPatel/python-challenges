def add_letters(*letters):
	if not letters: return 'z'
	else:
	    letters_ascii = [ord(i) - ord('a') + 1 for i in letters]
	    addition = sum(letters_ascii)
	    if addition > 26:
	    	return chr(addition - 26 + ord('a') - 1)
	    return chr(addition + ord('a') - 1)

print(add_letters([]))