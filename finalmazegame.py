import turtle
import random as rand 
import math
#Final Project - Turtle Maze Game CS111
#authors: Saima Ashrafi, Lizeth Fernandez, Pasha Sheikh
turtle.hideturtle()
# Global variables
lives = ''
score = 0
level = ''

easy_walls = []
hard_walls = []
play = True
t= turtle.Turtle()
t.hideturtle()
s = turtle.Screen()
score_turtle = turtle.Turtle()
score_turtle.hideturtle()


maze_turtle = turtle.Turtle()
maze_turtle.hideturtle()

trace_turtle = turtle.Turtle()
trace_turtle.hideturtle()

coin_turtle = turtle.Turtle()
coin_turtle.hideturtle()

button_turtle = turtle.Turtle()
button_turtle.hideturtle()

button_easy = turtle.Turtle()
button_easy.hideturtle()

button_hard = turtle.Turtle()
button_hard.hideturtle()

maze_create = turtle.Turtle()
maze_create.hideturtle()

end_turtle = turtle.Turtle()
end_turtle.hideturtle()

maze_player = turtle.Turtle()
maze_player.hideturtle()

lose_turtle = turtle.Turtle()
lose_turtle.hideturtle()

win_turtle = turtle.Turtle()
win_turtle.hideturtle

yes_button = turtle.Turtle()
yes_button.hideturtle()

no_button = turtle.Turtle()
no_button.hideturtle()

# Setup Screen
def setup_screen(x, y):
    yes_button.hideturtle()
    score_turtle.clear()
    no_button.hideturtle()
    lose_turtle.clear()
    win_turtle.clear()
    s.bgcolor("purple")
    t.shape("square")
    t.width(3)
    t.hideturtle()
    t.penup()
    t.goto(0, 150)
    t.color("White")
    t.write("Welcome to Turtle Maze Game!", align = "center", font = ("Courier", 40, "bold"))
    
    title_screen(s, t)



# Title screen
# on click "start" button -> go to level choose screen

def title_screen(x, y):
    turtle.hideturtle()
    t.goto(0, 50)
    t.write("Click the square to start!", align = "center", font = ("Courier", 24, "bold"))
    
    button_turtle.shape("square")
    button_turtle.color("yellow")
    button_turtle.penup()
    button_turtle.shapesize(stretch_wid = 4, stretch_len = 6)
    button_turtle.goto(0, -80)
    button_turtle.showturtle()
    button_turtle.onclick(choose_level)
# Level choose screen
# on click "easy" button -> go to easy level , etc

def choose_level(x = None, y = None):
    global lives 
    global score
    
    yes_button.hideturtle()
    no_button.hideturtle()
    lose_turtle.clear()
    win_turtle.clear()
    score_turtle.clear()

    
    score = 0
    #update_score()
    t.clear()
    s.bgcolor("yellow")
    t.color("Black")
    button_turtle.hideturtle()
    t.penup()
    t.goto(0, 160)
    t.write("Choose a level!", align = "center", font = ("Courier", 60, "bold"))
    t.goto(0, 80)
    t.write("The Green Button is for the Easy level", align = "center", font = ("Courier", 30, "bold"))
    t.goto(0, 30)
    t.write("The Red Button is for the Hard level", align = "center", font = ("Courier", 30, "bold"))

    #easy button creation
    
    button_easy.shape("square")
    button_easy.color("green")
    button_easy.penup()
    button_easy.goto(-150, -100)
    button_easy.shapesize(stretch_wid = 2, stretch_len = 4)
    button_easy.showturtle()


    #hard button creation

    button_hard.shape("square")
    button_hard.color("red")
    button_hard.penup()
    button_hard.goto(150, -100)
    button_hard.shapesize(stretch_wid = 2, stretch_len = 4)
    button_hard.showturtle()

    button_easy.onclick(easy)
    button_hard.onclick(hard)

    


    

# Maze creation
# create Maze - drawn by turtle?
# set maze boundaries - if player touches, then lose a life
# set coins? - when player collects coin, in increase score
# Easy Maze

def easy(x,y):
    global maze_player
    global level
    global lives
    lives = 3
    level = "Easy"
    button_easy.hideturtle()
    button_hard.hideturtle()
    s.bgcolor("white")
    t.clear()
    t.penup()
    t.goto(0, 300)
    t.color("Black")
    t.write("Easy Maze", align = "center", font = ("Courier", 45, "bold"))
    t.penup()
    
    create_easy_maze()
    
    update_score()
    maze_player.penup()
    # easy: -250, -80
    maze_player.goto(-250, -80) # sets player turtle to start at easy start location
    create_move_player()

    for i in range(3):
        x = rand.randint(-200, 200)
        y = rand.randint(-200, 200)
        draw_coin(x,y)

