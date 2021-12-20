x = input().split(";")
count = 0

for y in x:
    
    if ('-' in y):
        tmp = list(map(int, y.split("-")))
        count += tmp[1]-tmp[0]+1
    else:
        count += 1

print (count)
