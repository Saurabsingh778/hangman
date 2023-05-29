import random
from PyDictionary import PyDictionary
import nltk
nltk.download("wordnet")

from nltk.corpus import wordnet

class Game:
    def __init__(self) -> None:
        self.total_point = 0  
    def think_word(self):
        print("*******Let me Think********")
        sysnsets = list(wordnet.all_synsets())
        lis = []
        
        for i in sysnsets:
            p = i.lemmas()
            
            wor = p[0].name()
            
            if len(wor) <= 10:
                lis.append(wor)
                
        self.word = random.choice(lis)
        
        print("******Ok Done*******")
                
        dic = PyDictionary()
        
        flag = False
        
        print("**length of word is**", len(self.word))
        
        if len(self.word) <= 5:
            print("**maximum guess 3")
            self.guess = 3
        else:
            print("**maximum guess 10")
            self.guess = 10
        
        
        print("***Do you Want a hint type yes if want!***")
        hint_condition = input()
        
        if hint_condition == "yes":
            flag = True
        
        if flag:
            self.hint = True
            print("******Let me give you meaning of word*****\n\n")
            print(dic.meaning(self.word)['Noun'][0])
            print("\n")
        
    
    def play_game(self):
        print("***you can guess only 3 wrong words***\n\n")
        print("**please guess a word accordingly**\n")
        c = 0
        point = 0
        p = self.guess
        flag = True
        while True:
            guess = input()
            if guess == self.word:
                print("***You won the game***")
                point += 100
                if self.hint:
                    point -= 5
                self.total_point += point
                flag = False
                break
            else:
                c += 1
                point -= c * 3
            print("Try Again")
            p -= 1
            if p == 0:
                break
        if flag:
            print("**You lost**\n\n")
            print("Correct Word is", self.word)
            print()
            print("Total Point", self.total_point)
    def print_point(self):
        print("Total point ", self.total_point)

if __name__ == "__main__":
    print("Do you want to play if yes type y else n")
    x = input()
    if x == "y":
        while True:
            game = Game()
            game.think_word()
            game.play_game()
            
            print("Do you want to play again if yes type y else n")
            y = input()
            if y != "y":
                game.print_point()
                print("**Thankyou for playing**")
                break
    else:
        print("**Ok no problem**")
        
        
            
    
    
        
    