# Draw the Easy Maze

def create_easy_maze():
    maze_create.goto(0,0)
    maze_create.showturtle()
    maze_create.speed(0)
    maze_create.penup()
    maze_create.goto(-220, 0)
    maze_create.pensize(5)
    file = open("easymazewalls")
    lines = file.readlines()
    easy_walls.clear()
    for wall in lines:
        wall = wall.strip()
        walls = ""
        for ch in wall:
            if ch != "(" and ch!= ")":
                walls += ch
        walls = walls.split(",")
        for i in range(len(walls)):
            walls[i] = float(walls[i])
        easy_walls.append(((walls[0], walls[1]), (walls[2], walls[3])))
    for line in easy_walls:
        (start_x, start_y), (end_x, end_y) = line
        maze_create.goto(start_x, start_y)
        maze_create.pendown()
        maze_create.goto(end_x, end_y)
        maze_create.penup()
    maze_create.hideturtle()
    end_turtle.speed(0)
    end_turtle.penup()
    end_turtle.goto(-97, 280)
    end_turtle.color("orange")
    end_turtle.begin_fill()
    for i in range(2):
        end_turtle.forward(80)
        end_turtle.right(90)
        end_turtle.forward(40)
        end_turtle.right(90)
    end_turtle.end_fill()
    end_turtle.penup()
    end_turtle.hideturtle()
    maze_create.hideturtle()
    

# Hard Maze
def hard(x,y):
    global maze_player
    global level
    global lives
    t.clear()
    level = "Hard"
    lives = 5
    button_easy.hideturtle()
    button_hard.hideturtle()
    s.bgcolor("white")
    t.color("Black")
    t.penup()
    t.goto(0,300)
    t.pendown()
    t.write("Hard Maze", align = "center", font = ("Courier", 40, "bold"))
    trace_turtle.showturtle()
    trace_turtle.penup()
    trace_turtle.speed(0)
    trace_turtle.goto(325,-290)
    trace_turtle.pensize(5)
    trace_turtle.pendown()
    file = open("hardmazewalls")
    lines = file.readlines()
    hard_walls.clear()
    for wall in lines:
        wall = wall.strip()
        walls = ""
        for ch in wall:
            if ch != "(" and ch!= ")":
                walls += ch
        walls = walls.split(",")
        for i in range(len(walls)):
            walls[i] = float(walls[i])
        hard_walls.append(((walls[0], walls[1]), (walls[2], walls[3])))
    for wall in hard_walls:
        (start_x, start_y), (end_x, end_y) = wall
        trace_turtle.goto(start_x, start_y)
        trace_turtle.pendown()
        trace_turtle.goto(end_x, end_y)
        trace_turtle.penup()
    maze_player.penup()
    maze_player.goto(325,-260)
    end_turtle.speed(0)
    end_turtle.penup()
    end_turtle.goto(-300, 315)
    end_turtle.color("orange")
    end_turtle.begin_fill()
    for i in range(2):
        end_turtle.forward(40)
        end_turtle.right(90)
        end_turtle.forward(80)
        end_turtle.right(90)
    end_turtle.end_fill()
    end_turtle.penup()
    end_turtle.hideturtle()
    update_score()
    create_move_player()
    for i in range(5):
        x = rand.randint(-200, 200)
        y = rand.randint(-200, 200)
        draw_coin(x,y)

# Turtle movement
# Pasha handled this already
# up, down, left, right

# Event Handlers

