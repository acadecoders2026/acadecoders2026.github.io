import random

file = open('words.txt', 'r')


### this function must return a list of 10 random words, all captialized.
### it doesnt quite work yet...
def generate_words():
    random_words = []
    for i in range(11):
        #choose a random word
        all_the_words = file.readlines(300000)
        word = all_the_words[random.randint(0,6)]

        #add that word to the list
        random_words.append(word.strip())


    return random_words

    random_words = random_words.upper()


print(generate_words())
