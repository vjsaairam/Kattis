arr = list(map(int,input().split(' '))) 
money = arr[0]*3 + arr[1]*2 + arr[2]

vic = "Province" if money>=8 else "Duchy" if money>=5 else "Estate"
tres = "Gold" if money>=6 else "Silver" if money>=3 else "Copper"

print("{} or {}".format(vic,tres) if money>=2 else tres)
