from turtle import *
import random
sam = Turtle()
bob = Turtle()

def close(x,y):
        exitonclick()
      
onscreenclick(close)


bgcolor("white")
speed(0)
shape("turtle")
pensize(1)


ht()
penup()
setpos(300,300)
pendown()




        
                

setup( width = 1200, height = 700)
def draw_star(a,c,p):
    count = 0
    size = 100
    color(c)
    pensize(p)
    angle = (a)
    
    while count <= 5:
        fd(size)
        rt(angle)
        count += 1
    return




def draw_star_diff(b,c,p):
    count = 0
    size = 100
    color(c)
    pensize(p)
    angle = 144
    
    while count <= 5:
        fd(size)
        rt(b)
        count += 1
    
    return


draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )

penup()

setpos(-600,300)

pendown()
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )
draw_star(-216,"yellow",3 )
draw_star(216,"blue",3 )








color("yellow")
side = 400
penup()
goto(-200,-200)
pendown()
#Start Spiral
for i in range (1,100):
    forward(side)
           
    left(90)
    side=side-4









def k1():
    bgcolor("yellow")

def k2():
    bgcolor("blue")
    
def k3():
    circle(random.randint(0,200))
    pos(random.randint(-400,400))
    pensize(random.randint(0,10))
    while circle < 20:
        color("yellow")
    else:
        color("blue")

def k4():
    circle(random.randint(-200,0))
    pos(random.randint(400,-400))
    pensize(random.randint(0,10))
    while circle < 20:
        color("blue")
    else:
        color("yellow")
        
def k5():
    bgcolor("white")  
    
                
                   
onkey(k1, "Up")
onkey(k2, "space")
onkey(k3, "Down")
onkey(k4, "Left")
onkey(k5, "Right")



listen()
mainloop()


