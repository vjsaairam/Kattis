for i in range(int(input())):
    numbs = list(map(int,input().split(' ')))

    if(numbs[0]+numbs[1]==numbs[2] or numbs[0]*numbs[1]==numbs[2] or numbs[0]-numbs[1]==numbs[2] or numbs[1]-numbs[0]==numbs[2] or numbs[0]/numbs[1]==numbs[2] or numbs[1]/numbs[0]==numbs[2]):
        print("Possible")
    else:
        print("Impossible")
