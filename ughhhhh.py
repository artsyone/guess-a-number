from turtle import *
import random

def close(x,y):
        exitonclick()
      
onscreenclick(close)

 

setup( width = 1000, height = 600)


bg.color("PapayaWhip")
speed(0)
shape("turtle")
pensize(1)


ht()
penup()
setpos(0,-300)
pendown()
    


def draw_circle(d, c, p):
    color(c)
    pensize(p)
    circle(d)   
def draw_all_circles(c1,c2,c3,c4,c5,c6,c7,c8):
     
    for i in range (10,100,10):
        draw_circle(i,c1,1)
    for i in range (100,200,10):
        draw_circle(i,c2,3)
    for i in range (200,300,10):
        draw_circle(i,c3,3)
    
    for i in range (300,400,10):
        draw_circle(i,c4,3)
    
    for i in range (400,500,10):
        draw_circle(i,c5,6)

    for i in range (600,700,10):
        draw_circle(i,c6,6)

    for i in range (800,900,10):
        draw_circle(i,c7,6)

    for i in range (900,1000,10):
        draw_circle(i,c8,9)

    
        
    
draw_all_circles("red","orange","yellow","green","blue","BlueViolet","violet","black")


draw_all_circles("black","black","black","black","black","black","black","black")

draw_all_circles("white","white","white","white","white","white","white","white")



    
def k1():
    bgcolor("white")

def k2():
    bgcolor("black")
    
def k3():
        circle = random.rand(0,100)
        pensize = random.rand(0,20)
            
        while True:
                
                if pensize()>5 :
                    color("maroon")
                 
        
                else:
                   color("purple")
             
                
                   
onkey(k1, "Up")
onkey(k2, "space")
onkey(k3, "Down")



listen()
mainloop()
    
