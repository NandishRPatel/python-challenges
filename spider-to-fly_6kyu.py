import math
def spider_to_fly(spider, fly):
	if spider == fly: return 0
	elif spider[0] == fly[0]: return abs(int(spider[-1]) - int(fly[-1]))
	else:
		a = int(spider[-1])
		b = int(fly[-1])
		theta = abs(ord(spider[0]) - ord(fly[0])) * 45
		if theta == 180: 
			if a == b: return 2 * abs(ord(spider[0]) - ord(fly[0]))
			else: return 2 * abs(ord(spider[0]) - ord(fly[0])) - abs(a - b)
		else: return math.sqrt(a ** 2 + b ** 2 - (2 * a * b * math.cos(math.radians(theta))))


print(spider_to_fly("C4", "H2"))