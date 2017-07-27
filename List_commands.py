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
