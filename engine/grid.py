#
#  Developed by Maximiliano Brignone 
#  https://github.com/mbrignone93
#  © 2023	
#

import pygame
from engine.colors import Colors

class Grid:

	def __init__(self):
		self.number_rows = 20
		self.number_columns = 10
		self.cell_size = 30
		self.grid = [[0 for j in range(self.number_columns)] for i in range(self.number_rows)]
		self.colors = Colors.get_cell_colors()

	def print_grid(self):
		for row in range(self.number_rows):
			for column in range(self.number_columns):
				print(self.grid[row][column], end = " ")
			print() 

	def is_inside(self, row, column):
		return row >= 0 and row < self.number_rows and column >= 0 and column < self.number_columns

	def draw(self, screen):
		for row in range(self.number_rows):
			for column in range(self.number_columns):
				cell_value = self.grid[row][column]
				cell_rect = pygame.Rect(column * self.cell_size + 1, row * self.cell_size + 1, 
					self.cell_size - 1, self.cell_size - 1)
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)