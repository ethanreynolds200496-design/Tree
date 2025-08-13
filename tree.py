import random
import turtle

# -------- settings you can tweak --------
BRANCH_LENGTH = 100    # starting branch length
ANGLE_RANGE = (18, 28) # min and max split angle
SHRINK_RANGE = (0.65, 0.78)  # how much each branch shrinks
MIN_LENGTH = 8         # stop when branches get this short
TRUNK_THICKNESS = 12
LEAF_SIZE = 6
BACKGROUND = "#0b132b"
TRUNK_COLOUR = "#5b3924"
LEAF_COLOUR = "#0fbf69"
SCREEN_SIZE = (900, 800)
# ----------------------------------------

def setup_screen():
    screen = turtle.Screen()
    screen.setup(*SCREEN_SIZE)
    screen.title("Fractal Tree")
    screen.bgcolor(BACKGROUND)
    return screen

def setup_turtle():
    t = turtle.Turtle(visible=False)
    t.speed(0)  # fastest
    t.left(90)  # point upwards
    t.penup()
    t.goto(0, -SCREEN_SIZE[1] // 2 + 50)  # start near bottom centre
    t.pendown()
    t.color(TRUNK_COLOUR)
    t.pensize(TRUNK_THICKNESS)
    return t

def draw_leaf(t):
    # draw a simple dot as a leaf without changing heading
    t.color(LEAF_COLOUR)
    t.dot(LEAF_SIZE)
    t.color(TRUNK_COLOUR)

def draw_branch(t, length, thickness):
    if length < MIN_LENGTH:
        draw_leaf(t)
        return

    t.pensize(thickness)
    t.forward(length)

    # randomised split parameters for a natural look
    angle_left = random.uniform(*ANGLE_RANGE)
    angle_right = random.uniform(*ANGLE_RANGE)
    shrink_left = random.uniform(*SHRINK_RANGE)
    shrink_right = random.uniform(*SHRINK_RANGE)

    # left branch
    t.left(angle_left)
    draw_branch(t, length * shrink_left, max(1, thickness * shrink_left * 0.8))

    # right branch
    t.right(angle_left + angle_right)
    draw_branch(t, length * shrink_right, max(1, thickness * shrink_right * 0.8))

    # restore heading and position
    t.left(angle_right)
    t.up()
    t.backward(length)
    t.down()

def main():
    screen = setup_screen()
    t = setup_turtle()
    turtle.tracer(False)  # draw instantly
    draw_branch(t, BRANCH_LENGTH, TRUNK_THICKNESS)
    turtle.tracer(True)
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
