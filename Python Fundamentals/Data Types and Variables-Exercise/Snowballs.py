snowballs = int(input())
max_value = 0
max_weight = ""
max_time = ""
max_quality = ""

for i in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    current_value = (weight//time) ** quality

    if current_value > max_value:
        max_value = current_value
        max_weight = weight
        max_time = time
        max_quality = quality

print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")
