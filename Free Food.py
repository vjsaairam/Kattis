app =[]
n= int(input())
for i in range(n):
    day = input().split()
    d0 = int(day[0])
    d1 = int(day[1])
    for j in range(d0,d1+1):
        if j not in app:
            app.append(j)
    d0=0
    d1=0  
print(len(app))
