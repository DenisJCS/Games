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
