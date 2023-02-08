def turn_right():
    turn_left()
    turn_left()
    turn_left()


def shape_L():
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    
def last_move():
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    
def half_way_move():
    shape_L()
    shape_L()

def home_4():
    half_way_move()
    shape_L()
    last_move()

home_4()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
