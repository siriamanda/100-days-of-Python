import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# with open("nato_phonetic_alphabet.csv") as nato_phonetic_alphabet:
#    nato_phonetic_alphabet_df = pandas.DataFrame(nato_phonetic_alphabet)

nato_phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet_df.iterrows()}
# print(nato_phonetic_alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# output_list = []
# for x in input_letters:
#     phonetic_code = [code for (letter, code) in nato_phonetic_alphabet_dict.items() if letter == x]
#     output_list.append(phonetic_code)

# Shorter solution
def generate_phonetic():
    user_input = input("Enter a word: ")
    input_letters = [letter.upper() for letter in user_input]
    try:
        output_list = [nato_phonetic_alphabet_dict[letter] for letter in input_letters]
    except KeyError:
        print("Sorry, only letters from the alphabet please")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()


