def solution(roman):
	roman_dict = { "M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1 }
	number = 0
	index = 0
	while index < len(roman) :
		if roman_dict[roman[index]] < roman_dict[roman[index + 1]]:
			number += roman_dict[roman[index]] - roman_dict[roman[index + 1]]
			index += 1
		else:
			number += roman_dict[roman[index]]
		index += 1
	return number + roman_dict[roman[-1]]

print(solution("MCMXC"))