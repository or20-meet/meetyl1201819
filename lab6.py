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
