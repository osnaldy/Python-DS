n = int(input("Enter the number of operations "))
l = []
for _ in range(n):

    perform = str(input("Enter the expression to perform "))
    s = perform.split()
    key_word = s[0]
    operation = s[1:]

    if key_word != "print":
        key_word += "(" + ",".join(operation) + ")"
        eval("l."+key_word)
    else:

        print(l)

x = int(input())
y = int(input())
z = int(input())
num = int(input())
ar = []
p = 0

print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n ])

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != num:
                ar.append([])
                ar[p] = [i, j, k]
                p += 1
print(ar)
