unique = []
for i in range(10):
    x = int(input())
    if (x%42 not in unique):
        unique.append(x%42)
print(len(unique))
