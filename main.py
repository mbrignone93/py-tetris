#
#  Developed by Maximiliano Brignone 
#  https://github.com/mbrignone93
#  © 2023	
#

import pygame
import sys
from ui.grid import Grid
from engine.pieces.i_block import IBlock
from engine.pieces.j_block import JBlock
from engine.pieces.l_block import LBlock
from engine.pieces.o_block import OBlock
from engine.pieces.s_block import SBlock
from engine.pieces.t_block import TBlock
from engine.pieces.z_block import ZBlock

pygame.init()
dar_blue = (44, 44, 127)

icon = pygame.image.load('assets/icon.png')
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Py-Tetris")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

game_grid = Grid()

block = LBlock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#drawing
	screen.fill(dar_blue)
	game_grid.draw(screen)
	block.draw(screen)

	pygame.display.update()
	clock.tick(60) # <-- using 60 FPS