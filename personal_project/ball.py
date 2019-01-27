from turtle import *


class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)
		self.dx=dx
		self.dy=dy
		self.r=r


	def move(self):
		current_x= self.xcor()
		current_y= self.ycor()
		new_x= current_x+self.dx
		new_y= current_y+self.dy
		doughnut_radius=440
		self.goto(new_x,new_y)


		d= ((new_x-0)**2+(new_y-0)**2)**0.5
		if d>=doughnut_radius+self.r:
			self.dx= self.dx*-1
			self.dy=self.dy*-1
'''
	def move(self, screen_width, screen_height):
		current_x= self.xcor()
		current_y= self.ycor()
		new_x= current_x+self.dx
		new_y= current_y+self.dy
		right_side_ball= new_x+self.r
		left_side_ball= new_x-self.r
		up_side_ball= new_y+self.r
		down_side_ball= new_y-self.r
		self.goto(new_x, new_y)

		if (up_side_ball>=screen_height) or (down_side_ball<=(screen_height)*-1) :
			self.dy= self.dy*-1
		elif (right_side_ball>=screen_width) or (left_side_ball<=(screen_width)*-1):
			self.dx= self.dx*-1
'''