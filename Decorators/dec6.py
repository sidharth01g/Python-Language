import math


def clip_function(old_function):
    upper = 0.8
    lower = -0.8
    def clip(x):
        if old_function(x) > 0:
            return min(old_function(x), upper)
        else:
            return max(old_function(x), lower)
    return clip

@clip_function
def get_sin(x):
    return math.sin(x)

points = 101
for i in range(points):
    angle = i * 2.0 * math.pi / (points - 1)
    print get_sin(angle),
    #print angle,
