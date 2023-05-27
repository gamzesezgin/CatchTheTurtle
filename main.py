import turtle
import random

# Değişkenler
screen = turtle.Screen()
game_over = False
score = 0
FONT = ('Arial', 20, 'normal')
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

# turtle liste
turtles = []

#countdown liste
count_down_turtle = turtle.Turtle()

# Score turtle
score_turtle = turtle.Turtle()

# Puanı güncelleyen fonksiyon
def update_score():
    score_turtle.hideturtle()
    score_turtle.color("white")
    score_turtle.penup()

    score_turtle.goto(0, 250)
    score_turtle.write("Score: {}".format(score), move = False, align = "center", font = FONT)

grid_size = 10

def make_turtle (x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score), align = "center", font = FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    t.pendown()
    turtles.append(t)

x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtles:
        t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtles).showturtle()
        screen.ontimer(show_turtles_randomly, 500)

# Zamanı gösteren fonksiyon
def countdown(time):
    global game_over
    count_down_turtle.color("white")
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.goto(0, 280)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write("Time: {}".format(time), move = False, align = "center", font = FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)  # 1 saniye sonra fonksiyonu tekrar çağır.
    else:
        game_over = True
        count_down_turtle.clear()
        hide_turtles()
        count_down_turtle.write("Game Over!", align = "center", font = FONT)

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    update_score()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game_up()
turtle.mainloop()