def sum_of_intervals(intervals):
	final_list = []
	for interval in intervals:
		start,end = interval
		final_list.extend(range(start,end))
	return len(set(final_list))

print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))