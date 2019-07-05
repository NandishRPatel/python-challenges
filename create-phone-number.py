def create_phone_number(n):
	n = list(map(str, n))
	n = "".join(n)
	return "(" + n[:3] + ")" + " " + n[3:7] + "-" + n[7:]	

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))