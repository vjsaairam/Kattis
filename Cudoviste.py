rows, columns = list(map(int, input().split()))
map_rows = []
crush0 = 0
crush1 = 0
crush2 = 0
crush3 = 0
crush4 = 0
for _ in range(rows):
    map_rows.append(input())
for col in range(columns - 1):
    for row in range(rows - 1):
        chars = map_rows[row][col:col+2] + map_rows[row+1][col:col+2]
        if '#' in chars:
            continue
        x_count = 0
        for char in chars:
            if 'X' == char:
                x_count += 1
        if x_count == 0:
            crush0 += 1
        elif x_count == 1:
            crush1 += 1
        elif x_count == 2:
            crush2 += 1
        elif x_count == 3:
            crush3 += 1
        else:
            crush4 += 1
print(f"{crush0}\n{crush1}\n{crush2}\n{crush3}\n{crush4}")
