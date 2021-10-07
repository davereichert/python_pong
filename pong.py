import turtle

wn = turtle.Screen()
wn.title("Pong by Dave")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# Eingaben am Anfang: Wie heissen die Spieler und wieviele Runden spielt man?
player_a = wn.textinput("Pong by Dave", "Player A: Your name?")
if player_a is None or player_a == "":
    player_a = "Player A"
player_b = wn.textinput("Pong by Dave", "Player B: Your name?")
if player_b is None or player_b == "":
    player_B = "Player B"
rounds = int(wn.textinput("Pong by Dave", "How many rounds to win?"))
if rounds is None or rounds == "":
    rounds = 3

max_speed = int(wn.textinput("Pong by Dave", "max speed?"))
if max_speed is None or max_speed == "":
    max_speed = 3

# Score
score_a = 0
score_b = 0

# Bewegung
start_speed = 0.5
speed_up = 0.1
dir_x = 1
dir_y = 1

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Function
def restart_ball():
    global ball
    global speed

    speed = start_speed
    ball.goto(0, 0)
    ball.color("black")
    ball.dx = speed * dir_x
    ball.dy = speed * dir_y

# Function
def restart():
    global score_a
    global score_b

    # Reset score
    score_a = 0
    score_b = 0

    # Restart score display
    pen.clear()
    pen.color("orange")
    pen.write("{}: {} {}: {}".format(player_a,score_a,player_b,score_b), align="center", font=("Courier",24, "normal"))

    # Restart ball
    restart_ball()
    
# Function
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 40
    paddle_a.sety(y)
    
# Function
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 40
    paddle_a.sety(y)

#Function
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y+= 40
    paddle_b.sety(y)

#Function
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y-= 40
    paddle_b.sety(y)

# Ball
ball = turtle.Turtle()
ball.shape("square")
ball.penup()
speed = start_speed
restart_ball()

# pen
pen = turtle.Turtle()
pen.clear()
pen.speed(0)
pen.color("orange")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: {} {}: {}".format(player_a,score_a,player_b,score_b), align="center", font=("Courier",24, "normal"))


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(restart, "r")

# Main game loop
restart_ball()
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        dir_y *= -1
        ball.dy = speed * dir_y

    if ball.ycor() < -290:
        ball.sety(-290)
        dir_y *= -1
        ball.dy = speed * dir_y

    if ball.xcor() > 390:
        dir_x *= -1
        restart_ball()
        score_a += 1
        pen.clear()
        pen.color("blue")
        pen.write("{}: {} {}: {}".format(player_a,score_a,player_b,score_b), align="center", font=("Courier",24, "normal"))
               
    if ball.xcor() < -390:
        dir_x *= -1
        restart_ball()
        score_b += 1
        pen.clear()
        pen.color("red")
        pen.write("{}: {} {}: {}".format(player_a,score_a,player_b,score_b), align="center", font=("Courier",24, "normal"))
  
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        if speed < max_speed:
            speed += speed_up
        dir_x *= -1
        ball.dx = speed * dir_x
        ball.dy = speed * dir_y
        ball.color("red")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        if speed < max_speed:
            speed += speed_up
        dir_x *= -1
        ball.dx = speed * dir_x
        ball.dy = speed * dir_y
        ball.color("blue")

    if score_a == rounds:
        speed = 0
        ball.dx = speed * dir_x
        ball.dy = speed * dir_y
        pen.clear()
        pen.write("{} wins {} : {}. Press r to restart".format(player_a,score_a, score_b), align="center", font=("Courier",24, "normal"))
        
    if score_b == rounds:
        speed = 0
        ball.dx = speed * dir_x
        ball.dy = speed * dir_y
        pen.clear()
        pen.write("{} wins {} : {}. Press r to restart".format(player_b,score_b, score_a), align="center", font=("Courier",24, "normal"))
