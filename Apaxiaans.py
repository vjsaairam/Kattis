import sys
testInput= str(sys.stdin.readline())
newOutput= ""
for i in range(len(testInput)-1):
    if testInput[i] != testInput[i+1]:

        newOutput+= testInput[i]

print(newOutput)
