import turtle
import math
import time
import random
import ball
from ball import Ball

turtle.penup()
turtle.tracer(0,0)
turtle.hideturtle()

global running, sleep, screen_width, screen_height
running = True
sleep= 0.03
screen_width= int(turtle.getcanvas().winfo_width()/2)
screen_height= int(turtle.getcanvas().winfo_height()/2)

number_of_balls=6
minimum_ball_radius= 10
maximum_ball_radius= 70
minimum_ball_dx= -5
maximum_ball_dx= 5
minimum_ball_dy= -5
maximum_ball_dy= 5
balls=[]

my_ball= Ball(0, 0, 2, 2, 50, "green")

#the following function randomizes the values of x, y, dx, dy, r, color
def randomize(ball):
	x= random.randint(maximum_ball_radius-screen_width, screen_width-maximum_ball_radius)
	y=random.randint(maximum_ball_radius - screen_height, screen_height- maximum_ball_radius)
	dx=0
	while dx==0:
		dx= random.randint(minimum_ball_dx  , maximum_ball_dx)
	dy=0
	while dy==0:
		dy= random.randint(minimum_ball_dy, maximum_ball_dy)
	radius= random.randint(minimum_ball_radius, maximum_ball_radius)
	color= (random.random(), random.random(), random.random())
	ball.goto(x,y)
	ball.dx=dx
	ball.dy=dy
	ball.r= radius
	ball.shapesize(ball.r/10)
	ball.color(color)

def random_ball():
	x= random.randint(maximum_ball_radius-screen_width, screen_width-maximum_ball_radius)
	y=random.randint(maximum_ball_radius - screen_height, screen_height- maximum_ball_radius)
	dx=0
	while dx==0:
		dx= random.randint(minimum_ball_dx  , maximum_ball_dx)
	dy=0
	while dy==0:
		dy= random.randint(minimum_ball_dy, maximum_ball_dy)
	radius= random.randint(minimum_ball_radius, maximum_ball_radius)
	color= (random.random(), random.random(), random.random())
	return Ball(x, y, dx, dy, radius, color)


for i in range(number_of_balls):
	new_ball= random_ball()
	balls.append(new_ball)




def collide(ball1, ball2):
	if ball1==ball2:
		return False
	d= ((ball1.xcor()-ball2.xcor())**2 + (ball1.ycor()-ball2.ycor())**2)**0.5
	if  ball1.r+ ball2.r>= d +10 :
		return True
	else:
		return False



def check_all_collision():
	for ball1 in balls:
		for ball2 in balls:
			if collide(ball1, ball2):
				rad1= ball1.r
				rad2= ball2.r 
				if rad1> rad2:
					randomize(ball2)
					ball1.r+=1
					ball1.shapesize(ball1.r/10)
				elif rad2> rad1:
					randomize(ball1)
					ball2.r+=1
					ball2.shapesize(ball2.r/10)



def check_my_collision():
	for ball in balls:
		if collide(ball,my_ball):

			my_rad= my_ball.r
			ball_rad= ball.r
			if my_rad>ball_rad:
				my_ball.r+=1
				my_ball.shapesize(my_ball.r/10)
				randomize(ball)

			else:

				return False
	return True

#hoped@mit.edu

def movearound(event):
	x= event.x-screen_width
	y= screen_height-event.y
	my_ball.goto(x, y)


turtle.getcanvas().bind("<Motion>",movearound)
turtle.listen()

while running:
	if screen_width!= int(turtle.getcanvas().winfo_width()/2) or screen_height != int(turtle.getcanvas().winfo_height()/2):
		screen_width= int(turtle.getcanvas().winfo_width()/2)
		screen_height= int(turtle.getcanvas().winfo_height()/2)

	for ball in balls:
		ball.move(screen_width, screen_height)
	check_all_collision()
	running=check_my_collision()

	turtle.update()
	time.sleep(sleep)
