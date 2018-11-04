class animal(object):
	def __init__(self,sound, name, age, fav_color):
		self.sound=sound
		self.name=name
		self.age=age
		self.fav_color= fav_color
	def eat(self, food):
		print("yummy!"+self.name+"is eating"+ food)
	def desc(self):
		print(self.name+"is"+ self.age+"yearsold and loves the color"+ self.fav_color)
	def make_sound(self, x):
		print(self.sound*x)


d= animal("woof! ","rex","9","brown")
d.eat("kibble")
d.desc()
d.make_sound(12)



class person(object):
	def __init__(self,name,age,city,gender, breakfast, music):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
		self.breakfast=breakfast
		self.music=music
	def eat_breakfast(self):
		print(self.name+"is eating"+self.breakfast)
	
	def play_music(self):
		print(self.name+"plays the "+self.music)


m= person("mai",15, "jerusalem", "female","waffles", "guitar")

m.eat_breakfast()
m.play_music()