import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

zonr_d = 0
zone_f = 0
zone_a = 0

surface_n = int(input())  # the number of points used to draw the surface of Mars.
old_a = -1 old_x
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    if(old_a == land_y):
        zone_d = old_x
        zone_f = land_x
        zone_a = land_y
    old_x = land_x
    old_a = land_y
        

print(land_x, land_y, file=sys.stderr)
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print("-20 3")