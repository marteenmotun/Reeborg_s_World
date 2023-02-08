def turn_right():
    repeat 3:
        turn_left()

def shape_L():
    repeat 3:
        move()
    turn_left()
    repeat 3:
        move()
    turn_right()
    move()
    turn_right()
    
def last_move():
    repeat 3:
        move()
    turn_left()
    repeat 3:
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
