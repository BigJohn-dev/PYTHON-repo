import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("COHORT 25: PATHFINDERS")
screen.bgcolor("black")
screen.setup(width=900, height=700)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

groups = [
    ["Bolaji", "Damilare", "Oba"],
    ["Tega", "Olamide-boy", "Eddy"],
    ["Gift", "Justine", "Purity", "Big-John"],
    ["Helen", "Ibrahim", "Motunrayo", "Kelvin"],
    ["Justice", "Hilary", "Lotana"],
    ["Tomide", "Olamide-girl", "Hassan", "Wonder"],
    ["Timothy", "Abigail", "Theophilus", "John-Chi"],
    ["Emmanuel", "James", "Caleb", "Okafor"],
    ["Rahim", "Augustine"],
    ["Ekwe", "Ayomide", "Rasaq"],
    ["Domingo", "Chijioke", "Debola", "Wale"]
]

positions = [
    (-300, 200), (-100, 200), (100, 200), (300, 200),
    (-300, 0), (-100, 0), (100, 0), (300, 0),
    (-200, -200), (0, -200), (200, -200)
]

colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "magenta", "lime", "pink"]

def draw_hud(text):
    pen.goto(0, 310)
    pen.color("white")
    pen.write(text, align="center", font=("Arial", 24, "bold"))

def draw_names_circle(names, center_x, center_y, radius=60, color="white"):
    pen.color(color)
    angle_gap = 360 / len(names)
    for i, name in enumerate(names):
        pen.setheading(angle_gap * i)
        pen.goto(center_x, center_y)
        pen.forward(radius)
        pen.write(name, align="center", font=("Arial", 10, "bold"))

# Draw the HUD text first
draw_hud("Meet the PATHFINDERS...")

# Draw all name groups first
used_colors = []
for group, pos in zip(groups, positions):
    available_colors = [c for c in colors if c not in used_colors]
    if not available_colors:
        available_colors = colors
    color = random.choice(available_colors)
    used_colors.append(color)
    draw_names_circle(group, pos[0], pos[1], radius=60, color=color)

screen.exitonclick()
