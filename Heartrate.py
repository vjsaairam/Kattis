n=int(input())
for i in range(n):
    m=input().split()
    b=int(m[0])
    p=float(m[1])
    bpm = 60*b/p 
    var = 60/p 
    print((format(bpm-var,".4f")),(format(bpm,".4f")),(format(bpm+var,".4f")))
