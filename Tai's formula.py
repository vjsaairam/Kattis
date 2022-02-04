repetitions = int(input())
side1 = list(map(float,input().split(' ')))
total=0

for i in range(repetitions-1):
    side2 =list(map(float,input().split(' ')))
    total+= ((side1[1]+side2[1])/2)*(side2[0]-side1[0])/1000
    side1=side2;
print(total)
