map1 = ["🫸", "🫸", "🫸"]
map2 = ["🫸", "🫸", "🫸"]
map3 = ["🫸", "🫸", "🫸"]
new_map = [map1, map2, map3]
print(f"{map1}\n{map2}\n{map3}")

treasure_position = input("Where do you want to put the treasure?")

horizontal = int(treasure_position[0])
vertical = int(treasure_position[1])


selected_area =new_map[vertical-1]
selected_area[horizontal -1] = "X"

print(f"{map1}\n{map2}\n{map3}")