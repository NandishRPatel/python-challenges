'''
    Write a function that returns the longest contiguous palindromic substring in s. 
    In the event that there are multiple longest palindromic substrings, return the 
    first to occur.
'''

# TODO: Complete in linear time xDD
def longest_palindrome(s):
	if not s: return s
	else:
		string = s[0]
		pallindrome = ""
		for i in s[1:]:
			length = len(pallindrome)
			string += i
			if string == string[::-1]:
				if len(string) > length:
					pallindrome = string

		return pallindrome

print(longest_palindrome("cbbd"))