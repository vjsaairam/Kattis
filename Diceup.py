n=input().split()
n0=int(n[0])
n1=int(n[1])
if(n0==n1):
    sum1=n0+1
    print(sum1)
elif(n0>n1):
    for i in range(n1+1,n0+2):
        print(i)
else:
    for i in range(n0+1,n1+2):
        print(i)
