import pygame
import sys

pygame.init()
dar_blue = (44, 44, 127)

icon = pygame.image.load('assets/icon.png')
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Py-Tetris")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	#drawing
	screen.fill(dar_blue)
	pygame.display.update()
	clock.tick(60) # <-- using 60 FPS