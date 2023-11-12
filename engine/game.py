#
#  Developed by Maximiliano Brignone 
#  https://github.com/mbrignone93
#  © 2023	
#

from engine.grid import Grid
from engine.pieces.i_block import IBlock
from engine.pieces.j_block import JBlock
from engine.pieces.l_block import LBlock
from engine.pieces.o_block import OBlock
from engine.pieces.s_block import SBlock
from engine.pieces.t_block import TBlock
from engine.pieces.z_block import ZBlock
from engine.levels import Levels
import pygame
import random

class Game:

	def __init__(self):
		self.grid = Grid()
		self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.game_over = False
		self.game_paused = False
		self.score = 0
		self.HIGHSCORE_FILE = "highscore.txt"
		self.rotate_sound = pygame.mixer.Sound("assets/sounds/rotate.ogg")
		self.clear_sound = pygame.mixer.Sound("assets/sounds/clear.ogg")
		self.level = 1
		self.lines = 0
		self.lines_per_level = 0

		file = open(self.HIGHSCORE_FILE, "r")
		self.highscore = file.read()

		pygame.mixer.music.load("assets/sounds/music.ogg")
		pygame.mixer.music.play(-1)
		
	def update_score(self, lines_cleared, move_down_points):
		if self.level < 10:
			if self.lines_per_level >= 10:
				self.lines_per_level = 0
				self.level += 1

			match lines_cleared:
				case 1:
					self.score += 40 * (self.level + 1)
				case 2:
					self.score += 100 * (self.level + 1)
				case 3:
					self.score += 300 * (self.level + 1)
				case 4:
					self.score += 1200 * (self.level + 1)

			self.score += move_down_points
			self.lines += lines_cleared
			self.lines_per_level += lines_cleared

	def set_highscore(self):
		if self.score > int(self.highscore):
			file = open(self.HIGHSCORE_FILE, "a")
			file.seek(0)
			file.truncate()
			file.write(str(self.score))
			file.close()

	def set_pause_or_resume_game(self):
		if self.game_paused == False:
			self.game_paused = True
		elif self.game_paused == True:
			self.game_paused = False

	def get_random_block(self):
		if len(self.blocks) == 0:
			self.blocks = [
				IBlock(), JBlock(), LBlock(), 
				OBlock(), SBlock(), TBlock(), 
				ZBlock()
			]

		block = random.choice(self.blocks)
		self.blocks.remove(block)
		return block

	def move_left(self):
		self.current_block.move(0, -1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, 1)

	def move_right(self):
		self.current_block.move(0, 1)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(0, -1)

	def move_down(self):
		self.current_block.move(1, 0)
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.move(-1, 0)
			self.lock_block()

	def lock_block(self):
		pygame.time.set_timer(pygame.USEREVENT, Levels.level[self.level])

		tiles = self.current_block.get_cell_positions()
		for position in tiles:
			self.grid.grid[position.row][position.column] = self.current_block.id
		self.current_block = self.next_block
		self.next_block = self.get_random_block()
		rows_cleared = self.grid.clear_full_rows()
		if rows_cleared > 0:
			self.clear_sound.play()
			self.update_score(rows_cleared, 0)
		if self.block_fits() == False:
			self.game_over = True

	def reset(self):
		self.grid.reset()
		self.blocks = [
			IBlock(), JBlock(), LBlock(), 
			OBlock(), SBlock(), TBlock(), 
			ZBlock()
		]
		self.current_block = self.get_random_block()
		self.next_block = self.get_random_block()
		self.set_highscore()
		self.score = 0
		self.level = 1
		self.lines = 0
		self.lines_per_level = 0
		file = open(self.HIGHSCORE_FILE, "r")
		self.highscore = file.read()

	def block_fits(self):
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_empty(tile.row, tile.column) == False:
				return False
		return True
			
	def rotate(self):
		self.current_block.rotate()
		if self.block_inside() == False or self.block_fits() == False:
			self.current_block.undo_rotation()
		else:
			self.rotate_sound.play()

	def move_to_floor(self):
		self.current_block.move_to_floor

	def block_inside(self):
		tiles = self.current_block.get_cell_positions()
		for tile in tiles:
			if self.grid.is_inside(tile.row, tile.column) == False:
				return False
		return True

	def draw(self, screen):
		self.grid.draw(screen)
		self.current_block.draw(screen, 11, 11)

		# only pieces I and O are custom drawn centralized 
		if self.next_block.id == 1:
		 	self.next_block.draw(screen, 255, 430)
		elif self.next_block.id == 4:
		 	self.next_block.draw(screen, 255, 415)
		else:
		 	self.next_block.draw(screen, 270, 415)