import random as r

class Card():
    def __init__(self):
        self.number = 10
    
    def new_card(self):
        self.number = r.randint(1,13)
        
    def show(self):
        print(f"The card is {self.number}")
        
class Points():
    def __init__(self):
        self.points = 300
        
    def add_points(self):
        self.points+=100
        
    def minus_points(self):
        self.point-=75
    
    def game_over(self):
        if self.points <= 0:
            print("Game Over")
        
def main():
    play = True
    card = Card()
    points = Points()
    card.show()
    card.new_card()
    guess = int(input("Higher or Lower? h/l "))
"""     while play:
        if guess > card.number:
            print("Lower")
            points.minus_points()
        elif guess < card.number:
            print("Higher")
            points.minus_points
        else:
            points.add_points()
        play_again = input("Play again? y/n ")
        if play_again.lower() == "n":
            play = False
 """            
if __name__ == "__main__":
    main()