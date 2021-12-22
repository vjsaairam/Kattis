best = -1;
place = -1;
for i in range (1,6):
    array = input().split(' ')
    total = 0
    for char in array:
        total += int(char)

    if(total>best):
        best = total
        place = i

print(place, best)
