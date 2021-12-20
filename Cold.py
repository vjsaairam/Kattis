n=int(input())
m=[]
a=[]
sum=0
for i in range(1):
    m=input().split()
    for i in range(len(m)):
        if(int(m[i])<0):
            a=[i]
            sum+=int(len(a))
    print(sum)
