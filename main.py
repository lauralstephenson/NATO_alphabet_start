#Replace letters in a word with the Nato alphabet using a dictionary
#Using a Pandas dataframe
#Day 30: Updating the file using error handling to prevent user error
import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv(r".\nato_phonetic_alphabet.csv", encoding="UTF-8")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#Test
#print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#Also, we're creating a try block to prevent user error

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        # Iterate over the words, with the code words behind a colon
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()