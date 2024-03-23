import pandas

#Read the nato alphabet file, save as data
data = pandas.read_csv("nato_alpha.csv")

#print data to a dictionary
print(data.to_dict())

#New dictionary saving the letters as the key and the phonetic code as the value 
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#Ask user for a word
users_word = input("Pick a word: ").upper()

#List comprehension to produce the phonetic spelling of the word
users_word_phonetics = [phonetic_dict[letter] for letter in users_word]

#Print the phonetic spelling of the word inputted
print(users_word_phonetics)