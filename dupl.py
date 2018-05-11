n=int(input())
l=[]
for i in range(0,n):
    b=int(input())
    l.append(b)
n=set()
for i in l:
    if l.count(i)>1:
        n.add(i)
m=[]
for i in n:
    m.append(i)
sorted(m)
for i in m:
    print(i)
