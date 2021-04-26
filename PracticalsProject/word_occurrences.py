word = input("Enter a sentence:")
words = word.split()
word_dict = {}
for w in words:
    if w not in word_dict:
        word_dict[w] = 1
    else:
        word_dict[w] = word_dict[w] + 1

print(word_dict)
