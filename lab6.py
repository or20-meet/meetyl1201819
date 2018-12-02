'''
from turtle import Turtle
import turtle
import random

class Square(Turtle):
	def __init__(self, sz):
		Turtle.__init__(self)
		self.sz= sz
		self.shape("square")
		self.shapesize(sz)

	def random_color(self):
		colors= ["red", "orange", "pink"]
		c= random.randint(0,2)
		self.color(colors[c])

s= Square(5)
s.random_color()
turtle.mainloop()
'''





from turtle import Turtle
import turtle

class Hexagon(Turtle): 
	def __init__(self, size):
		Turtle.__init__(self)
		self.size=size
		turtle.penup()

		

		turtle.begin_poly()
		for i in range(6):
			turtle.fd(100)
			turtle.right(60)
		turtle.end_poly()
		s= turtle.get_poly()
		turtle.register_shape("hexagon", s)
		self.shape("hexagon")
		self.shapesize(self.size)


t1= Hexagon(2)

turtle.mainloop()





