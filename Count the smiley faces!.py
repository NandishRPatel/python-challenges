import re
def count_smileys(arr):
	regex = re.compile(r"[:;]{1}[-~]{0,1}[)D]{1}")
	return len(list(filter(regex.match, arr)))

print(count_smileys([';]', ':[', ';*', ':$', ';-D']))