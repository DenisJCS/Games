name = "Twiggy"
leaves = 0
for day in range(3):
  leaves += 1
  if leaves == 3:
    print(name, "is a seedling!")

print("Leaves:", leaves)
display_simulation()



leaves = 3
light = 1
water = 1

for day in range(3):
  leaves += light
  leaves += water
  if leaves > 8:
    leaves += 2
    print("Growth spurt!")

print("Leaves:", leaves)
display_simulation()


# Output
Growth spurt!
Leaves: 11
       🌿🌿🌿
     🌿🌿🌿🌿🌿
      🌿🌿🌿⟋
       (^_^)
        | |
        | |


"""Day two on brilliant """
leaves = 11
water = 1
daily_weather = ["☀️", "☁️", "☀️"]

for day in daily_weather: 
  if day == "☀️": 
    light = 2
  else:
    light = 1
  leaves += light + water

print("Leaves:", leaves)
display_simulation()
