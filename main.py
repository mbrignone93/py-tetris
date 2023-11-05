#
#  Developed by Maximiliano Brignone 
#  https://github.com/mbrignone93
#  © 2023	
#

import pygame
import sys
from engine.game import Game

pygame.init()
dar_blue = (44, 44, 127)

icon = pygame.image.load('assets/icon.png')
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Py-Tetris")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

game = Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				game.move_left()
			if event.key == pygame.K_RIGHT:
				game.move_right()
			if event.key == pygame.K_DOWN:
				game.move_down()

	#drawing
	screen.fill(dar_blue)
	game.draw(screen)

	pygame.display.update()
	clock.tick(60) # <-- using 60 FPS