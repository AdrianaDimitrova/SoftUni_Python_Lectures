orders = int(input())
grand_total = 0

for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    total = price_per_capsule * days * capsules_per_day

    print(f"The price for the coffee is: ${total:.2f}")

    grand_total += total

print(f"Total: ${grand_total:.2f}")
