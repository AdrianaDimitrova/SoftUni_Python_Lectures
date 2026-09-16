budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25

milk_price_needed = milk_price / 4

one_bread_price = flour_price + eggs_price + milk_price_needed

loaves_count = 0
eggs_count = 0

while budget >= one_bread_price:
    budget -= one_bread_price
    loaves_count += 1
    eggs_count += 3

    if loaves_count % 3 == 0:
        eggs_count -= (loaves_count-2)

print(f"You made {loaves_count} loaves of Easter bread! Now you have {eggs_count} eggs and {budget:.2f}BGN left.")