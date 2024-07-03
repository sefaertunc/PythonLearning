from turtle import Turtle


class CreateTurtle(Turtle):
	def __init__(self, color, pos):
		super().__init__()
		self.color(color)
		self.shape("turtle")
		self.penup()
		self.setposition(pos)

	def move_forward(self, speed):
		self.forward(speed)
