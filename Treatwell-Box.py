"""
Here is my attempt to draw a box of a given dimension using Python. As can be seen
I have used the turtle package which is used to draw lines and made some slightly modifications
such as removing the arrowhead from the line and setting the drawing speed to the fastest
so that no animation is seen.
"""


import turtle        #to draw the box, I have imported the package turtle
import numbers       #also import this package to check if values are numbers



def box_drawer(w,h):   #inputs w is the box width and h the box height
    
    if isinstance(w, numbers.Number) == True and isinstance(h, numbers.Number) == True:   #First I check if the inputs are numbers, if they are we proceed            
        if w > 0 and h > 0:    #Now check if the box dimensions are positive values, because having a box with zero or negative dimensions does not make sense.
            
            turtle.bye()              #This is used to clear the turtle from previous runs
            turtle.hideturtle()  #I used this to hide the arrow head of the turtle
            turtle.speed(0)        #I have set the speed of the turtle to 0 which is the fastest possible so there is no animation
            
            turtle.forward(w)  #The turtle starts in the middle of the screen facing right by default and so I move it forward by w initially 
            turtle.left(90)    #The turtle now rotates left by 90 degrees 
            turtle.forward(h)  #Now the turtle movesup distance h and so on
            turtle.left(90)
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.done()      #We call this to let the turtle know it has finished its' walk
        else:
            return 'Not all inputs are positive numbers'
    else:
        return 'Not all the inputs are numbers!'  #if the inputs are not numbers, then I have returned a message saying so
    
print(box_drawer('dog',20))     #test non numeric input 

print(box_drawer(50,-500))      #test with non positive input

print(box_drawer(5,90))          #now test with valid inputs

#Because the turtle can't open in multiple windows so to do tests rerun the script with
#a different test each time. This isn't ideal but I couldn't think of a way round it.

#print(box_drawer(20,20))
#print(box_drawer(100,50))

