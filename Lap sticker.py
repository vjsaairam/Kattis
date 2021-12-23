margin = 1
wc, hc, ws, hs = list(map(int, input().split()))
horizontal = margin + ws + margin <= wc
Vertical = margin + hs + margin <= hc
willFit = horizontal and Vertical
if willFit:
    print(1)
else:
    print(0)
    
    
