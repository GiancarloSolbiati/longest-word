# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods


#import the string module that contains constants, utility functions and string manipulaiton functions.
import string
#import random module that generate random numbers and has functions for manipulations these numbers.
import random

#create a class game
class Game:
#defines the constructor method '__init__'. The self parameter is referring to the instance of the calss being created.
    def __init__(self):
        #initialized a an empty list called 'grid'.
        self.grid = []
        # starts a look that iterates 9 times.
        for _ in range(9):
            #in this line, we will select a sting of uppercase letter, from the string module, select a random character and append to the next one.
            self.grid.append(random.choice(string.ascii_uppercase))

#defines a method names is_valid that takes the "self" and "word" parameters. The self, as the previous case, refers to the isntance of the class being created...
#...and the word parameter check if the work is empty.
def is_valid(self, word):
    if not word:
        return False
    #this line creates a copy of the grid and assings it to a variable called "letters".
    letters = self.grid.copy()
    #iterates through each character in "word".
    for letter in word:
        #check if the letter exists in letters.
        if letter in letters:
            #If the letter is found in letters, it is removed from the list. This simulates consuming the letter from the grid
            letters.remove(letter)
        else:
            return False
    return True

def is_valid(self, word):
    if not word:
        return False
    letters = self.grid.copy() # Consume letters from the grid
    for letter in word:
        if letter in letters:
            letters.remove(letter)
        else:
            return False
    return True
