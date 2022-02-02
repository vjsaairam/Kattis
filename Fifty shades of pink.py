add=0
n = int(input())
for i in range(n):
    ot = input().lower()
    if 'pink' in ot or 'rose' in ot:add+=1
if add > 0:
    print(add)
else:
    print('I must watch Star Wars with my daughter')
