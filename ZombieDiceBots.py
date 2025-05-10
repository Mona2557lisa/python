print("name : monalisa.n \n usn : 1AY24AI073 \n section : O ")

import zombiedice

class StopAt2Brains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        result = zombiedice.roll()
        while result is not None:
            brains += result['brains']
            if brains >= 2:
                break
            result = zombiedice.roll()

zombiedice.registerBot(StopAt2Brains("QuickBot"))
zombiedice.runTournament(numGames=10)
