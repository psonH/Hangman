import random

print("----------WELCOME TO HANGMAN----------")
wordlist=[]    #to store all the words from the file
state=True
#reading and writing words into the 'wordlist' list
with open('sowpods.txt','r') as open_file:
    line = open_file.readline()
    while line:
        word = line.split()
        wordlist.append(word)
        line = open_file.readline()

chances = 6
while state == True:
    word = random.choice(wordlist)      #returns a list with a single item
    word = ''.join(map(str,word))       #converting the word to a string
    word_list = list(word)              #making a list out of the word; hence word_list contains each character of the word
    ans_list = ['_'] * len(word_list)   #ans_list will contain the guessed word,if correct.
    guess = ' '.join(map(str, ans_list))
    print(guess)

    chances = 6
    while ('_' in guess) and (chances != 0):
        letter = input("Guess the letter:")
        if letter in word_list:
            #looping to make sure occurances of the letter guessed right is displayed
            while True:
                index = word_list.index(letter)
                ans_list[index] = letter               # adding the guessed letter to the answer list
                word_list[index] = '_'                 # removing the guessed letter from the actual word list
                guess = ' '.join(map(str, ans_list))
                if letter in word_list:
                    continue
                else:
                    break
            print(guess)
        else:
            print("-------------------")
            print("Incorrect guess !!")
            chances = chances -1
            print("Chances left:",chances)
    if '_' in guess:
        print("-------------------")
        print("You Lost !!! You're out of chances !!!")
        print("Correct answer:",word)
    else:
        print("Yay !!!! You Won !!!")
    choice=input("Do you wish to continue? [yes/no]:")
    if choice == "no":
        state = False

