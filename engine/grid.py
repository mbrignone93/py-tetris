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

	def is_inside(self, row, column):
		return row >= 0 and row < self.number_rows and column >= 0 and column < self.number_columns

	def is_empty(self, row, column):
		if self.grid[row][column] == 0:
			return True
		return False

	def is_row_full(self, row):
		for column in range(self.number_columns):
			if self.grid[row][column] == 0:
				return False
		return True

	def clear_row(self, row):
		for column in range(self.number_columns):
			self.grid[row][column] = 0

	def move_row_down(self, row, number_rows):
		for column in range(self.number_columns):
			self.grid[row + number_rows][column] = self.grid[row][column]
			self.grid[row][column] = 0

	def clear_full_rows(self):
		completed = 0
		for row in range(self.number_rows -1, 0, -1):
			if self.is_row_full(row):
				self.clear_row(row)
				completed += 1
			elif completed > 0:
				self.move_row_down(row, completed)
		return completed

	def reset(self):
		for row in range(self.number_rows):
			for column in range(self.number_columns):
				self.grid[row][column] = 0
	
	def draw(self, screen):
		for row in range(self.number_rows):
			for column in range(self.number_columns):
				cell_value = self.grid[row][column]
				cell_rect = pygame.Rect(column * self.cell_size + 1, row * self.cell_size + 1, 
					self.cell_size - 1, self.cell_size - 1)
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)