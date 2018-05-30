import sys
import math
import re

def console(message):
    print("Debug messages >> ", message, file=sys.stderr)


def binToChuck(binaire):
    def repl(m):
        contents = m.group(0)
        if contents[0] == '0':
            return " 00 ".ljust(len(contents), '0') 
        else:
            return " 0 ".ljust(len(contents), '0') 
    return re.sub('(1+)|(0+)', repl, binaire).strip()


message = input()

binmessage = list(["{:0>7}".format(str(bin(ord(c)))[2:]) for c in message])

print(str(binToChuck(''.join(binmessage))))