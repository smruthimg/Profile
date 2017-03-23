"""
To draw raindrops and calculate the area
file: Raindrops.py
author: Smruthi Gadenkanahalli
Created: 9 Sep 2016
revised: 11 Sep 2016

"""


import turtle as t
import random
import math

# function definitions

def initWorld():
    """
    initWorld initializes the drawing by establishing its pre-conditions.


    pre-conditions:
    post-conditions: turtle is at origin,
                     turtle is pen-up.
    """

    t.setup(700, 700)

    t.home()  # turtle is at origin, facing east, pen-down
    t.up()  # turtle is pen-up
    t.pensize(1)


def MAX_RAINDROPS():
    '''return maximum number of rain raindrops allowed '''
    return 100


def MIN_RAINDROPS():
    '''return minimum number of rain raindrops allowed '''
    return 1

def MAX_BORDER_X():
    '''max range of positive x axis'''
    return 250

def MIN_BORDER_X():
    '''min range of positive x axis'''
    return -250

def MAX_BORDER_Y():
    '''max range of positive y axis'''
    return 250


def MIN_BORDER_Y():
    '''min range of positive y axis'''
    return -250

def MIN_POSITIVE_INTEGER():
    '''Minimum poisitve randon integer '''
    return 1


def MAX_POSTIVE_INTEGER():
    '''Maximum poisitve randon integer '''
    return 20


def MAX_RIPPLES():
    '''Maximum number of ripples allowed'''
    return 8


def MIN_RIPPLES():
    '''Minimum number of ripples allowed'''
    return 3

def INIT_AREA():
    '''Initial value of the area'''
    return 0

def drawBorder():
    '''Draw a border to confine the drops and the ripples'''
    t.up()
    t.goto(MIN_BORDER_X(),MIN_BORDER_Y())
    t.pencolor("black")
    t.fillcolor('skyblue') #  fill the box with color
    t.begin_fill()
    t.down()
    t.forward(500)
    t.left(90)
    t.forward(500)
    t.left(90)
    t.forward(500)
    t.left(90)
    t.forward(500)
    t.end_fill()
    t.up()
    t.goto(0,0)
    t.left(90)

def drawRipples(n,a):
    '''Draw rain drops and ripples based on user input with number raindrops'''

    t.down()
    t.pencolor("black")
    if n>0:
        # draw the raindrops recursively if the number is greater than 1

        # random number for radius of the drop
        r=random.randint(MIN_POSITIVE_INTEGER(),MAX_POSTIVE_INTEGER())


        #  setting random location for the raindrop
        xaxis=random.randint(MIN_BORDER_X(),MAX_BORDER_X())
        yaxis=random.randint(MIN_BORDER_Y(),MAX_BORDER_Y())
        print(xaxis,yaxis)

        #  setting random number for the ripples
        rips=random.randint(MIN_RIPPLES(),MAX_RIPPLES())

        if (xaxis-r)>MIN_BORDER_X() and (yaxis-r)>MIN_BORDER_Y() and ((r+r+xaxis)<MAX_BORDER_X() and (r+r+yaxis)<MAX_BORDER_Y()):

            #  draawing raindrop only if its within the border
            t.up()

            t.goto(xaxis,yaxis)

            # t.screen.colormode(255)

            t.down
            t.fillcolor(random.random(),random.random(),random.random())
            #  fill color to raindrop
            t.begin_fill()
            t.circle(r)
            t.end_fill()
            t.up()
            t.right(90)
            t.forward(r)
            t.left(90)
            newr=r*2
            while (rips>0):  #  quit drawing ripples if it goes beyond the border
                if (xaxis-newr) < MIN_BORDER_X() or (yaxis-newr) < MIN_BORDER_Y() or (newr +newr+ xaxis) > MAX_BORDER_X()  or  (newr+newr + yaxis) > MAX_BORDER_Y():

                    break
                else:
                    t.down()
                    t.circle(newr)
                    t.up()
                    t.right(90)
                    t.forward(r)
                    t.left(90)
                    newr=newr+r
                    rips=rips-1

        # call draw raindrop function recursively and return area of raindrops
        return drawRipples(n-1,(a+(math.pi*r*r)))

    else:
        #  return area if the number of raindrops is 0
        return a


def promptNoOfDrops():
    '''Request user to input the number of raindrops to be draw'''
    x=int(input("Enter the number of raindrops to be drawn (1-100):"))
    if x>MAX_RAINDROPS() or x<MIN_RAINDROPS() :
        # if the number is not in the range of max and min number of rainrops allowed then prompt user
        print("Raindrops must be between 1 and 100 inclusive")
        exit()
    else:
        drawBorder()
        area=drawRipples(x,INIT_AREA())
        print("The total area of the raindrops is ",area ,"square units")



def main():
    '''main function to set the canvas and callt he functions to draw the pond and ripples'''
    # t.speed('fastest')
    initWorld()
    promptNoOfDrops()

#  finally calling the main
main()
t.done()