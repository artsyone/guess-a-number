from turtle import *
import random


def close(x,y):
        exitonclick()
      
onscreenclick(close)

colormode(255)
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

def draw_circle(c,s):
    count = 0
    
    color(c)
    setpos(s)
    
    
    while count <= 5:
        circle(random.randint(0,200))
        pensize(random.randint(0,10))
        penup()
        setpos(s)       
        pendown()
        count += 1
    return

draw_circle("black",(-400,0))                
draw_circle("black",(-200,0))
draw_circle("black",(0,0))



def k1():
    bgcolor("yellow")

def k2():
    bgcolor("blue")
    


def stars():
    for i in range(5):
           color("blue")
           fd(100)
           rt(216)
           angle = 144
           
           pensize(random.randint(0,5))
           
        
def more_stars():   
    for i in range(4):
           color("yellow")
           fd(100)
           lt(216)
           pensize(random.randint(0,5))
         

def k3():
    bgcolor("black")   
                
                   
onkey(k1, "Up")
onkey(k2, "space")
onkey(k3, "\n")
onkey(stars, "Left")
onkey(more_stars, "Right")




listen()
mainloop()


