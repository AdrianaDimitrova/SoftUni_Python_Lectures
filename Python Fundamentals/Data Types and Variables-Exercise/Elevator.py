people = int(input())
capacity = int(input())

courses = people // capacity
other_people = people % capacity

if other_people > 0:
    courses += 1

print(f"{courses}")