from turtle import Turtle
import random
import math
colliding=False

class Ball(Turtle):
	def __init__(self, radius, color, x, y, dx,dy):
		Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.shape("circle")
		self.shapesize(radius/10)
		self.rad =radius
		self.color(color)
		self.x= x
		self.y=y
		self.goto(self.x,self.y)
		self.showturtle()
		self.dx= dx
		self.dy=dy
	def move(self, height, width):
		newx= self.xcor()+self.dx
		newy= self.ycor()+self.dy
		self.goto(newx,newy)
		if (newx>width/2) or (newx< -1*width/2):
			self.dx= dx*-1
		elif (newy> height/2) or (newy< height*-1/2):
			self.dy= -1*dy

def check_collision(a,b):
	x1= a.xcor()
	y1= a.ycor()
	x2= b.xcor()
	y2= b.ycor()
	colliding=False
	d=  math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

	if d <= (a.rad+b.rad):
		colliding=True
	return(colliding)

a= Ball(20, "pink",100,100, 10, 20, )
b= Ball(30, "green", -100, -100, 20)

while True:
	

	a.move()
	b.move()

	



	c=check_collision(a,b)
	print(c)
turtle.mainloop()