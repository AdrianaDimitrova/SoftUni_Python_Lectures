num = input()
digit_list = list(num)

digit_list.sort(reverse=True)

largest_number = "".join(digit_list)

print(largest_number)