# You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
a=[1,2,3,4,5,6,7,8,9,10]
for a in list(a):
    print(a*a,end=' ')
print("\n")
# it s with infinite loop u can enter n numbers  
a=[]
d=1
while d==1:
    b=int(input("enter a value:"))
    a.append(b)
    c=b*b
    print(c)
