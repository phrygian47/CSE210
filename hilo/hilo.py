import random as r

class Card():
    def __init__(self):
        self.number = 0
    
    def new_card(self):
        self.old_number = self.number
        self.number = r.randint(1,13)
        
    def show(self):
        print(f"The card is {self.number}")
        
class Points():
    def __init__(self):
        self.points = 300
        
    def add_points(self):
        self.points+=100
        
    def minus_points(self):
        self.points-=75
    
    def game_over(self):
        if self.points <= 0:
            print("Game Over")
        
def main():
    play = True
    card = Card()
    points = Points()
    card.new_card()
    card.show()
    while play and points.points > 0:
        guess = input("Higher or Lower? h/l ")
        card.new_card()
        if (card.number > card.old_number) and guess.lower() == "h":
            points.add_points()
        elif (card.number < card.old_number) and guess.lower() == "l":
            points.add_points()
        elif (card.number > card.old_number) and guess.lower() == "l":
            points.minus_points()
        elif (card.number < card.old_number) and guess.lower() == "h":
            points.minus_points()
        print(f"The card was: {card.number}")
        print(f"Your score is {points.points}")
        if points.points > 0:
            play_again = input("Play again? y/n ")
            if play_again.lower() == "n":
                play = False
        points.game_over()
          
if __name__ == "__main__":
    main()