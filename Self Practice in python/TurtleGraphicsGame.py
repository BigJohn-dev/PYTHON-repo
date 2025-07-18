import turtle
import random
import math

# Set up the screen
screen = turtle.Screen()
screen.title("COHORT 25: PATHFINDERS")
screen.bgcolor("#181824")
screen.setup(width=800, height=600)

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
    (-350, 250), (-100, 250), (150, 250), (400, 250),
    (-350, 50), (-100, 50), (150, 50), (400, 50),
    (-200, -150), (100, -150), (350, -150)
]

colors = [
    "#FF5F57", "#FFBD2E", "#28C940", "#0074D9", "#B10DC9",
    "#FFDC00", "#39CCCC", "#F012BE", "#3D9970", "#85144b", "#7FDBFF"
]

def draw_hud(text):
    pen.goto(0, 340)
    pen.color("#F8F8F2")
    pen.write(text, align="center", font=("Verdana", 32, "bold"))

def draw_glow_circle(center_x, center_y, radius, color):
    # Draw a glowing circle behind the names
    pen.goto(center_x, center_y - radius)
    pen.pendown()
    pen.pensize(4)
    pen.color(color)
    pen.setheading(0)
    pen.circle(radius)
    pen.penup()
    pen.pensize(1)

def draw_names_circle(names, center_x, center_y, radius=70, color="white"):
    # Draw glow
    draw_glow_circle(center_x, center_y, radius + 10, color)
    # Draw names in a circle
    angle_gap = 360 / len(names)
    for i, name in enumerate(names):
        angle = angle_gap * i
        rad = math.radians(angle)
        x = center_x + radius * math.cos(rad)
        y = center_y + radius * math.sin(rad)
        pen.goto(x, y)
        pen.setheading(angle)
        pen.color(color)
        pen.write(name, align="center", font=("Arial", 12, "bold"))

def animate_intro():
    # Simple animation for intro
    pen.goto(0, 0)
    pen.color("#FFBD2E")
    for size in range(10, 180, 10):
        pen.clear()
        pen.pensize(4)
        pen.pendown()
        pen.circle(size)
        pen.penup()
        screen.update()
    pen.clear()

screen.tracer(0)  # Turn off animation for fast drawing

animate_intro()
draw_hud("Meet the PATHFINDERS...")

# Draw all name groups
used_colors = []
for group, pos in zip(groups, positions):
    available_colors = [c for c in colors if c not in used_colors]
    if not available_colors:
        available_colors = colors
    color = random.choice(available_colors)
    used_colors.append(color)
    draw_names_circle(group, pos[0], pos[1], radius=70, color=color)

screen.update()
screen.exitonclick()