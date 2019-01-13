import turtle
import math
import time
import random
import ball
from ball import Ball

turtle.penup()
turtle.tracer(1)
turtle.hideturtle()

global running, sleep, screen_width, screen_height
running = True
sleep= 0.0077
screen_width= turtle.getcanvas().winfo_width()/2
screen_height= turtle.getcanvas().winfo_height()/2

number_of_balls=5
minimum_ball_radius= 10
maximum_ball_radius= 100
minimum_ball_dx= -5
maximum_ball_dx= 5
minimum_ball_dy= -5
maximum_ball_dy= 5
balls=[]

my_ball= Ball(0, 0, 2, 2, 50, "green")

for i in range(number_of_balls):
	x=  random.randint(maximum_ball_radius-screen_width, screen_width-maximum_ball_radius)
	y= random.randint(maximum_ball_radius - screen_height, screen_height- maximum_ball_radius)
	dx=0
	while dx==0:
		dx= random.randint(minimum_ball_dx  , maximum_ball_dx)
	dy=0
	while dy==0:
		dy= random.randint(minimum_ball_dy, maximum_ball_dy)
	radius= random.randint(minimum_ball_radius, maximum_ball_radius)
	color= (random.random(), random.random(), random.random())
	new_ball= Ball(x, y, dx, dy, radius, color)
	balls.append(new_ball)

for ball in balls:
	ball.move(screen_width, screen_height)

def collide(ball1, ball2):
	if ball1==ball2:
		return False
	d= math.sqrt((ball1.xcor()-ball2.xcor())**2 + (ball1.ycor()-ball2.ycor()**2))
	if  ball1.r+ ball2.r<= d +10 :
		return True
	else:
		return False


def check_all_collision():
	for ball1 in balls:
		for ball2 in balls:
			if collide(ball1, ball2):
				rad1= ball1.r
				rad2= ball2.r 
				if ball1.r> ball2.r:
					ball2= Ball()
turtle.mainloop()