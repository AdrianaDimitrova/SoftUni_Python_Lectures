year = int(input())

while True:
    year += 1
    years_as_string = str(year)
    unique_digits = set(years_as_string)

    if len(years_as_string) == len(unique_digits):
        print(year)
        break


