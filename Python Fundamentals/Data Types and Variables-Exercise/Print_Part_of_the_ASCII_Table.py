start_index = int(input())
end_index = int(input())

# Въртим цикъл от началния до крайния индекс (включително, затова + 1)
for i in range(start_index, end_index + 1):
    character = chr(i)
    # Отпечатваме символа и казваме на Python вместо нов ред да сложи интервал
    print(character, end=" ")