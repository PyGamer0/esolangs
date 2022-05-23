import re
import sys

def transpile(x):
  x += "from mpmath import *\n"
  x = x.replace("lambda", "________lambda")
  x = x.replace("*", "**").replace("/", "//")
  x = x.replace("×", "*").replace("÷", "/")
  x = x.replace("=", "==").replace("≤", "<=").replace("≥", ">=").replace("≠", "!=")
  x = x.replace("and", "________and").replace("or", "________or").replace("not", "________not")
  x = x.replace("∧", " and ").replace("∨", " or ").replace("¬", " not ")
  x = x.replace("in", "________in").replace("∊", " in ")
  x = re.sub("(\w+ *)←", "\1=")
  x = x.replace("←", "return ")
  x = re.sub(r"λ(.*?)\.", r"lambda \1: ", x)
  return x


if sys.argv[1] == "T": # just transpile
  print(transpile(open(sys.argv[2], encoding="utf-8")))
else:
  exec(transpile(open(sys.argv[1], encoding="utf-8")))
