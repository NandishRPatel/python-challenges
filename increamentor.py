def incrementer(nums):
	final_list = []
	for i in range(len(nums)):
		final_list.append(int(str(nums[i] + (i + 1))[-1:]))
	return final_list