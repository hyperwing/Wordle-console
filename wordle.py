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
    words = get_words()
    os.system('color')

    win_count = 0
    lose_count = 0

    continue_game = True
    while continue_game:
        # word_length = int(input("enter how many letters word should be"))
        word_length = 5

        #choose a word
        chosen_word = ""
        while len(chosen_word) != word_length:
            chosen_word = random.choice(words)
            # print(random.choice(words))
        chosen_word = chosen_word.lower()
        # print(chosen_word)

        #game loop
        chances = 5 #chances to guess word
        solution = list(chosen_word)
        current_guess = ["*"] *5
        print(current_guess)
        for i in range(chances):


            guess = input("").lower()

            while not verify_guess(guess, solution, words):
                guess = input("invalid guess, enter a new one:\n")
            
            if list(guess) == solution:
                win_count +=1
                print(colored(guess, "green"))
                print("solved!")
                break

            print(color_guess(guess, solution))

        if (list(guess) != solution):
            lose_count +=1
            print("sorry, you didnt get it: " + str(solution))
            

        print("Wins: " + str(win_count) +"\nLosses: " + str(lose_count))
        if input("play again? Y|N:\n").upper() != "Y":
            continue_game = False

def verify_guess(guess, solution, words):
    #should be same length and a real word
    return len(guess) == len(solution) and guess in words


def color_guess(guess, solution):
    final = ""
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            final += colored(guess[i], "green")
        elif guess[i] in solution:
            if solution.count(guess[i]) >= guess.count(guess[i]):
                final += colored(guess[i], "yellow")
            else:
                final += colored(guess[i], "red")
        else:
            final += colored(guess[i], "red")
    return final
if __name__ == "__main__":
    main()