def create_move_player():
    global level
    global lives
    maze_player.showturtle()
    def move_player():
        if lives <= 0:
            lose_screen()
        maze_player.penup()
        maze_player.forward(4.5)
        if level == "Easy":
            check_collision_easy() 
            #-10, 280 -10, 240 -100, 280 -100, 240
            if (-100 <= maze_player.xcor() <= -10) and (240 <= maze_player.ycor() <= 280):
                print("Inside end point box")
                inside = True
                if score == 3 and inside:
                    win_screen()
        elif level == "Hard":
            check_collision_hard()
            if (-300 <= maze_player.xcor() <= -260) and (235 <= maze_player.ycor() <= 315):
                print("Inside end point box")
                inside = True
                if score == 5 and inside:
                    win_screen()
        coin_collision()
    def up():
        maze_player.setheading(90)
        move_player()
    def down():
        maze_player.setheading(270)
        move_player()
    def right():
        maze_player.setheading(0)
        move_player()
    def left():
        maze_player.setheading(180)
        move_player()

    # Create Player
    #maze_player = turtle.Turtle()
    maze_player.shape("turtle")
    maze_player.fillcolor("green")
    maze_player.penup()
    #maze_player.goto(0, 0)
    maze_player.pendown()
    

    s.onkey(up, "Up")
    s.onkey(down, "Down")
    s.onkey(right, "Right")
    s.onkey(left, "Left")
    s.listen()


# Collision checker


def check_collision_easy():
    global lives
    px, py = maze_player.position()
    tol_h = 2
    tol_v = 2
    
    for wall in easy_walls:
        (start_x, start_y), (end_x, end_y) = wall
        # horizontal walls
        if start_y == end_y and (min(start_x, end_x) <= px and px <= max(start_x, end_x)):
            if abs(py - start_y) <= tol_h:
                print("hit horizontal")
                print(abs(abs(py) - abs(start_y)))
                print("------------")
                lose_life()
                update_score()
                maze_player.goto(-250, -80)

        # vertical walls
        elif start_x == end_x and (min(start_y, end_y) <= py and py <= max(start_y, end_y)):
            if abs(px - start_x) <= tol_v:
                print("hit vertical")
                print(abs(abs(px) - abs(start_x)))
                print(px , "|", start_x)
                print("------------")
                lose_life()
                update_score()
                maze_player.goto(-250, -80)


def check_collision_hard():
    global lives
    px, py = maze_player.position()
    tol_h = 2
    tol_v = 2
    for wall in hard_walls:
        (start_x, start_y), (end_x, end_y) = wall
        # horizontal walls
        if start_y == end_y and (min(start_x, end_x) <= px and px <= max(start_x, end_x)):
            if abs(py - start_y) <= tol_h:
                print("hit horizontal")
                print(abs(abs(py) - abs(start_y)))
                print("------------")
                lose_life()
                update_score()
                maze_player.goto(325,-260)

        # vertical walls
        elif start_x == end_x and (min(start_y, end_y) <= py and py <= max(start_y, end_y)):
            if abs(px - start_x) <= tol_v:
                print("hit vertical")
                print(abs(abs(px) - abs(start_x)))
                print(px , "|", start_x)
                print("------------")
                lose_life()
                update_score()
                maze_player.goto(325,-260)


# Scoreboard - track lives and points
# I imagine this will work like the last turtle project we did - Liz

def update_score():
    global score
    global lives
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.goto(-600, -100)
    score_turtle.clear()

    score_turtle.write(f"Lives: {lives}", align = "left", font = ("Courier", 25, "bold"))
    score_turtle.goto(-600, -150)
    score_turtle.write(f"Score: {score}", align = "left", font = ("Courier", 25, "bold"))

coin_postions = []
def draw_coin(x,y):
    global easy_walls
    coin_turtle.hideturtle()
    coin_turtle.penup()
    
    def valid_position(x,y):
        if level == "Easy":
            for wall in easy_walls:
                (start_x, start_y), (end_x, end_y) = wall
                if start_y == end_y and (min(start_x, end_x) <= x <= max(start_x, end_x)):
                    if abs(y - start_y) < 10:
                        return False
                elif start_x == end_x and (min(start_y, end_y) <= y <= max(start_y, end_y)):
                    if abs(x - start_x) < 10:
                        return False
        elif level == "Hard":
            for wall in hard_walls:
                (start_x, start_y), (end_x, end_y) = wall
                if start_y == end_y and (min(start_x, end_x) <= x <= max(start_x, end_x)):
                    if abs(y - start_y) < 10:
                        return False
                elif start_x == end_x and (min(start_y, end_y) <= y <= max(start_y, end_y)):
                    if abs(x - start_x) < 10:
                        return False
        return True

    max_attempts = 100
    attempts = 0

    while not valid_position(x,y) and attempts < max_attempts:
        x = rand.randint(-200, 200)
        y = rand.randint(-200, 200)
        attempts += 1
        
    if attempts < max_attempts:
        coin_turtle.goto(x,y)
        coin_turtle.dot(20, "gold")
        coin_postions.append((x,y))

