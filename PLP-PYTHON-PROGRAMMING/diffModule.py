# using the difflib to find nearest match
import difflib as dff

words = ["apple", "melon", "orange", "ovacado", "pineapple", "banana", "app", "apply"]
def closest_match(word):
    if type(word) == str:
        closest_match = dff.get_close_matches(word, words, n=3, cutoff=0.6)
        print("Did you mean any of these words : ")
        for i in range(len(closest_match)):
            print(f"{i + 1} : {closest_match[i]}")    
        number = int(input("Enter the position : "))
        print("Your favourite fruit is {}".format(closest_match[number - 1]))
    else:
        print("Wrong input, enter only string or characters : ")   

user_word = input("Enter the name of your favorite fruit : ")
closest_match(user_word)