n=float(input())*(5280/4854)
float_value=float('%.5f'%n)
round_value=str(round(float_value,3))
point=round_value[::-1].find('.')
print(round(float(round_value)*(10**point)))