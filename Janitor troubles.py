a, b, c, d = map(int, input().split())
s = (a + b + c + d) / 2 
area = ((s - a) * (s - b) * (s - c) * (s - d)) ** 0.5
print(area)
