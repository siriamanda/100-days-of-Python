# Get a hold of names for invitation

with open("./Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()

# Create list with cleaned names

stripped_names = []

for name in range(len(name_list)):
    stripped_name = name_list[name].strip("\n")
    stripped_names.append(stripped_name)

# print(stripped_names)

with open("./Input/Letters/starting_letter.txt", "r") as starting_letter_file:
    starting_letter = starting_letter_file.read()

# print(starting_letter)
    for invitee in range(len(stripped_names)):
        name = stripped_names[invitee]
        new_letter = starting_letter.replace("[name]", name)
        with open(f".Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
