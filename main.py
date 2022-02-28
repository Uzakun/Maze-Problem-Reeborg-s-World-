def turn_right():
    turn_left()
    turn_left()
    turn_left()

def keep_moving():
    turn_right() 
    while wall_on_right():    
      move()
    while front_is_clear():
        move()  
        
while not at_goal():
   if wall_in_front() and wall_on_right():
    turn_left()
   elif right_is_clear():
    turn_right()
    move()
   elif wall_in_front():
    keep_moving() 
   else:
    move()