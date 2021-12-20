start, end, _ = map(int, input().split())
walk = list(map(int, input().split()))
bus = list(map(int, input().split()))
interval = list(map(int, input().split()))

for i in range(len(walk)):
    # Time taken on a bus
    if i != 0:
        start += bus[i - 1]
    # Time to walk to the next station
    start += walk[i]
    # Time to wait for the bus
    if i != len(walk) - 1 and start % interval[i] != 0:
        start += interval[i] - start % interval[i]

print("yes" if start <= end else "no")
