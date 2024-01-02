row1 = ["🫸", "🫸", "🫸"]
row2 = ["🫸", "🫸", "🫸"]
row3 = ["🫸", "🫸", "🫸"]

map = [row1, row2, row3]

print(f" {row1}\n {row2}\n {row3}")

treasure_position = input("Where do you want to put your treasure?")

horizontal = int(treasure_position[0])
vertival =int(treasure_position[1])

selected_area = map[vertival-1]
selected_area[horizontal -1] = "X"

print(f" {row1}\n {row2}\n {row3}")