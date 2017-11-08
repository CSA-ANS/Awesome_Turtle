def final_turtle():
    import turtle
    wn=turtle.Screen()
    wn.bgcolor("green")
    

    alex=turtle.Turtle()
    alex.color("brown")
    alex.speed(5)
    alex.pensize(10)
    alex.shape("turtle")
    alex.pencolor("pink")
    tess=turtle.Turtle()
    tess.color("hotpink")
    tess.speed(10)
    tess.pensize(15)
    tess.shape("circle")
    tess.pencolor("green")
    alex.fillcolor("purple")
    alex.begin_fill()
    for i in range(8):
        alex.forward(150)
        alex.left(45)
        alex.stamp()
    alex.end_fill()
    tess.fillcolor("blue")
    tess.begin_fill()
    for i in range(4):
        tess.forward(150)
        tess.left(90)
        tess.stamp()
    tess.end_fill()
    

final_turtle()
    
