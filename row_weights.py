def row_weights(array):
    if len(array) == 1:
    	return (array[0],0)
    else:
    	index = 0
    	team_1 = 0
    	team_2 = 0
    	while index < len(array):
    		if index % 2 == 0 :team_1 += array[index]
    		else:team_2 += array[index]
    		index += 1
    	return (team_1, team_2)

print(row_weights([0,1,0]))