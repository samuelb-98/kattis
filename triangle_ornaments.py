from cmath import pi
import math
import sys

input_nr = 0
T = 0
triangles = []
for line in sys.stdin:
    line = [int(i) for i in line.split()]
    if input_nr == 0:
        T = line[0]
    if 0 < input_nr <= T:
        triangles.append(line)
    if input_nr == T:
        width = 0
        for triangle in triangles:
            a,b,c = triangle
            A = math.acos((b**2 + c**2 -a**2) / (2*b*c))
            c  /= 2
            a = (b**2 + c**2 - 2*b*c*math.cos(A))**0.5
            B = math.asin((b*math.sin(A))/a)
            width += 2*c*math.cos(math.pi/2 - B)
        print(width)
    if input_nr == T:
        break
    input_nr +=1