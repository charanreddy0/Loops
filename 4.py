#Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.
b=[]
c=[]
for a in range(1,101):
    if a%2==0:
        b.append(a)
    else:
            c.append(a)
print(c)
print(b)
