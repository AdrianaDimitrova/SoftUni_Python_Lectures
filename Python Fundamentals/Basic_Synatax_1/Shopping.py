budget = int(input())
command = input()

while command != "End":
    product_price = int(command)

    if budget < product_price:
        print("You went in overdraft!")
        break

    else:
        budget-=product_price
        command = input()


else:
    print("You bought everything needed.")


