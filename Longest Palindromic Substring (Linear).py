'''
    Write a function that returns the longest contiguous palindromic substring in s. 
    In the event that there are multiple longest palindromic substrings, return the 
    first to occur.
'''

# TODO: Complete in linear time xDD
def longest_palindrome(s):
	if not s: return s
	elif len(set(s)) == 1: return s
	else:
		len_s = len(s)
		new = ""
		pallindrome = ""
		length = 0
		for i in range(0, len_s):
			for j in range(len_s - 1, i + length - 1, -1):
				if s[i] == s[j]:
					new = s[i:j + 1]
					if new == new[::-1]:
						if length < len(new):
							pallindrome = new
							length = len(pallindrome)
		
		if pallindrome:return pallindrome
		else: return s[0]
			

'''print(longest_palindrome('babad') == 'bab')
print(longest_palindrome('madam') == 'madam')
print(longest_palindrome('dde') == 'dd')
print(longest_palindrome('ababbab') == 'babbab')
print(longest_palindrome('abababa') == 'abababa')


print(longest_palindrome('banana') == 'anana')
print(longest_palindrome('abba') == 'abba')
print(longest_palindrome('cbbd') == 'bb')
print(longest_palindrome('zz') == 'zz')
print(longest_palindrome('dddd') == 'dddd')


print(longest_palindrome('') == '')
print(longest_palindrome('abcdefghijklmnopqrstuvwxyz') == 'a')
print(longest_palindrome('ttaaftffftfaafatf') == 'aaftffftfaa')

print(longest_palindrome('bbaaacc') == 'aaa')
print(longest_palindrome('m') == 'm')
'''
import time
s = time.time()
print(longest_palindrome('a'*10000) == 'a'*10000)
print(time.time()-s)