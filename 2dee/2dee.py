import sys

def eprint(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

class Obstacle:
    def __init__(self):
        pass

    def on_collide(self, mover):
        if mover.direction == "DOWN":
            mover.direction == "LEFT"
        elif mover.direction == "UP":
            mover.direction == "RIGHT"
        elif mover.direction == "LEFT":
            mover.direction == "DOWN"
        elif mover.direction == "RIGHT":
            mover.direction == "UP"

class Mover:
    def __init__(self, x=0, y=0):
        self.pos = [x, y]
        self.value = None
        self.direction = "UP"

    def step(self):
        if self.direction == "DOWN":
            self.pos[0] += 1
        elif self.direction == "UP":
            self.pos[0] -= 1
        elif self.direction == "RIGHT":
            self.pos[1] += 1
        elif self.direction == "LEFT":
            self.pos[1] -= 1

    def print(self):
        print(self.value)

if not len(sys.argv) > 1:
    eprint("Usage: $ python 2dee.py <filename>")
    exit(1)

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    eprint(f"File '{sys.argv[1]}' not found.")
    exit(2)

if file.readable:
    code = file.readlines()
else:
    code = ""
