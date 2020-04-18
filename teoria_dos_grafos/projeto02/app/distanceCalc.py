
# -*- coding: utf-8 -*-

def distanceCalc(lat0, lng0, lat1, lng1):
    b = abs(lat0 - lat1)
    h = abs(lng0 - lng1)
    print(b,h)
    hyp = ((b**2) + (h**2)) ** (1/2)
    return hyp * 111.32
    
