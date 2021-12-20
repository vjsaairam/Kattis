n=int(input())
list=[]
for i in range(n):
    a=input()
    list.append(a)
for i in range(0,n):
    if (i%2==0):
        print(list[i])
