import turtle #allows you to do basic graphics

wn=turtle.Screen() #making a screen
wn.title("Pong") #title of the screen
wn.bgcolor("black") #background color #color spelt with o no u
wn.setup(width=800, height=600) #setting dimensions
wn.tracer(0)        # it stops the window from updating

#paddle A
paddle_a=turtle.Turtle() #turtle object called paddle_a
paddle_a.speed(0) #speed of the animation
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) #where we want it to start


#paddle B
paddle_b=turtle.Turtle() #turtle object called paddle_a
paddle_b.speed(0) #speed of the animation
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) #where we want it to start
#ball
ball=turtle.Turtle() #turtle object called paddle_a
ball.speed(0) #speed of the animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0) #where we want it to start
ball.dx = 0.07
ball.dy = -0.07
#functions of each object we created
def paddle_a_up():
    y=paddle_a.ycor()
    y+=40
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=40
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=40
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=40
    paddle_b.sety(y)
#inorder to use the functions we need to link it to keyboard(keyboard binding)
wn.listen()  #listen for keyboard inputs 
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
#every game needs a main loop
while True: #true with cap T
    wn.update()
#move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#border checking
    if ball.ycor() > 290:#if ball reaches upper border reverse
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor() < -290:#if ball reaches upper border reverse
        ball.sety(-290)
        ball.dy *=-1
    if ball.xcor() > 390:#if ball reaches upper border reverse
        ball.goto(0,0)
        ball.dx *=-1
    if ball.xcor() < -390:#if ball reaches upper border reverse
        ball.goto(0,0)
        ball.dx *=-1
    
    #paddle and ball collisions
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
        ball.dx *=-1
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
        ball.dx *=-1