def coin_collision():
    global score, coin_postions
    for coin in coin_postions[:]:
        if maze_player.distance(coin) < 10:
            coin_postions.remove(coin)
            coin_turtle.penup()
            coin_turtle.goto(coin)
            coin_turtle.dot(20, "white")
            gain_point()

# Gain point when coin is collected
def gain_point():
    global score
    score += 1
    update_score()
    
    
# Lose life when turtle touches walls
def lose_life():
    global lives
    lives -= 1
    
    
        
        
    
# Win and Lose Screen Screens
# Win if player reached win threshold and completed the end of the maze 
# else lose
# try again? option
# quit option - ends program
# go to main menu screen - back to level selection screen
def win_screen():
    score_turtle.clear()
    score_turtle.hideturtle()
    maze_player.hideturtle()
    maze_create.clear()
    trace_turtle.clear()
    t.clear()
    end_turtle.clear()
    coin_turtle.clear()
    maze_player.clear()
    s.bgcolor('#b0faa7')
    win_turtle.penup()
    win_turtle.color('white')
    win_turtle.goto(0,0)
    win_turtle.pendown()
    win_turtle.write("Congratulations!! You Win!", align = "center", font = ("Courier", 40, "bold"))
    win_turtle.penup()
    win_turtle.goto(0, -30)
    win_turtle.pendown()
    win_turtle.write("Would you like to play again?", align = "center", font = ("Courier", 25))
    win_turtle.penup()

    #yes button
    yes_button.shape("square")
    yes_button.color("#579150")
    yes_button.penup()
    yes_button.goto(-150, -100)
    yes_button.shapesize(stretch_wid = 2, stretch_len = 4)
    yes_button.showturtle()
    win_turtle.goto(-150, -170)
    win_turtle.color("black")
    win_turtle.pendown()
    win_turtle.write("YES", align = "center", font = ("Courier", 25))
    win_turtle.penup()

    #no button
    no_button.shape("square")
    no_button.color("#579150")
    no_button.penup()
    no_button.goto(150, -100)
    no_button.shapesize(stretch_wid = 2, stretch_len = 4)
    no_button.showturtle()
    win_turtle.goto(150, -170)
    win_turtle.color('black')
    win_turtle.pendown()
    win_turtle.write("NO", align = "center", font = ("Courier", 25))
    win_turtle.penup()
    win_turtle.hideturtle()
    yes_button.onclick(choose_level)
    no_button.onclick(setup_screen)

def lose_screen():
    score_turtle.clear()
    score_turtle.hideturtle()
    maze_player.hideturtle()
    maze_create.clear()
    trace_turtle.clear()
    t.clear()
    end_turtle.clear()
    coin_turtle.clear()
    s.bgcolor('#bf8888')
    maze_player.clear()
    lose_turtle.penup()
    lose_turtle.color('black')
    lose_turtle.goto(0,0)
    lose_turtle.pendown()
    lose_turtle.write("Sorry, you lost :(", align = "center", font = ("Courier", 40, "bold"))
    lose_turtle.penup()
    lose_turtle.goto(0, -30)
    lose_turtle.pendown()
    lose_turtle.write("Would you like to try again?", align = "center", font = ("Courier", 25))
    lose_turtle.penup()

    #yes button
    #yes_button = turtle.Turtle()
    yes_button.penup()
    yes_button.shape("square")
    yes_button.color("#854141")
    yes_button.goto(-150, -100)
    yes_button.shapesize(stretch_wid = 2, stretch_len = 4)
    yes_button.showturtle()

    lose_turtle.goto(-150, -170)
    lose_turtle.color("white")
    lose_turtle.pendown()
    lose_turtle.write("YES", align = "center", font = ("Courier", 25))
    lose_turtle.penup()
    
    #no button
    #no_button = turtle.Turtle()
    no_button.penup()
    no_button.shape("square")
    no_button.color("#854141")
    no_button.goto(150, -100)
    no_button.shapesize(stretch_wid = 2, stretch_len = 4)
    no_button.showturtle()
    lose_turtle.goto(150, -170)
    lose_turtle.color('white')
    lose_turtle.pendown()
    lose_turtle.write("NO", align = "center", font = ("Courier", 25))
    lose_turtle.penup()
    lose_turtle.hideturtle()
    
    yes_button.onclick(choose_level)
    no_button.onclick(setup_screen)

setup_screen(s, t) 

s.mainloop()