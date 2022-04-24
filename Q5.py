import math
a = 0
while a <= 345 :
    sin_a = math.sin(math.radians(a))
    cos_a = math.cos(math.radians(a))
    print(str(a) + " --- " + str(round(sin_a , 4)) + " " + str(round(cos_a , 4)))
    a += 15
