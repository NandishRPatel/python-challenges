import collections
def meeting(s):
    final_string = ""
    s = s.upper()
    temp_dict = {}
    for i in s.split(";"):
    	f_name, l_name = i.split(":")
    	#print(f_name,l_name)
    	if l_name in temp_dict:
    		temp_dict[l_name].append(f_name)
    	else:
    		temp_dict[l_name] = [f_name]
    temp_dict = collections.OrderedDict(sorted(temp_dict.items()))
    #print(temp_dict)
    for key,value in temp_dict.items():
    	if len(value) > 1:
    		for i in sorted(value):
    			final_string += "(" + key + ", " + i + ")"
    	else:
    		final_string += "(" + key + ", " + value[0] + ")"
    return final_string

print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))