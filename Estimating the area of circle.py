from math import pi 

while(True):
    r,m,c= map(float,input().split())    
    if(r==0):
        break
    else:
        print(pi*r**2, (2*r)**2* c/m)
