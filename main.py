import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def console (*msg):
    print(*msg, file=sys.stderr)

def encadre (minVal, val, maxVal):
    return max(minVal, min(val, maxVal))

class Stricker:

    def __init__(self, circuit = list(), curentCp = (0,0), nbTour = 0, lastPos = (0,0)):
        self._circuit  = circuit
        self._curentCp = curentCp
        self._nbTour   = nbTour
        self._lastPos  = lastPos
        self._boost    = 0

    def getCmd(self, x, y, next_checkpoint_x, next_checkpoint_y, 
            next_checkpoint_dist, next_checkpoint_angle, opponent_x, 
            opponent_y ):
        self._debug(x, y, next_checkpoint_x, next_checkpoint_y, 
            next_checkpoint_dist, next_checkpoint_angle, opponent_x, 
            opponent_y)
        self._storeCP(next_checkpoint_x, next_checkpoint_y)
        trust = encadre(
            10, 
            int((90 - abs(next_checkpoint_angle)) * 200 / 90), 
            100
            )
        delta = self._delta(x, y)
        if (next_checkpoint_dist - (delta * 3)) < 0:
            trust = 0
        if (not self._boost) and self._nbTour >= 2 and next_checkpoint_dist > 10000 and abs(next_checkpoint_angle) < 5:
            trust = 'BOOST'
            self._boost += 1
        if self._boost > 0:
            console("BOOST")
        self._storePos(x, y)
        return "{0} {1} {2}".format(next_checkpoint_x, next_checkpoint_y, trust )

    def _storeCP(self, next_checkpoint_x, next_checkpoint_y):
        cp = (next_checkpoint_x, next_checkpoint_y)
        if cp not in self._circuit:
            self._circuit.append(cp)
        else: 
            if self._circuit.index(cp) == 0:
                console ("NOUVEAU TOUR")
                if cp != self._curentCp:
                    self._nbTour += 1
        self._curentCp = cp

    def _storePos(self, x, y):
        self._lastPos = (x, y)

    def _debug(self, x, y, next_checkpoint_x, next_checkpoint_y, 
            next_checkpoint_dist, next_checkpoint_angle, opponent_x, 
            opponent_y):
        console("s = Strick(", self._circuit, ",", self._curentCp, ",", self._nbTour, ",",
            self._lastPos, ")")
        console("s.getCmd(", x, ",", y, ",",  next_checkpoint_x, ",",  next_checkpoint_y,
            ",", next_checkpoint_dist, ",",  next_checkpoint_angle, ",",  opponent_x, ",", 
            opponent_y, ")")
            
    def _deg2rad(self, deg):
        return math.pi * deg / 180
        
    def _delta(self, x, y):
        oldx, oldy = self._lastPos
        return int( math.sqrt(pow(x-oldx, 2) + pow(y-oldy, 2)) )

s = Stricker()

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
        
    print(s.getCmd(x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle, opponent_x, opponent_y))