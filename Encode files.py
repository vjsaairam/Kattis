import math
for i in range(int(input())):
    message = input()
    lenMess = int(math.sqrt(len(message)))
    

    for x in range(lenMess-1,-1,-1):
        print(message[x::lenMess],end='\n' if x==0 else '')
