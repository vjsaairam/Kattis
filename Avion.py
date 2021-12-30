n = []
for _ in range(5):
    n.append(input())

found = False
for i in range(5):
    if "FBI" in n[i]:
        print(i + 1, end=' ')
        found = True

if not found:
    print("HE GOT AWAY!")
