print('HI')
a=[]
for b in range(5):
    b=input('enter a value:')
    a.append(b)
c=input('again enter a value')
if c==b:
    b.remove(c[0])
print(a)
print(c)
