key = int(input())
rows = int(input())
decrypted_message = ""

for i in range(rows):
    char = input()
    code = ord(char)
    new_code = code + key
    new_char = chr(new_code)
    decrypted_message += new_char

print(decrypted_message)
