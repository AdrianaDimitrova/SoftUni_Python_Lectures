string1 = input()
string2 = input()

for i in range(len(string1)):
    current_string = ""

    for j in range(i+1):
        current_string += string2[j]

    for j in range(i+1, len(string1)):
        current_string += string1[j]

    if current_string != string1:
        print(current_string)
        string1 = current_string
