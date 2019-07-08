def century(year):
	if year > year//100 * 100 : return year//100 + 1
	else: return year//100

print(century(200))