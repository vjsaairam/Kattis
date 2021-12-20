n=int(input())
k=0
sum=0
for i in range(1,n+1):
    m=int(input())
    while(m>0):
        l=m%10
        m//=10
        break
    k=m**l 
    sum+=k
print(sum)
