import sys

def eprint(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

class ReflectorBackslash:
    def on_collide(self, mover):
        if mover.direction == "DOWN":
            mover.direction == "LEFT"
            mover.pos[0] -= 1
        elif mover.direction == "UP":
            mover.direction == "RIGHT"
            mover.pos[0] += 1
        elif mover.direction == "LEFT":
            mover.direction == "DOWN"
            mover.pos[1] += 1
        elif mover.direction == "RIGHT":
            mover.direction == "UP"
            mover.pos[1] -= 1

    def __repr__(self):
        return "\\"

class ReflectorSlash:
    def on_collide(self, mover):
        if mover.direction == "DOWN":
            mover.direction == "RIGHT"
        elif mover.direction == "UP":
            mover.direction == "LEFT"
        elif mover.direction == "LEFT":
            mover.direction == "UP"
        elif mover.direction == "RIGHT":
            mover.direction == "DOWN"

    def __repr__(self):
        return "/"

class CDot:
    def on_collide(self, mover):
        mover.print()

    def __repr__(self):
        return "."

class CExit:
    def on_collide(self, mover):
        exit(0)

    def __repr__(self):
        return f";"

class CNone:
    def on_collide(self, mover):
        pass

    def __repr__(self):
        return f"None"

class Mover:
    def __init__(self, x=0, y=0):
        self.pos = [x, y]
        self.value = None
        self.direction = "RIGHT"

    def step(self):
        if self.direction == "DOWN":
            self.pos[0] += 1
        elif self.direction == "UP":
            self.pos[0] -= 1
        elif self.direction == "RIGHT":
            self.pos[1] += 1
        elif self.direction == "LEFT":
            self.pos[1] -= 1

    def __repr__(self):
        return f"M({self.pos}, {self.direction}, {self.value})"

    def on_collide(self, mover):
        pass

    def print(self):
        print(self.value)

def atom(char, pos):
    if char == '#':
        return Mover(pos[1] - 1, pos[0] - 1)
    elif char in '/\\':
        return ReflectorBackslash() if char == '\\' else ReflectorSlash()
    elif char == '.':
        return CDot()
    elif char == ';':
        return CExit()
    else:
        return CNone()

def parse(string):
    code = []
    string = string.split("\n")

    y = 0
    while y < len(string):
        line = string[y]
        y += 1
        lcode = []

        x = 0
        while x < len(line):
            char = line[x]
            x += 1

            lcode.append(atom(char, (y, x)))
        code.append(lcode)
    return code

def execute(code):
    movers = []

    for l in code:
        for c in l:
            if isinstance(c, Mover):
                movers.append(c)

    if len(movers) == 0:
        return

    while True:
        for mover in movers:
            mover.step()

            current = code[mover.pos[0]][mover.pos[1]]
            current.on_collide(mover)


if not len(sys.argv) > 1:
    eprint("Usage: $ python 2dee.py <filename>")
    exit(1)

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    eprint(f"File '{sys.argv[1]}' not found.")
    exit(2)

if file.readable:
    code = parse(file.read())
else:
    code = [[CNone()]]

eprint(code)
execute(code)
