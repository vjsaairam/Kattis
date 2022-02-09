import string


for i in range(0,int(input())):
    x = input().lower()
    output = [y for y in string.ascii_lowercase if y not in x]
    print("pangram" if len(output)==0 else "missing {}".format(''.join(output)))
