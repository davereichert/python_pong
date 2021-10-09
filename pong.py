import turtle

# Initialisierung des Spielbildschirms
wn = turtle.Screen()
wn.title("Pong by Dave")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

# Eingaben am Anfang: Wie heissen die Spieler und wieviele Runden spielt man?
player_a = wn.textinput("Pong by Dave", "Player A: Your name?")
if player_a is None or player_a == "":
    player_a = "Player A"
player_b = wn.textinput("Pong by Dave", "Player B: Your name or bot for computer player?")
if player_b is None or player_b == "":
    player_B = "Player B"
rounds = wn.textinput("Pong by Dave", "How many rounds to win?")
if rounds is None or rounds == "":
    rounds = 3
else:
    rounds = int(rounds)
max_speed = wn.textinput("Pong by Dave", "max speed?")
if max_speed is None or max_speed == "":
    max_speed = 3
else:
    max_speed = float(max_speed)

# bot_mode ist True falls player_b "bot" heisst sonst False
bot_mode = (player_b == "bot")
bot_difference = 70

# Score
score_a = 0
score_b = 0

# Werte zur Ballbewegung
start_speed = 0.5
speed_up = 0.1
dir_x = 1
dir_y = 1

# Funktion um die Paddles neu zu setzen
def place_paddles():
    global paddle_a
    global paddle_b
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)

# Funktion um den Ball neu zu starten
def restart_ball():
    global ball
    global speed
    speed = start_speed
    ball.goto(0, 0)
    ball.color("black")
    ball.dx = speed * dir_x
    ball.dy = speed * dir_y

# Funktion um das Spiel neu zu starten
def restart():
    global score_a
    global score_b
    global score_board

    # Score wieder auf Null setzen
    score_a = 0
    score_b = 0

    # Scoreboard neu aufbauen
    score_board.clear()
    score_board.color("orange")
    score_board.write("{}: {} {}: {}".format(player_a, score_a, player_b, score_b), align="center",
                      font=("Courier", 24, "normal"))

    # Ball und Paddles neu starten
    restart_ball()
    place_paddles()

# Funktion um das linke Paddle hoch zu bewegen
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 40
    paddle_a.sety(y)

# Funktion um das linke Paddle runter zu bewegen
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 40
    paddle_a.sety(y)

# Funktion um das rechte Paddle hoch zu bewegen
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 40
    paddle_b.sety(y)

# Funktion um das rechte Paddle runter zu bewegen
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 40
    paddle_b.sety(y)

# Ball erzeugen
ball = turtle.Turtle()
ball.shape("square")
ball.penup()
speed = start_speed

# Ball erstmalig starten
restart_ball()

# Paddle A erzeugen
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()

# Paddle B erzeugen
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()

# Beide Paddles erstmalig platzieren
place_paddles()

# Scoreboard erzeugen
score_board = turtle.Turtle()
score_board.clear()
score_board.speed(0)
score_board.color("orange")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("{}: {} {}: {}".format(player_a, score_a, player_b, score_b),
                  align="center", font=("Courier", 24, "normal"))

# Oben definierte Funktionen zum Neustart und zur Paddle-Bewegung mit Tasten verbinden
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
# Den rechten Spieler nur verbinden wenn er kein Bot ist
if not bot_mode:
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(restart, "r")

# Das Spiel selbst, dieser Teil wird immer wieder wiederholt
while True:
    wn.update()

    # Bewegung Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bewegung des rechten Paddles falls der rechte Spieler der Bot ist
    if bot_mode:
        if ball.ycor() > paddle_b.ycor() + bot_difference:
            paddle_b_up()
        if ball.ycor() < paddle_b.ycor() - bot_difference:
            paddle_b_down()

    # Check ob man an der rechten Spielfeldgrenze ist
    if ball.ycor() > 290:
        ball.sety(290)
        dir_y *= -1
        ball.dy = speed * dir_y

    # Check ob man an der linken Spielfeldgrenze ist
    if ball.ycor() < -290:
        ball.sety(-290)
        dir_y *= -1
        ball.dy = speed * dir_y

    # Check ob man an der oberen Spielfeldgrenze ist
    if ball.xcor() > 390:
        dir_x *= -1
        restart_ball()
        score_a += 1
        score_board.clear()
        score_board.color("blue")
        score_board.write("{}: {} {}: {}".format(player_a, score_a, player_b, score_b), align="center",
                          font=("Courier", 24, "normal"))

    # Check ob man an der unteren Spielfeldgrenze ist
    if ball.xcor() < -390:
        dir_x *= -1
        restart_ball()
        score_b += 1
        score_board.clear()
        score_board.color("red")
        score_board.write("{}: {} {}: {}".format(player_a, score_a, player_b, score_b), align="center",
                          font=("Courier", 24, "normal"))

    # Check ob der Ball auf das rechte Paddle trifft
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        if speed < max_speed:
            speed += speed_up
        dir_x *= -1
        ball.dx = speed * dir_x
        ball.dy = speed * dir_y
        ball.color("red")


    # Check ob der Ball auf das linke Paddle trifft
    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        if speed < max_speed:
            speed += speed_up
        dir_x *= -1
        ball.dx = speed * dir_x
        ball.dy = speed * dir_y
        ball.color("blue")

    # Check ob der linke Spieler gewonnen hat
    if score_a == rounds:
        speed = 0
        ball.dx = speed * dir_x
        ball.dy = speed * dir_y
        score_board.clear()
        score_board.write("{} wins {} : {}. Press r to restart".format(player_a, score_a, score_b), align="center",
                          font=("Courier", 24, "normal"))

    # Check ob der rechte Spieler gewonnen hat
    if score_b == rounds:
        speed = 0
        ball.dx = speed * dir_x
        ball.dy = speed * dir_y
        score_board.clear()
        score_board.write("{} wins {} : {}. Press r to restart".format(player_b, score_b, score_a), align="center",
                          font=("Courier", 24, "normal"))
