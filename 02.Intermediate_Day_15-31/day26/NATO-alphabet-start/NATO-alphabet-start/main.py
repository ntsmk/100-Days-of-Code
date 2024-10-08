student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    print(row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = data.to_dict()
df = pandas.DataFrame(data_dict)
new_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(new_dict)

# for index, row in df.iterrows():
#     print(f"{row["letter"]}:{row["code"]}")

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
# input_list = [letter.upper() for letter in user_input]
# print(input_list)
# answer_list = [word for word in new_dict.items() if ]
# print(answer_list)
thislist = [new_dict[letter] for letter in user_input]
# for i in input_list:
#     thislist.append(new_dict[i])
print(thislist)