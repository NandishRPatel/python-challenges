from math import gcd
def convertFracts(lst):
    denom = []
    num = []
    final_list = []
    final_denom = 0 
    if lst == []: return []
    else:
    	for lsts in lst:
    		num.append(lsts[0])
    		denom.append(lsts[-1])

    final_denom = denom[0]
    for i in denom[1:]:
        final_denom = int(final_denom*i/gcd(final_denom,i))

    for i in range(0,len(num)):
        final_list.append([num[i] * int(final_denom/denom[i]), final_denom])
    
    return final_list

print(convertFracts([[1, 2], [1, 3], [1, 4]]))

#[[90390, 170300], [11310, 170300], [127725, 170300]] should equal [[18078, 34060], [2262, 34060], [25545, 34060]]