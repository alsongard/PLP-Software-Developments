import difflib as dif
import json

# load the json data
with open("./data/data.json") as file:
    data_dict = json.load(file)

print(type(data_dict))
# method 1 : retrieving key values
# key_values = data_dict.keys()
# print(len(key_values))

# method 2 : retrieving key values using list
key_values = [key for key in data_dict.keys()]
# i = 0
# while i < 20:
#     print(key_values[i])
#     i += 1
# print("The lenght of the keys in the data_dict is {}".format(len(key_values)))
def get_definition(word):
    if type(word) == str:
        #convert the work in small letter
        word = word.lower()
        if word in data_dict:
            return data_dict[word]
        close_word_matches = dif.get_close_matches(word, key_values, n=2, cutoff=0.6)
        if close_word_matches:
            print("Did you mean any of these words : ")
            for i in range(len(close_word_matches)):
                print(f"{i} : {close_word_matches[i]}")
            print("if so enter position of the word : ")
            number = int(input("Enter the position : "))
            return data_dict[close_word_matches[number]]
        else:
            return "Word not found"
    else:
        return "Enter only string or letters"

user_word = input("Enter any word that comes in mind : ")
answer = get_definition(user_word)
print(answer)