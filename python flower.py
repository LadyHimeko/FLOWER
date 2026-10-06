import turtle

# Set up the screen
sc = turtle.Screen()
sc.setup(500, 500)
sc.bgcolor('black')

# Set up the turtle pen
pen = turtle.Turtle()
pen.pensize(4)
pen.speed(20)

# Colors for petals
col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
i = 0

# Draw 30 circles to make a flower shape
for angle in range(0, 360, 12):
    pen.color(col[i])
    if i == 6:
        i = 0
    else:
        i += 1
    
    pen.seth(angle)
    pen.circle(80)

# Hide the turtle when done
pen.ht()
turtle.done()
