import turtle as t
import random


class HirstBase(t.Turtle):
	def __init__(self, dot_number, step_size):
		t.Turtle.__init__(self)
		self.start_pos_index = -200
		self.dot_line_number = dot_number
		self.step_size = step_size
		self.speed(50)
		self.pensize(10)
		t.colormode(255)
		self.hideturtle()
		self.penup()
		self.setposition(self.start_pos_index, self.start_pos_index)

	def create_dots(self, colors):
		for i in range(self.dot_line_number):
			for j in range(self.dot_line_number):
				color = random.choice(colors)
				self.color(color.rgb)
				self.dot()
				self.penup()
				self.forward(self.step_size)
			self.setposition(self.start_pos_index, self.start_pos_index + (i + 1) * self.step_size)


