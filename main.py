import pygame, sys

screen = pygame.display.set_mode((500, 500))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit("User closed the window...")
      sys.exit()
      
    pygame.display.update()
