import turtle

#create a turtle object
t1 = turtle.Turtle()

#program t1 to do stuff
def setup():
  t1.penup()
  t1.color("lightblue")
  t1.shape("turtle")
  t1.goto(-200,-200)
  t1.pendown()
  t1.goto(200,-200)
  
t1.shape("turtle")

def forLoops():
  t1.speed(20)
  t1.penup()
  t1.goto(0,0)
  t1.pendown()
  for i in range(4):
    for i in range(4):
      t1.fd(100)
      t1.left(90)
    t1.left(90)


def two():
  t1.penup()
  t1.speed(10)
  t1.goto(0,-200)
  t1.left(90)
  t1.pendown()
  for i in range(40):
    t1.forward(10)
    t1.right(90)
    t1.forward(10)
    t1.forward(-20)
    t1.forward(10)
    t1.left(90)

def three():
  t1.speed(10)
  for i in range(3):
    t1.fd(100)
    t1.left(120)
  for i in range(4):
    t1.forward(100)
    t1.left(90)
  for i in range(5):
    t1.forward(100)
    t1.left(90)
  for i in range(6):
    t1.forward(100)
    t1.left(90)
  for i in range(7):
    t1.forward(100)
    t1.left(90)


def four():
  t1.pensize(10)
  for i in range(1):
    t1.color("red")
    t1.left(90)
    t1.forward(100)
    t1.forward(-100)
    t1.color("green")
    t1.forward(-100)
  t1.forward(100)
  t1.color("blue")
  t1.right(90)
  t1.forward(100)
  t1.forward(-100)
  t1.color("yellow")
  t1.forward(-100)

def five():
  t1.goto(0,0)
  t1.speed(10)
  for i in range(1):
    t1.pendown()
    t1.circle(i * 10)
  

def six():
  for i in range(50):
    for x in range(4):
      t1.circle(i*5)
      t1.left(90)

def seven():
  t1.speed(0)
  for i in range(36):
    t1.color("red")
    t1.circle(50)
    t1.left(10)
    t1.color("blue")
    t1.circle(100)
    

seven()