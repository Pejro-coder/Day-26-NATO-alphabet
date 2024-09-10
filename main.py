student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_dataframe = pandas.DataFrame(nato_data)
# print(nato_data)
# print(nato_data_dataframe)

nato_dict = {row.letter: row.code for (index, row) in nato_data_dataframe.iterrows()}
print(nato_dict)
name = input("Name for NATO conversion: ").upper()
nato_words = [nato_dict.get(key) for (key, value) in nato_dict.items() if key in name]

# nato_words = [nato_dict.get(letter) for letter in name]
print(nato_words)
# for a in name:
#     print(nato_dict.get(a))


#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

