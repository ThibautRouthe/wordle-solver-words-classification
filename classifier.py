import json
import os

words_list_file = 'words_alpha.txt'
words_by_length_file = 'words_by_length.json'
words_by_letters_folder = 'words_by_letters'

words_by_length = {}
words_by_letters = {}

words = []
with open(words_list_file,'r') as f:
    words = f.read().splitlines()
    for index_word, word in enumerate(words):

        word_length = len(word)
        if word_length not in words_by_length:
            words_by_length[word_length] = []
        words_by_length[word_length].append(index_word)

        for index_character, character in enumerate(word):
            if character != '\n':
                if character not in words_by_letters:
                    words_by_letters[character] = {}
                if index_word not in words_by_letters[character]:
                    words_by_letters[character][index_word] = []

                words_by_letters[character][index_word].append(index_character)

with open(words_by_length_file,'w',encoding='utf-8') as f:
    f.write(json.dumps(words_by_length))

for letter in words_by_letters.keys() :
    file_name = f'letter_{letter}.json'
    print(file_name)
    words_by_letter_file = os.path.join(words_by_letters_folder,file_name)
    with open(words_by_letter_file,'w+',encoding='utf-8') as f:
        f.write(json.dumps(words_by_letters[letter]))