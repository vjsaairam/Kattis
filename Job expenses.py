n = int(input())
t = input().split()

total = 0
for i in t:
    i = int(i)
    if i < 0:
        total += -i

print(total)
