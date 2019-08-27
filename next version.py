def next_version(version):
	count = version.count(".")
	count_9 = version.count("9")
	temp = version.replace(".","")
	if count == 0:return str(int(version) + 1)
	elif count == 1:return str(float(version) + 0.1)
	else:
		temp_list = []
		version_int = int(temp)
		version_int += 1
		version_str = str(version_int)
		if count_9 > count:
			temp_list.append(str(10))
			temp_list.extend([i for i in version_str[2:]])
		else:
			temp_list = [str(i) for i in version_str]
		return ".".join(temp_list)

'''assert next_version("1.2.3") == "1.2.4", "Wrong"
assert next_version("0.9.9") == "1.0.0", "Wrong"
assert next_version("1") == "2", "Wrong"
assert next_version("1.2.3.4.5.6.7.8") == "1.2.3.4.5.6.7.9", "Wrong"
assert next_version("9.9") == "10.0", "Wrong")'''