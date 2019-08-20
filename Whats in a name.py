def name_in_str(sen, name):
	sen = sen.lower()
	name = name.lower()
	if sen.find(name) != -1:
		return True
	else:
		flag = 1
		index = -1
		for i in range(len(name)):
			idx = sen.find(name[i])
			if idx != -1:
				if index <= idx:
					flag *= 1
				else:
					flag *= 0
			else:
				return False
			sen = sen[idx + 1:]
		return bool(flag)


print(name_in_str("Just enough nice friends","Jennifer"))