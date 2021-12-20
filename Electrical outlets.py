n=int(input())
sum=0
wel=[]
for i in range(1,n+1):
    m=input().split()
    for i in range(1,len(m)):
        sum+=int(m[i])
        hel=sum-(len(m)-2)
    print(hel)
    sum=0
