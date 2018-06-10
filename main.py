

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


s = Stricker()

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [
        int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    print(s.getCmd(x, y, next_checkpoint_x, next_checkpoint_y,
                   next_checkpoint_dist, next_checkpoint_angle, opponent_x, opponent_y))
