import pygame
pygame.init()

image_assets_path = "assets/images/"
pygame.init()
main_loop = True
size = (1024, 1024)
icon = pygame.image.load(image_assets_path + "icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("CSGO Case Unboxer")
screen.fill((255, 255, 255))
loopCount = 0

while True:
    