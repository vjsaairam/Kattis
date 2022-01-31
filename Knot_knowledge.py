num = input()

num1 = map(int,input().split())
num2 = map(int,input().split())

print((set(num1) - set(num2)).pop())
