def likes(names):
	length_names = len(names)
	if length_names == 0:
		return 'no one likes this'
	elif length_names == 1:
		return names[0] + ' likes this'
	elif length_names == 2:
		return names[0] + ' and ' + names[1] +  ' like this'
	elif length_names == 3:
		return names[0] + ', ' + names[1] + ' and ' + names[2]  +  ' like this'
	else:
		return names[0] + ', ' + names[1] + ' and ' + str(length_names - 2) + ' others like this'


print(likes(['Peter']))