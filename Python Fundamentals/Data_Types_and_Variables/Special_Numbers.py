number = int(input())

for i in range(1, number+1):

    number_as_string = str(i)
    digits_sum = 0

    for digit in number_as_string:
        digits_sum+= int(digit)

        if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
            print(f"{i} -> True")

        else:
            print(f"{i} -> False")