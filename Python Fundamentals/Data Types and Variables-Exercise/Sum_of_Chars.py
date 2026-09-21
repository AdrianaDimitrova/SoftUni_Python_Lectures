rows = int(input())
total_sum = 0

for i in range(rows):
    char = input()
    new_char = ord(char)
    total_sum += new_char

print(f"The sum equals: {total_sum}")