n=int(input())
s=[]
for i in range(n):
    m=int(input())
    for j in range(m):
        l=list(input())
        if(l not in s):
            s.append(l)
    print(len(s))
    s.clear()
