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
        char = guess
        if char in self.hidden_word:
            x = int(self.hidden_word.index(char))
            return (self.blank_string[:x] + char + self.blank_string[x+1:])
        if char not in self.hidden_word:
            return self.draw_hangman(self.lives - 1)

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
        while self.lives > 0:
            self.process_guess(self.guess)

    def play(self):s
        print(self.draw_hangman(6))
        print("Guess the word")
        print(game.blank_string)
        self.guess = input()
        self.won_game()


if __name__ == "__main__":
    game = Hangman()
    game.play()
