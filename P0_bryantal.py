######################################################################
# Author: Alex Bryant
# Username: bryantal
#
# Assignment: P0: Final Project
# Purpose: Enhancing the Nim game from A5 to use turtle graphics and click handlers to play.
#
######################################################################
import turtle
from t14_point import *

class Nim_Game():
    """
    Class that sets up the Game of Nim graphics.
    """
    def __init__(self, sb=20):
        """
        Initializer for the
        """
        self.start_balls = sb
        self.turtle = None

    def draw_bowl(self):
        """
        Draws the window where the game will begin.
        :return:
        """
        turt = turtle.Turtle()
        turt.color("purple")
        turt.hideturtle()
        turt.pensize(5)
        turt.penup()
        turt.goto(-150, -50)
        turt.pendown()
        turt.forward(300)
        turt.left(90)
        turt.forward(300)
        turt.penup()
        turt.goto(-150, -50)
        turt.pendown()
        turt.forward(300)
        turt.color("Black")
        turt.penup()
        turt.goto((0, -180))
        turt.pendown()
        turt.write("Click up to four balls to take them away", move=False, align="Center", font=("Arial",15))
        turt.penup()
        turt.goto((0, -200))
        turt.pendown()
        turt.write("Check the console for instructions", move=False, align="Center", font=("Arial",15))


    def draw_balls(self):
        """
        Draws the number of balls inside the bowl
        :return:
        """
        #for i in range(self.start_balls):
        #a = -120
        #d = -25
        b = Ball(-120, -25)
        b.draw_ball()
        c = Ball(-70, -25)
        c.draw_ball()
        d = Ball(-20, -25)
        d.draw_ball()
        e = Ball(30, -25)
        e.draw_ball()
        f = Ball(80, -25)
        f.draw_ball()
        g = Ball(130, -25)
        g.draw_ball()
        h = Ball(-120, 25)
        h.draw_ball()
        i = Ball(-70, 25)
        i.draw_ball()
        j = Ball(-20, 25)
        j.draw_ball()
        k = Ball(30, 25)
        k.draw_ball()
        l = Ball(80, 25)
        l.draw_ball()
        m = Ball(130, 25)
        m.draw_ball()
        n = Ball(-120, 75)
        n.draw_ball()
        o = Ball(-70, 75)
        o.draw_ball()
        p = Ball(-20, 75)
        p.draw_ball()
        q = Ball(30, 75)
        q.draw_ball()
        r = Ball(80, 75)
        r.draw_ball()
        r = Ball(130, 75)
        r.draw_ball()
        s = Ball(-120, 125)
        s.draw_ball()
        t = Ball(-70, 125)
        t.draw_ball()

    def game_turns(self):
        total = 20
        while total> 0:
            total = player_turn(total)
            if total == 0:
                print("You win!")
                break
            total = nim_gonna_win(total)
            if total == 0:
                print("You've lost.")
                print("Thanks for playing, try again.")




class Ball():
    """
    Class to create the balls to click on in the Game of Nim.
    """
    def __init__(self, co1, co2):
        """

        :param x:
        :param y: size of the ball
        :param color: ball color
        """
        self.x = co1
        self.y = co2
        #self.color = color
        self.t = None

    def draw_ball(self):
        """
        :param start_point: Where the turtle will start to draw the circle
        :return:
        """
        #self.turtle = turtle.Turtle()
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        self.t.shape("circle")
        self.t.onclick(self.click_ball)

    def click_ball(self, x, y):
        self.t.clear()
        self.t.hideturtle()
        
def nim_gonna_win(num):
    """how much the computer takes from the total"""
    if (num - 1) % 5 == 0 or (num - 1) == 0:
        num = num -1
        print("Okay, I'll take away 1")
        print("The total should now be " + str(num))
        return num
    elif (num - 2) % 5 == 0 or (num - 2) == 0:
        num = num -2
        print("Okay, I'll take away 2")
        print("The total should now be " + str(num))
        return num
    elif (num - 3) % 5 == 0 or (num - 3) == 0:
        num = num -3
        print("Okay, I'll take away 3")
        print("The total should now be " + str(num))
        return num
    elif (num - 4) % 5 == 0 or (num - 4) == 0:
        num = num -4
        print("Okay, I'll take away 4")
        print("The total should now be " + str(num))
        return num
    else:
        num = num - 1
        print("The total is now be " + str(num))
        return num
        
def player_turn(num):
    """the player's input number"""
    choice = int(input("How many balls would you like to take away? (1-4):"))
    while choice< 1 or choice> 4 or choice> num:
        choice = int(input("Sorry, can't do that.  Choose another number (1-4):"))
    num = num - choice
    print("The total should now be " + str(num))
    return num



def main():
    wn = turtle.Screen()
    wn.title("The Game of Nim")
    g = Nim_Game()
    g.draw_bowl()
    g.draw_balls()
    print("Type the number of balls you want to take away and then click the screen")
    print("To take them away from the bowl.")
    print("The computer will then say in the console how many balls it wants to take away.")
    print("Click the balls on screen to take away its amount of balls.")
    g.game_turns()
    wn.mainloop()

if __name__ == "__main__":
    main()

