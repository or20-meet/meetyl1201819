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

#the following function randomize the values of x, y, dx, dy, r, color
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
	ball.color=color

for i in range(number_of_balls):
	new_ball= Ball(1,1,1,1,1,"green")
	randomize(new_ball)
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
				if rad1> rad2:
					randomize(ball2)
					ball1.r+=1
				elif rad2> rad1:
					randomize(ball1)
					ball2.r+=1



def check_my_collision():
	for ball in balls:
		if collide(ball,my_ball):
			my_rad= my_ball.r
			ball_rad= ball.r
			if my_rad>ball_rad:
				my_ball.r+=1
				randomize(ball)

			elif ball_rad>my_rad:
				return False
	return True



def movearound(event):
	x= event.x-screen_width
	y= screen_height-event.y
	my_ball.goto(x, y)


turtle.getcanvas().bind("<Motion>",movearound)
turtle.listen()
turtle.mainloop()