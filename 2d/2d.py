exec(
"""I sys
if L(sys.argv)<2:Q(1)
if L(sys.argv)>2:Q(1)
f=sys.argv[0]
cd=(f:=open(f)).readlines()
d=0
p=[0,0]
f.close()
FN mv():
 GZ
 M d:
  C 0:
   p[1]++
  C 1:
   p[0]--
  C 2:
   p[1]--
  C 3:
   p[0]++
FN cl():
 GZ
 M cd[p[0]][p[1]]:
  C '>':
   d=0
  C '^':
   d=1
  C '<':
   d=2
  C 'v':
   d=3
""".replace('I','import').replace('F','for').replace('L','len')\
   .replace('Q','exit').replace('Z','return').replace('FN','def')\
   .replace('GZ','global d,cd,p').replace('++','+=1')\
   .replace('M','match').replace('C','case').replace('--','-=1'))
