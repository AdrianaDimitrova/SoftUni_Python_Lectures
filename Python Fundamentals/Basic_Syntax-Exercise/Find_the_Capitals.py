text = input()
capitals_indices = []

for i in range(len(text)):
    if text[i].isupper():
        capitals_indices.append(i)

print(capitals_indices)

