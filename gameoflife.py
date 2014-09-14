#! /usr/bin/python
# -*- encoding: utf-8 -*-

from processor import Processor

class GameOfLife(Processor):

    #def __init__(self):
       # self.neighbors = list(set(itertools.permutations([-1, -1, 1, 1, 0], 2)))
        #self.random_life()
     #   self.welcome()

        
    def welcome(self):
        #output message
        print("==============================")
        print("==============================")
        print("Welcome to Game Of Life")
        print("==============================")
        print("==============================")
        self.row = int(input("Row: "))
        self.column = int(input("Column: "))
        
    def main(self):
        #init
        self.welcome()
        self.start()
        
        



if __name__ == '__main__':
    #starting with game play
    game = GameOfLife()
    game.main()
