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

running = True

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.KEYDOWN:
			if game.game_over == True:
				game.game_over = False
				game.reset()

			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()

		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

	#drawing
	screen.fill(dar_blue)
	game.draw(screen)

	pygame.display.update()
	clock.tick(60) # <-- using 60 FPS