n=int(input())
l=1
sum=0
for i in range(0,n):
    m=int(input())
    for j in range(1,m+1):
        l=l*j 
    sum=l+0
    sum%=10
    l=1
    print(sum)
