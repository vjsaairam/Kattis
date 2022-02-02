a1 =[]
a2 = []
for _ in range(int(input())):
    st1 = list(input())
    st2 = list(input())
    for i in range(len(st1)):
        if (st1[i] == st2[i]):
            a1.append('.')
            
        else:
            a1.append('*')
            
    print(''.join(st1))
    print(''.join(st2))
    print(''.join(a1))
    print('\n')
    a1.clear()
