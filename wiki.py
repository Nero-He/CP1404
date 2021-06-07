import wikipedia


def main():
    key_word = input('Please type in what you want to search: ')
    while key_word != " ":
        try:
            wikipedia.search(key_word)
            wikipedia.summary(key_word)
        except wikipedia.DisambiguationError:
            return "Error"


main()
