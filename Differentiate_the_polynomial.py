import re

def differentiate(equation, point):
	final = 0
	for i in re.findall("[-+]?[^+-]+", equation):
		if 'x' in i:
			if '^' in i:
				coef, exp = re.split("\\^", i)
				coef = coef[:-1]
				exp = int(exp)
			else:
				coef = i[:-1]
				exp = 1
				print(coef, exp)
			
			if coef == "-":coef = -1
			elif coef == "":coef = 1
			elif coef == "+":coef = 1
			else:coef = int(coef)
			if int(exp) >= 2:
					coef  *= exp
					exp = exp - 1
					final += coef * (point ** exp)
			else:final += coef
	return final


print(differentiate("x^2+x", 3))