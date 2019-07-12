import math
def spider_to_fly(spider, fly):
	if spider == fly: return 0
	elif spider[0] == fly[0]: return abs(int(spider[-1]) - int(fly[-1]))
	elif spider[-1] == fly[-1]: return 2 * abs(ord(spider[0]) - ord(fly[0]))
    else:
    	a = int(spider[-1])
    	b = int(fly[-1])
    	theta = abs(a - b) * 45