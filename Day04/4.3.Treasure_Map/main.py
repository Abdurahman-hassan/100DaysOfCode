row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row_index = position[0]
colm_index = position[1]

map[int(colm_index)-1][int(row_index)-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
