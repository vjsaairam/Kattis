temp=0
i=1
j=0
n=int(input())
while(temp<n):
    temp+=i*i
    i+=2
    j+=1 
if(temp>n):
    j-=1
print(j)