n=int(input())
a=[]
s=[]
sum=0
for i in range(1):
    m=input().split()
    for i in range(len(m)):
        if (int(m[i])!=-1):
            s.append(m[i])
    for z in range(len(s)):
        sum+=int(s[z])
        delo=sum/len(s)
    print(delo)
