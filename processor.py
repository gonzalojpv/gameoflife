# -*- encoding: utf-8 -*-

import random
import os
import itertools
import time


class Processor(object):

    def __init__(self):
        self.neighbors = list(set(itertools.permutations([-1, -1, 1, 1, 0], 2)))

        
    def board(self):
        #create mesh
        mesh = ''

        for row in self.game:
            for cell in row:
                mesh += 'x' if cell else '.'
            mesh += '\n'

        return mesh

    def clear(self):
        #clean of gameboard
        os.system('clear')

    def random_life(self):
        #get random life
        
        life = lambda:[random.randint(0,1) for n in range(self.column)]
        
        self.game = [life() for n in range(self.row)]

    def get_neighbors(self, x, y):
        #get neighbors
        count = 0
        exists_neighbor = lambda x, y: not (x in range(self.row) and y in range(self.column))
		
	for i, j in self.neighbors:
            if not exists_neighbor(x + i, y + j):
                count += 1 if self.game[x + i][y + j] else 0
		
	return count


    def process(self):
        for nf in range(self.row):
            for nc in range(self.column):
                neighbors = self.get_neighbors(nf, nc)
                
                if neighbors < 2 or neighbors > 3:
                    self.game[nf][nc] = 0
                elif neighbors == 3:
                    self.game[nf][nc] = 1
                    
    def start(self):
        self.random_life()
        
        while True:
            self.clear()
            print(self.board())
            self.process()
            time.sleep(0.5)
