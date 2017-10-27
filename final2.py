from turtle import *

window_height()
400
window_width ()
640


speed(0)
shape("turtle")
pensize(1)





    



def draw_circle(d, c, p):
    color(c)
    pensize(p)
    
    circle(d)

    ht()
    speed(0)
    penup()
    setpos(0,-300)
    penup()
    pendown()
    
    count = 0


    
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
    

onkey(k1, "Up")
onkey(k2, "space")

    

listen()
mainloop()
    

