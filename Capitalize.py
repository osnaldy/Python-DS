def capitalize(string):

    a = [i.capitalize() for i in string.split(" ")]
    return " ".join(a)

word = input("Enter the sentence")
print(capitalize(word))