import pygame
import random
import odds
import csgo_weapon_case as case1

pygame.init()

mainLoop = True

size = (512, 512)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("CSGO Case Unboxer")
loopCount = 0

# Chances


# # # # # CS:GO Weapon Case # # # # #


# # # # #

case_opened = False
csgo_weapons_case = False
show_skin_image = False

while mainLoop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            mainLoop = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                csgo_weapons_case = True
    screen.fill((255, 255, 255))
    rarity_float = 100 * random.random()

    if csgo_weapons_case == True:

        case_name = "csgo_weapons_case"

        if rarity_float <= odds.mil_spec:
            selected_skin = random.randint(0, len(case1.mil_spec) - 1)
            print(
                case1.mil_spec[selected_skin]["weapon"]
                + " | "
                + case1.mil_spec[selected_skin]["skin"]
            )
            skin_image = pygame.image.load(
                "./assets/"
                + case_name
                + "/"
                + str(case1.mil_spec[selected_skin]["id"])
                + ".png"
            )

        elif rarity_float <= odds.restricted and rarity_float >= odds.mil_spec:
            selected_skin = random.randint(0, len(case1.restricted) - 1)
            print(
                case1.restricted[selected_skin]["weapon"]
                + " | "
                + case1.restricted[selected_skin]["skin"]
            )
            skin_image = pygame.image.load(
                "./assets/"
                + case_name
                + "/"
                + str(case1.restricted[selected_skin]["id"])
                + ".png"
            )

        elif rarity_float <= odds.classified and rarity_float >= odds.restricted:
            selected_skin = random.randint(0, len(case1.classified) - 1)
            skin_image = pygame.image.load(
                "./assets/"
                + case_name
                + "/"
                + str(case1.classified[selected_skin]["id"])
                + ".png"
            )

        elif rarity_float <= odds.covert and rarity_float >= odds.classified:
            selected_skin = random.randint(0, len(case1.covert) - 1)
            print(
                case1.covert[selected_skin]["weapon"]
                + " | "
                + case1.covert[selected_skin]["skin"]
            )
            skin_image = pygame.image.load(
                "./assets/"
                + case_name
                + "/"
                + str(case1.covert[selected_skin]["id"])
                + ".png"
            )

        elif rarity_float <= odds.exceedingly_rare and rarity_float >= odds.covert:
            selected_skin = random.randint(0, len(case1.exceedingly_rare) - 1)
            print(
                case1.exceedingly_rare[selected_skin]["weapon"]
                + " | "
                + case1.exceedingly_rare[selected_skin]["skin"]
            )
            skin_image = pygame.image.load(
                "./assets/"
                + case_name
                + "/"
                + str(case1.exceedingly_rare[selected_skin]["id"])
                + ".png"
            )
        show_skin_image = True

        csgo_weapons_case = False
    if show_skin_image == True:
        screen.blit(skin_image, (0, 0))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
