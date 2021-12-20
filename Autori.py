import sys
input= str(sys.stdin.readline())
print(input[0], end= "")
for i in range(len(input)):
    if input[i] == "-":
        print(input[i+1], end= "")
