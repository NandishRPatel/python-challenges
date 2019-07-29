def sequence(p):
	p=p.upper()
	number=[1,2,3,4,5,6,7,8,9,0]
	alphabets=['1','ABC2','DEF3','GHI4','JKL5','MNO6','PQRS7','TUV8','WXYZ9',' 0']
	messege=''
	prev=''
	for i in p:
		if i=='#' or i=='*':
			messege+=i
		else:
			for x in alphabets:
				if i in x:
					count=x.index(i)+1
					x_messege=(count*str(number[alphabets.index(x)]))
					if prev==x_messege[0]:messege+=('p'+x_messege)
					else:messege+=x_messege
		prev=messege[-1]
	return messege