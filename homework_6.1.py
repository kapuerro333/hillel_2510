sentence = input("Write a sentence you like: ")
print(sentence)
symbols = len(sentence)
print(symbols)

unique_chars = set(sentence)
count_unique = len(unique_chars)
print("There are {} unique characters.".format(count_unique))