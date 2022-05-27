class Hangman:
    def __init__(self, word):
        """
        Initialize the game with the word to guess.

        :type  word: str
        :param word: the word to guess.
        """
        self._word = word
        self.board = "_ _ _ _ _"

        
    def check_guess(self, guess):
        """Check user input guess with answer
        assign correct letters to board property

        Args:
            guess (_str_): word given from user
        """
        word = ""
        for i in range(len(guess)):
            if guess[i] == self._word[i]:
                #print(f"{guess[i]} ", end = "")
                word += f"{guess[i]} "
            else:
                #print("_ ", end ="")
                word += "_ "
        self.board = word
        print()
        
    def print_board(self):
        # Display the starting board and correctly guessed letters
        print(self.board)
         
                

