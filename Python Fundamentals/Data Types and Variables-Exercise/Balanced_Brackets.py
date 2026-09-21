n = int(input())
last_bracket = ""
is_balanced = True

for i in range(n):
    line = input()

    if line == "(":
        if last_bracket == "(":
            is_balanced = False
        last_bracket = "("

    elif line == ")":
        if last_bracket != "(":
            is_balanced = False
        last_bracket = ")"

if last_bracket == "(":
    is_balanced = False

if is_balanced:
    print("BALANCED")

else:
    print("UNBALANCED")
