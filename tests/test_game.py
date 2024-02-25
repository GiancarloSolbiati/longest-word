#imports the Class "Game", from a module named game within a package named longest_Word.
from longest_word.game import Game
#Imports the string module that provides string manipulation functions.
import string

#creates a class called "TestGame"
class TestGame:
    #defines the method name as "test_game_initialization"
    def test_game_initialization(self):
            #Setup: Creates a new instance of the Game Class.
            new_game = Game()

            #Exercise: This line retrieves the grid attribute from the new_game object.
            grid = new_game.grid

            #Verify: This assertion checks if the type of grid is a list and if the length of the grid is equal to 9.
            assert type(grid) == list
            assert len(grid) == 9
            #This assertion checks if each letter in the grid is a valid uppercase letter.
            #It compares each letter in the grid against the set of uppercase letters obtained from string.ascii_uppercase.
            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_empty_word_is_invalid(self):
        # setup
        new_game = Game()
        # verify
        assert new_game.is_valid('') is False

    def test_is_valid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'EUREKA'
        # exercice
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is True
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched

    def test_is_invalid(self):
        # setup
        new_game = Game()
        test_grid = 'KWEUEAKRZ'
        test_word = 'SANDWICH'
        # exerice
        new_game.grid = list(test_grid) # Force the grid to a test case
        # verify
        assert new_game.is_valid(test_word) is False
        # teardown
        assert new_game.grid == list(test_grid) # Make sure the grid remained untouched
    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
