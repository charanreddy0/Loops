''' separation of list by str,int,float'''
b=[]
c=[]
d=[]
a=['a',10,20,'py',29.093,'python',9834.234]
for a in list(a):
    if isinstance(a,int):
        b.append(a)
    if isinstance(a,str):
        c.append(a)
    if isinstance(a,float):
        d.append(a)
print(b)
print(c)
print(d)
