def race(v1, v2, g):
    l=[]
    x=v2-v1
    if v1>v2:
        return
    h=g//x
    m=(g/x-h)*60
    s=(m-int(m))*60
    if m>59:    
        h+=1
    if s>59:
        m+=1
        s=0
    
    
    l.append(int(h));l.append(int(m));l.append(int(s))
    return l