def match_arrays(v, r):
	count = 0
	for i in v:
		if i in r:
			count += 1
	return count
# DON'T remove
verbose = False # set to True to diplay arrays being tested in the random tests