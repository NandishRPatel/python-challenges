def sum_of_intervals(intervals):
	final_list = []
	for interval in intervals:
		start,end = interval
		final_list.extend(list(range(start,end)))
	return len(set(final_list))

print(sum_of_intervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ))