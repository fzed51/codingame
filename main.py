import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def console (*msg):
    print(*msg, file=sys.stderr)


class Stricker:

    def __init__(self, circuit = list(), curentCp = (0,0), nbTour = 0, lastPos = (0,0)):
        self._circuit = circuit
        self._curentCp = curentCp
        self._nbTour = nbTour
        self._lastPos = lastPos

    def getCmd(self, x, y, next_checkpoint_x, next_checkpoint_y, 
            next_checkpoint_dist, next_checkpoint_angle, opponent_x, 
            opponent_y ):

        self._debug(x, y, next_checkpoint_x, next_checkpoint_y, 
            next_checkpoint_dist, next_checkpoint_angle, opponent_x, 
            opponent_y)
            
        self._storeCP(next_checkpoint_x, next_checkpoint_y)
        
        trust = int(max(10,min(
            100, 
            10 + 100 * math.cos(self._deg2rad(next_checkpoint_angle))
        )))

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
        console("s.getCmd(", x, ",",  y, ",",  next_checkpoint_x, ",",  next_checkpoint_y,
            ",", next_checkpoint_dist, ",",  next_checkpoint_angle, ",",  opponent_x, ",", 
            opponent_y, ")")
            
    def _deg2rad(self, deg):
        return math.pi * deg / 180

#     delta = abs(old[0]-x) + abs(old[1]-y)
# console("delta : ", delta)
# CP = (next_checkpoint_x, next_checkpoint_y)
# 
# if CP not in CPs:
#     CPs.append(CP)
# else:
#     posCP = CPs.index(CP)
#     tour = 1
#     if posCP < len(CPs) - 1:
#         if next_checkpoint_dist < 3000:
#             next_checkpoint_x, next_checkpoint_y = CPs[posCP + 1]
#             
# if tour > 0 and next_checkpoint_dist > 9000 and (next_checkpoint_angle * 180 / math.pi) < 5:
#     trust = "BOOST"
# else :
#     trust = min(max(10 + int( 100 * math.cos(next_checkpoint_angle * 180 / math.pi) ), 0), 100)
#     if tour == 0 and next_checkpoint_dist < 3000:
#         trust /= 2        
#     if tour == 0 and next_checkpoint_dist < 1500:
#         trust /= 2

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