import math
angle = math.radians(120)
for n in range(0, 370, 10):
    angle = math.radians(n)
    print(n, math.tan(angle))
