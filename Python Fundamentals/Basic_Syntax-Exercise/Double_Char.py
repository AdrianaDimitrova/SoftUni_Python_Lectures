word = input()

while word != "End":

    if word == "SoftUni":
        word = input()
        continue

    doubled_string = ""

    for char in word:
        doubled_string += char *2

    print(doubled_string)

    word = input()


