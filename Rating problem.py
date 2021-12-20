jud,vote= input().split() 
jud=int(jud)
vote=int(vote)
sum=0.0
cval = 3*(jud-vote)
for i in range(0,vote):
    sum+=int(input())
    
print((sum - cval) / jud, (sum + cval) / jud)
