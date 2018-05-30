import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def console(*message):
    print(*message, file=sys.stderr)


l = int(input())
h = int(input())
t = str(input())
f = list()
for i in range(h):
    z = input()
    f.append(z)


class Ascii:

    def __init__(self, l, h, font):
        self.l = int(l)
        self.h = int(h)
        self.font = list(font)
        self.alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"

    def _getStart(self, car):
        if car in self.alpha:
            return self.l * int(self.alpha.find(car))
        return self.l * int(self.alpha.find('?'))

    def _wrileLineCar(self, ligne, car):
        if car == ' ':
            return ''.ljust(self.l)
        start = self._getStart(car)
        end = start + self.l
        return self.font[ligne][start:end]

    def write(self, msg):
        output = ""
        cars = list([c for c in str(msg).upper()])
        for i in range(self.h):
            for car in cars:
                output += self._wrileLineCar(i, car)
            output += "\n"
        return output


formater = Ascii(l, h, f)

print(formater.write(t))
