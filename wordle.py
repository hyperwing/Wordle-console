import urllib.request
import random  
from termcolor import colored
import os

def get_words():

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    req = urllib.request.Request(word_url, headers=headers)

    response = urllib.request.urlopen(req)
    long_txt = response.read().decode()
    return(long_txt.splitlines())


def main():
    #get words
    try:
        words = get_words()
        os.system('color')
    except e:
        print("failed getting word list")

    print("welcome to the game: dont forget, no plurals")

    win_count = 0
    lose_count = 0
    hint_count = 0

    proper_noun_flag = False
    if input("enable proper nouns? y|n: \n").lower == "y":
        proper_noun_flag = True

    continue_game = True
    while continue_game:
        # word_length = int(input("enter how many letters word should be"))
        word_length = 5

        #choose a word
        chosen_word = "a"
        if not proper_noun_flag :

            while len(chosen_word) != word_length and chosen_word[0].isupper:
                chosen_word = random.choice(words)
                # print(random.choice(words))
        else:
            while len(chosen_word) != word_length:
                chosen_word = random.choice(words)
            
        chosen_word = chosen_word.lower()
        # print(chosen_word)

        #game loop
        chances = 5 #chances to guess word
        solution = list(chosen_word)
        current_guess = ["*"] *5 # TODO actually store all correct letters
        print(current_guess)
        for i in range(chances):


            guess = input("-h for a hint\n").lower()

            if guess == "-h":
                print(random.choice(chosen_word))
                guess = input("").lower()
                hint_count +=1

            while not verify_guess(guess, solution, words):
                guess = input("Guess must be " +str(word_length) +" characters long and a real word, enter a new one:\n")
            
            if list(guess) == solution:
                win_count +=1
                print(colored(guess, "green"))
                print("solved!")
                break

            print(color_guess(guess, solution))

        if (list(guess) != solution):
            lose_count +=1
            print("sorry, you didnt get it: " + str(solution))
            

        print("Wins: " + str(win_count) +"\nLosses: " + str(lose_count) + "\nHints used this session: " +  str(hint_count))
        if input("play again? Y|N:\n").upper() != "Y":
            continue_game = False

def verify_guess(guess, solution, words):
    #should be same length and a real word

    return len(guess) == len(solution) and (guess in words or guess.capitalize() in words)


def color_guess(guess, solution):
    final = ""
    guessCount = ""

    for i in range(len(guess)):
        if guess[i] == solution[i]:
            final += colored(guess[i], "green")
        elif guess[i] in solution:
            if guess[i] in guessCount:
                if solution.count(guess[i]) - 1 >= guess.count(guess[i]):
                    final += colored(guess[i], "yellow")
                else:
                    final += colored(guess[i], "red")
            else:
                if solution.count(guess[i]) >= guess.count(guess[i]):
                    final += colored(guess[i], "yellow")
                else:
                    final += colored(guess[i], "red")
        else:
            final += colored(guess[i], "red")

        guessCount+= guess[i]
    return final
if __name__ == "__main__":
    main()