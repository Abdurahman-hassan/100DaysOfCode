name_list = []
with open("./Input/Names/invited_names.txt") as Names:
    for name in Names.readlines():
        name_list.append(name.strip("\n"))

with open("./Input/Letters/starting_letter.txt") as file:
    content = file.read()

    for i in name_list:
        with open(f"./Output/ReadyToSend/txt_letter_for_{i}.txt", "w") as output_letter:
            output_letter.write(content.replace("[name]", i))

# another_way

# PLACEHOLDER = "[name]"
#
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_letter)

