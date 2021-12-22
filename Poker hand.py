arr = [w[0] for w in list(input().split(' '))]
total = 1
for i in range(5):
    counts = arr.count(arr[i])
    total = counts if counts>total else total
print (total)
