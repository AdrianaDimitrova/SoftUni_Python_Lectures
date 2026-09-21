n = int(input())
water_in_tank = 0
capacity = 255

for i in range(n):
    liters = int(input())

    if water_in_tank+liters > capacity:
        print("Insufficient capacity!")

    else:
        water_in_tank += liters

print(f"{water_in_tank}")