#
#  Developed by Maximiliano Brignone 
#  https://github.com/mbrignone93
#  © 2023	
#

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
from engine.colors import Colors
from engine.game import Game

pygame.init()

title_font = pygame.font.Font(None, 40)

highscore_surface = title_font.render("Highscore", True, Colors.white)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)
game_paused_surface = title_font.render("PAUSE", True, Colors.white)

highscore_rect = pygame.Rect(320, 60, 170, 60)
score_rect = pygame.Rect(320, 195, 170, 60)
next_rect = pygame.Rect(320, 335, 170, 180)

icon = pygame.image.load('assets/icon.png')
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Py-Tetris")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

running = True

game = Game()

print("Py-Tetris running...")

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

			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()
			if event.key == pygame.K_LEFT or event.key == pygame.K_a and game.game_over == False and game.game_paused == False:
				game.move_left()
			if event.key == pygame.K_RIGHT or event.key == pygame.K_d and game.game_over == False and game.game_paused == False:
				game.move_right()
			if event.key == pygame.K_DOWN or event.key == pygame.K_s and game.game_over == False and game.game_paused == False:
				game.move_down()
				game.update_score(0, 1)
			if event.key == pygame.K_UP or event.key == pygame.K_w and game.game_over == False and game.game_paused == False:
				game.rotate()
			if event.key == pygame.K_RETURN and game.game_over == False:
				game.set_pause_or_resume_game()

		if event.type == GAME_UPDATE and game.game_over == False:
			if game.game_paused == False:
				game.move_down()

	#drawing
	highscore_value_surface = title_font.render(str(game.get_highscore()), True, Colors.white)
	score_value_surface = title_font.render(str(game.score), True, Colors.white)

	screen.fill(Colors.dark_blue)
	screen.blit(highscore_surface, (340, 20, 50, 50))
	screen.blit(score_surface, (365, 160, 50, 50))
	screen.blit(next_surface, (375, 300, 50, 50))

	if game.game_paused == True:
		screen.blit(game_paused_surface, (355, 552, 50, 50))

	if game.game_over == True:
		screen.blit(game_over_surface, (320, 552, 50, 50))
	
	pygame.draw.rect(screen, Colors.light_blue, highscore_rect, 0, 10)
	pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
	
	screen.blit(highscore_value_surface, highscore_value_surface.get_rect(centerx = highscore_rect.centerx, centery = highscore_rect.centery))
	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
	
	pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
	game.draw(screen)

	pygame.display.update()
	clock.tick(60) # <-- using 60 FPS