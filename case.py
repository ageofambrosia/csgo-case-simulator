import pygame
import sys
import random
import modules.odds as odds
import modules.wear_values as wear
import modules.color as color
import modules.cases.csgo_weapon_case as case1
import modules.cases.esports_2013_case as case2

# Pygame Initialization #
image_assets_path = "assets/images/"
pygame.init()
pygame.font.init()
main_loop = True
size = (1024, 1024)
icon = pygame.image.load(image_assets_path + "icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("CSGO Case Unboxer")
screen.fill((255, 255, 255))
loopCount = 0
font = pygame.font.Font("assets/comfortaa.ttf", 50)

#########################

# CS:GO Case Initialization #

list_of_cases = ["placeholder", case1, case2]
case_opened = False
show_image_skin = False
show_image_case = False
show_image_stattrak = False
image_stattrak = pygame.image.load(image_assets_path + "stattrak.png")

filler_skin_0 = None
filler_skin_1 = None
filler_skin_2 = None
filler_skin_3 = None
filler_skin_4 = None
filler_skin_5 = None
filler_skin_6 = None
filler_skin_7 = None
filler_skin_8 = None
filler_skin_9 = None
filler_skin_10 = None
filler_skin_11 = None
filler_skin_12 = None
filler_skin_13 = None
filler_skin_14 = None
filler_skin_15 = None
filler_skin_16 = None
filler_skin_17 = None
filler_skin_18 = None
filler_skin_19 = None

list_of_filler_skins = [
    filler_skin_0,
    filler_skin_1,
    filler_skin_2,
    filler_skin_3,
    filler_skin_4,
    filler_skin_5,
    filler_skin_6,
    filler_skin_7,
    filler_skin_8,
    filler_skin_9,
    filler_skin_10,
    filler_skin_11,
    filler_skin_12,
    filler_skin_13,
    filler_skin_14,
]

list_of_filler_skins_x = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

list_of_filler_skins_colors = [
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
]

#############################

# Aspect Scale
# Author: Frank Raiser (crashchaos at gmx.net)
# Description: Scaling surfaces keeping their aspect ratio
# http://www.pygame.org/pcr/transform_scale/


def AspectScale(img, bx, by):
    """ Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    ix, iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx / float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by / float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by / float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx / float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by
    sx = round(sx)
    sy = round(sy)
    return pygame.transform.scale(img, (sx, sy))


def CaseOpen(CaseID):

    image_assets_path = "assets/images/"
    list_of_cases = ["placeholder", case1, case2]
    case_opened = False
    show_image_skin = False
    show_image_case = False
    show_image_stattrak = False
    image_stattrak = pygame.image.load(image_assets_path + "stattrak.png")
    case_id = CaseID
    image_case = pygame.image.load(
        image_assets_path + list_of_cases[case_id].case_name + "/" + "case.png"
    )

    # Deciding Rarity

    rarity_float = 100 * random.random()

    if rarity_float < odds.mil_spec:

        rarity = list_of_cases[case_id].mil_spec

        selected_skin = random.randint(0, len(rarity) - 1)
        skin_name_hf = (
            rarity[selected_skin]["weapon"] + " | " + rarity[selected_skin]["skin"]
        )
        image_skin = pygame.image.load(
            image_assets_path
            + list_of_cases[case_id].case_name
            + "/"
            + str(rarity[selected_skin]["id"])
            + ".png"
        )
        rarity_color = color.mil_spec

    elif rarity_float < odds.restricted and rarity_float >= odds.mil_spec:

        rarity = list_of_cases[case_id].restricted

        selected_skin = random.randint(0, len(rarity) - 1)
        skin_name_hf = (
            rarity[selected_skin]["weapon"] + " | " + rarity[selected_skin]["skin"]
        )
        image_skin = pygame.image.load(
            image_assets_path
            + list_of_cases[case_id].case_name
            + "/"
            + str(rarity[selected_skin]["id"])
            + ".png"
        )
        rarity_color = color.restricted

    elif rarity_float < odds.classified and rarity_float >= odds.restricted:

        rarity = list_of_cases[case_id].classified

        selected_skin = random.randint(0, len(rarity) - 1)
        skin_name_hf = (
            rarity[selected_skin]["weapon"] + " | " + rarity[selected_skin]["skin"]
        )
        image_skin = pygame.image.load(
            image_assets_path
            + list_of_cases[case_id].case_name
            + "/"
            + str(rarity[selected_skin]["id"])
            + ".png"
        )
        rarity_color = color.classified

    elif rarity_float < odds.covert and rarity_float >= odds.classified:

        rarity = list_of_cases[case_id].covert

        selected_skin = random.randint(0, len(rarity) - 1)
        skin_name_hf = (
            rarity[selected_skin]["weapon"] + " | " + rarity[selected_skin]["skin"]
        )
        image_skin = pygame.image.load(
            image_assets_path
            + list_of_cases[case_id].case_name
            + "/"
            + str(rarity[selected_skin]["id"])
            + ".png"
        )
        rarity_color = color.covert

    elif rarity_float < odds.exceedingly_rare and rarity_float >= odds.covert:

        rarity = list_of_cases[case_id].exceedingly_rare

        selected_skin = random.randint(0, len(rarity) - 1)
        selected_knife_skin_index = random.randint(
            0, (len(rarity[selected_skin]["skin"]) - 1),
        )
        selected_knife_skin_name = rarity[selected_skin]["skin"][
            selected_knife_skin_index
        ]

        if selected_knife_skin_index == 0:
            skin_name_hf = rarity[selected_skin]["weapon"]

        else:
            skin_name_hf = (
                rarity[selected_skin]["weapon"] + " | " + selected_knife_skin_name
            )
        image_skin = pygame.image.load(
            image_assets_path
            + list_of_cases[case_id].case_name
            + "/knives/"
            + str(rarity[selected_skin]["id"])
            + "/"
            + str(selected_knife_skin_index)
            + ".png"
        )
        rarity_color = color.exceedingly_rare

    # Deciding Wear

    ## Deciding Knife Wear, kinda complicated because it has to calculate for each skin

    if rarity == list_of_cases[case_id].exceedingly_rare:
        wear_float = random.uniform(
            (case1.knife_skin_wears[selected_knife_skin_index - 1][0]),
            (case1.knife_skin_wears[selected_knife_skin_index][1]),
        )
    else:
        wear_float = random.uniform(
            (rarity[selected_skin]["wear_range"][0]),
            (rarity[selected_skin]["wear_range"][1]),
        )

    if wear_float < wear.factory_new[1]:
        skin_wear = "fn"
        skin_wear_name_hf = "Factory New"
    elif wear_float < wear.minimal_wear[1] >= wear.factory_new[1]:
        skin_wear = "mw"
        skin_wear_name_hf = "Minimal Wear"
    elif wear_float < wear.field_tested[1] >= wear.minimal_wear[1]:
        skin_wear = "ft"
        skin_wear_name_hf = "Field-Tested"
    elif wear_float < wear.well_worn[1] >= wear.field_tested[1]:
        skin_wear = "ww"
        skin_wear_name_hf = "Well Worn"
    elif wear_float < wear.battle_scarred[1] >= wear.well_worn[1]:
        skin_wear = "bs"
        skin_wear_name_hf = "Battle Scarred"

    # Deciding StatTrak™

    stattrak_float = 100 * random.random()

    if stattrak_float < odds.stattrak:
        stattrak = True
    else:
        stattrak = False
    if stattrak == True:
        if rarity_float < odds.exceedingly_rare and rarity_float >= odds.covert:
            skin_name_hf = "★ StatTrak™ " + skin_name_hf
        else:
            skin_name_hf = "StatTrak™ " + skin_name_hf
    elif stattrak == False and (
        rarity_float < odds.exceedingly_rare and rarity_float >= odds.covert
    ):
        skin_name_hf = "★ " + skin_name_hf
    image_skin = AspectScale(image_skin, 512, 512)
    return (
        image_skin,
        stattrak,
        image_case,
        list_of_cases[case_id].case_name_hf,
        skin_name_hf,
        skin_wear_name_hf,
        rarity_color,
    )


pygame.init()

while main_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:

                for r in range(len(list_of_filler_skins)):
                    filler_choose = CaseOpen(1)
                    list_of_filler_skins[r] = filler_choose[0]
                    list_of_filler_skins_colors[r] = filler_choose[6]
                for r in range(len(list_of_filler_skins)):
                    list_of_filler_skins_x[r] = 0
                case_opened = True
                animation_finished = False
                case_open = CaseOpen(1)
                blit_skin = case_open[0]
                blit_stattrak = case_open[1]
                blit_case = case_open[2]
                print(
                    "["
                    + case_open[3]
                    + "] "
                    + case_open[4]
                    + " ("
                    + case_open[5]
                    + ")"  # Assembling full name of the skin
                )

                skin_x = 1024
                skin_y = 0

                for s in range(
                    len(list_of_filler_skins)
                ):  # Initial position of the filler skains, 500x its index in the list
                    list_of_filler_skins_x[s] = s * 500

            if event.key == pygame.K_w:
                for r in range(len(list_of_filler_skins)):
                    filler_choose = CaseOpen(2)
                    list_of_filler_skins[r] = filler_choose[0]
                    list_of_filler_skins_colors[r] = filler_choose[6]
                for r in range(len(list_of_filler_skins)):
                    list_of_filler_skins_x[r] = 0
                case_opened = True
                animation_finished = False
                case_open = CaseOpen(2)
                blit_skin = case_open[0]
                blit_stattrak = case_open[1]
                blit_case = case_open[2]
                print(
                    "[" + case_open[3] + "] " + case_open[4] + " (" + case_open[5] + ")"
                )
                skin_x = 1024
                skin_y = 20
                skin_name_x = 1024
                skin_name_y = 100
                for s in range(len(list_of_filler_skins)):
                    list_of_filler_skins_x[s] = s * 500

    screen.fill((255, 255, 255))

    if case_opened == True:
        screen.blit(blit_case, (400, 600))
        screen.blit(blit_skin, (skin_x, skin_y))
        skin_name = case_open[4]
        skin_wear = "(" + case_open[5] + ")"
        skin_name_screentext = font.render(skin_name, False, (case_open[6]))
        skin_wear_screentext = font.render(skin_wear, False, (case_open[6]))
        screen.blit(skin_name_screentext, (skin_x + 100, skin_y + 400))
        screen.blit(skin_wear_screentext, (skin_x + 100, skin_y + 500))
        if blit_stattrak == True:
            screen.blit(image_stattrak, (skin_x + 400, skin_y))

        for s in range(len(list_of_filler_skins)):
            pygame.draw.rect(
                screen, (225, 225, 225), [(list_of_filler_skins_x[s]), 20, 512, 512], 0
            )
            pygame.draw.rect(
                screen,
                list_of_filler_skins_colors[s],
                [(list_of_filler_skins_x[s]), 450, 512, 100],
                0,
            )
            screen.blit(list_of_filler_skins[s], (list_of_filler_skins_x[s], 50))
            list_of_filler_skins_x[s] -= 50 - s * 2
            if list_of_filler_skins_x[-1] <= -500:
                animation_finished = True
                for i in range(len(list_of_filler_skins)):
                    list_of_filler_skins_x[s] = -1000
        if skin_x >= 256 and animation_finished == True:
            skin_x -= 20

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()