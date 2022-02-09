import math

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ '")
dist = 30*math.pi/14

def smallestDist (x, y):
    z=abs(alphabet.index(x)-alphabet.index(y))
    return z if z<28-z else 28-z
    

for i in range(int(input())):
    time=0.0
    string = input()
    for j in range(len(string)-1):
        time+= 1 + smallestDist(string[j],string[j+1])*dist/15

    print(time+1)
