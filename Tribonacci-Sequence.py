def tribonacci(s,n):
	y=3
	x=0
	if n==0:
		return []
	elif y>n:
		return s[:n]
	else:
		while y<n:
			a=s[x]
			b=s[x+1]
			c=s[x+2]
			s.append(a+b+c)
			x+=1;y+=1
	return s