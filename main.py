import sys
import math

def console(*message):
    print(*message, file=sys.stderr)

zonr_d = 0
zone_f = 0
zone_a = 0

surface_n = int(input())
old_a = -1
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    if(old_a == land_y):
        zone_d = old_x
        zone_f = land_x
        zone_a = land_y
    old_x = land_x
    old_a = land_y

# v^2 = v0^2 + 2aΔx
# v >= -35
# v0 = vitesse actuelle
# a = -3.78 + 4
# Δx = altitude actuelle
def estCritique(a, v):
    vMax = 35
    acl = 3.711 - 4
    vCal = pow(v, 2) - pow(vMax, 2) + (2 * acl * a)
    c = bool(vCal > 0)
    if c:
        console("CRITIQUE")
    return c
    
def estOut(cible, x, v):
    d = abs(cible - x)
    vMax = 15
    g = -1
    vCal = pow(v, 2) - pow(vMax, 2) + (2 * g * d)
    c = bool(vCal > 0)
    if c:
        console("OUT")
    return c

console("debut : ", zone_d, ", fin : ", zone_f, ", alt : ", zone_a)
# game loop
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [
        int(i) for i in input().split()]
    
    power = 0
    rotate = 0

    # on se dirige vers la zone
    if abs(h_speed) > 15:
        power = 4
    if x < zone_d and h_speed < 40:
        power = 4
        rotate = -45
    if x > zone_f and h_speed > -40:
        rotate = -45
        power = 4
        
    # on evite de depasser la zone
    if estOut ((zone_d+zone_f)/2, x, h_speed):
        power = 4
        rotate = h_speed * 2
        rotate = max(min(rotate, 45), -45)
    
    # on se stabilise
    if zone_d < x and x < zone_f:
        power = int(abs(v_speed * 4) / 35)
        rotate = 0
        if abs(h_speed) > 0:
            power = 4
            rotate = h_speed * 2
            rotate = max(min(rotate, 45), -45)

    # on ne s'écrase pas
    if estCritique((y - zone_a), v_speed):
        rotate = max(min(rotate, 15), -15)
        power = 4
        
    # on remonte pas
    if v_speed > 0:
        power = 3
    
    # on se pose à plat
    if (y - zone_a) < 100:
        rotate = 0
    
    print("{0} {1}".format(rotate, power))