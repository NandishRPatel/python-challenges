import math
def spider_to_fly(spider, fly):
	a = int(spider[-1])
	b = int(fly[-1])
	theta = abs(ord(spider[0]) - ord(fly[0])) * 45
	return math.sqrt(a ** 2 + b ** 2 - (2 * a * b * math.cos(math.radians(theta))))


print(spider_to_fly("C4", "H2"))