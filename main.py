import sys
import math
import re


def console(message):
    print("Debug messages >> ", message, file=sys.stderr)


def binToChuck(binaire):
    def remplace(m):
        contents = str(m.group(0))
        if contents[0] == '0':
            return " 00 ".ljust(4+len(contents), '0')
        else:
            return " 0 ".ljust(3+len(contents), '0')
    return re.sub('(1+)|(0+)', remplace, binaire).strip()


message = input()
console("message : {0}".format(message))

binmessage = list(["{:0>7}".format(str(bin(ord(c)))[2:]) for c in message])
console("binmessage : {0}".format(binmessage))

output = str(binToChuck(''.join(binmessage)))
print(output)
