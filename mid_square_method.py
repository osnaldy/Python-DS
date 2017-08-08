number = 44**2

value = [int(x) for x in str(number)]

value = value[1:3]

y = [str(t) for t in value]
print(int(''.join(y)))