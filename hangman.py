import random
"""This game plays hangman with the user."""
class Hangman:

    def __init__(self):
        self.hidden_word = self.find_word()
        self.blank_string = "-" * len(self.hidden_word)
        self.lives = 6

        #For debugging only ;)
        print(self.hidden_word)
        print(self.blank_string)

    def process_guess(self, guess):
        if guess != hidden_word:
            lives = int(lives) - 1
            draw_hangman(lives)
        else:
            blank_string = "uffh"
        print(blank_string)

    def find_word(self):
        #This method is complete
        dictionary = open('/usr/share/dict/words','r')
        words = list(dictionary)
        return random.choice(words).lower().strip()

    def draw_hangman(self, lives):
        if lives == 6:
            print("=========\n ||     |\n ||\n ||\n ||\n ||\n/  \\")
        elif lives == 5:
            print("=========\n ||     |\n ||     O\n ||\n ||\n ||\n/  \\")
        elif lives == 4:
            print ("=========\n ||     |\n ||     O\n ||     |\n ||\n ||\n/  \\")
        elif lives == 3:
            print ("=========\n ||     |\n ||    \O\n ||     |\n ||\n ||\n/  \\")
        elif lives == 2:
            print("=========\n ||     |\n ||    \O/\n ||     |\n ||\n ||\n/  \\")
        elif lives == 1:
            print ("=========\n ||     |\n ||    \O/\n ||     |\n ||    /\n ||\n/  \\")
        elif lives == 0:
            print ("=========\n ||     |\n ||     O \n ||    /|\\\n ||    / \\\n ||\n/  \\")

    def won_game(self):
        pass #Your code here (thios should be called from play)

    def play(self):
        print("Guess the word")
        print(game.blank_string)
        guess = input()
        game.process_guess(guess)



if __name__ == "__main__":
    game = Hangman()
    game.play()
