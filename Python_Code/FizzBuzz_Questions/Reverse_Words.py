string_of_words = "Bo likes cats"

list_of_words = []
list_of_words = string_of_words.split(" ")


reversed_wording = ""
length_of_words_list = len(list_of_words)
while length_of_words_list !=0:
    length_of_words_list -= 1
    reversed_wording = reversed_wording + list_of_words[length_of_words_list] + " "


print(f"Original  :{string_of_words}")
print(f"Reverse   :{reversed_wording}")