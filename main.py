#!/user/bin/env python
import numpy as np


class World:

    def __init__0(self):
        '''
        Initialization function for the World
        '''

        self.x = 100
        self.y = 100
        self.food_count = 100

        self.food_positions = 100*np.random.rand(self.food_count, 2)

        print(self.food_positions)


class Herbivore:

    def __init__():
        '''
        Initialization Function
        '''


world = World()
