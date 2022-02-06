l,r=map(int,input().split())
if(l==r==0):
    print('Not a moose')
elif(l==r):
    total = 2*l
    print('Even',total)
else:
    total = max(l,r)* 2
    print('Odd',total)
