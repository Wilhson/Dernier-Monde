# Import library
import pygame
import json
import random
from pygame.locals import *

# Needed Init
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

# [Image Import and Convert]
load_window = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Load")
load_icon = pygame.image.load("Assets\Images\Icon\Load.png").convert_alpha()
load_icon = pygame.transform.scale(load_icon, (32, 32))
pygame.display.set_icon(load_icon)


def button(surface, x, y, w, h, bf, bt):

    # Button Init
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        surface.blit(bt, (x, y))
        if click[0] == 1:
            return True
    else:
        surface.blit(bf, (x, y))


def update():
    pygame.display.update()


def wait():
    pygame.time.delay(30)


def options_txt():

    options = {}

    options["options"] = {
        "width": "1600",
        "height": "900",
        "volume": "0.2",
        "character": "0"
    }
    data = json.dumps(options)

    with open("Assets\Data\Config.txt", "w") as options:
        options.write(data)


def player_txt():

    player = {}

    player["player"] = {
        "position": "0"
    }
    player["inventory"] = {
        "slot number": "4",
        "slot 1": "0",
        "slot 2": "0",
        "slot 3": "0",
        "slot 4": "0",
        "slot 5": "0",
        "slot 6": "0",
        "slot 7": "0",
        "slot 8": "0",
        "slot 9": "0",
        "slot 10": "0"
    }
    data = json.dumps(player)

    with open("Assets\Data\Player.txt", "w") as player:
        player.write(data)


def character_txt():

    character = {}

    character["johnson"] = {
        "slots": "6",
        "endurance": "6",
        "strength": "2",
        "vision": "2"
    }
    data = json.dumps(character)

    with open("Assets\Data\Character.txt", "w") as character:
        character.write(data)


def map_txt():
    code_map = []
    crash_site = random.randrange(0, 512)
    for i in range(0, 512):
        code_map.append([i])
        tree = random.randrange(0, 4)
        code_map[i].append(tree)
        tree_c = random.randrange(0, 4)
        code_map[i].append(tree_c)
        code_map[i].append(False)
        if crash_site == i:
            code_map[i][3] = True
            code_map[i][1] = 0

    with open('Assets\Data\Map.txt', 'r+') as map_file:
        json.dump(code_map, map_file)

    with open("Assets\Data\player.txt", "r") as player:
        data = player.read()
        player = json.loads(data)

    (player["player"]["position"]) = crash_site

    data = json.dumps(player)

    with open("Assets\Data\player.txt", "w") as player:
        player.write(data)


def function_menu():

    # [Info Profile]

    with open("Assets\Data\Options.txt", "r") as options:
        data = options.read()
        options = json.loads(data)
        w = int(options["options"]["width"])
        h = int(options["options"]["height"])
        vol = float(options["options"]["volume"])

    # [Variable Convert]

    # Button Play
    xp = int(50 / 1600 * w)
    yp = int(40 / 900 * h)
    wp = int(92 / 1600 * w)
    hp = int(40 / 900 * h)

    # Button Options
    xo = int(50 / 1600 * w)
    yo = int(90 / 900 * h)
    wo = int(156 / 1600 * w)
    ho = int(40 / 900 * h)

    # Button Quit
    xq = int(50 / 1600 * w)
    yq = int(140 / 900 * h)
    wq = int(84 / 1600 * w)
    hq = int(40 / 900 * h)

    # [Button Menu]
    button_menu = pygame.image.load("Assets\Images\Button\Button Menu.png").convert_alpha()

    # Button Play
    pf = pygame.transform.scale(button_menu.subsurface(0, 0, 23, 9), (wp, hp))
    pt = pygame.transform.scale(button_menu.subsurface(23, 0, 23, 9), (wp, hp))

    # Button Options
    of = pygame.transform.scale(button_menu.subsurface(46, 0, 39, 9), (wo, ho))
    ot = pygame.transform.scale(button_menu.subsurface(85, 0, 39, 9), (wo, ho))

    # Button Quit
    qf = pygame.transform.scale(button_menu.subsurface(124, 0, 21, 9), (wq, hq))
    qt = pygame.transform.scale(button_menu.subsurface(145, 0, 21, 9), (wq, hq))

    # Background Import and Convert
    bg_menu = pygame.image.load("Assets\Images\Background\Menu.png").convert_alpha()
    bg_menu = pygame.transform.scale(bg_menu, (w, h))

    # Music Import
    pygame.mixer.music.load("Assets\Sounding\Music\Music_menu.mp3")

    # Sound Import
    s_b = pygame.mixer.Sound("Assets\Sounding\Sound\Button.wav")

    # Display Menu
    menu_surface = pygame.display.set_mode((w, h), FULLSCREEN)
    pygame.display.set_caption("Neocamp")

    # Icon
    loadicon = pygame.image.load("Assets\Images\Icon\Load.png").convert_alpha()
    loadicon = pygame.transform.scale(loadicon, (32, 32))
    pygame.display.set_icon(loadicon)

    # Song
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(vol)

    # Tick Init
    clock = pygame.time.Clock()

    # Run loop and Function Button
    play_updater = False
    options_updater = False
    quit_updater = False
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        # Exit Control
        if keys[pygame.K_ESCAPE]:
            run = False
        if keys[pygame.QUIT]:
            run = False

        # Background Display
        menu_surface.blit(bg_menu, (0, 0))

        # [Play Button]

        play_updater = button(menu_surface, xp, yp, wp, hp, pf, pt)

        if play_updater:
            pygame.mixer.Sound.play(s_b)
            wait()
            pygame.mixer.music.stop()
            function_map()

        # [Options Button]

        options_updater = button(menu_surface, xo, yo, wo, ho, of, ot)

        if options_updater:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(s_b)
            function_options()

        # [Quit Button]

        quit_updater = button(menu_surface, xq, yq, wq, hq, qf, qt)

        if quit_updater:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(s_b)
            run = False

        update()

    pygame.quit()


def function_map():

    # [Info Options]

    with open("Assets\Data\Options.txt", "r") as options:
        data = options.read()
        options = json.loads(data)
        w = int(options["options"]["width"])
        h = int(options["options"]["height"])
        character = int(options["options"]["character"])

    with open("Assets\Data\Player.txt", "r") as player:
        data = player.read()
        player = json.loads(data)
        pos = int(player["player"]["position"])
        slot_number = int(player["inventory"]["slot number"])
        slot1 = int(player["inventory"]["slot 1"])
        slot2 = int(player["inventory"]["slot 2"])
        slot3 = int(player["inventory"]["slot 3"])
        slot4 = int(player["inventory"]["slot 4"])
        slot5 = int(player["inventory"]["slot 5"])
        slot6 = int(player["inventory"]["slot 6"])
        slot7 = int(player["inventory"]["slot 7"])
        slot8 = int(player["inventory"]["slot 8"])
        slot9 = int(player["inventory"]["slot 9"])
        slot10 = int(player["inventory"]["slot 10"])
    slot = [slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, slot10]

    with open("Assets\Data\Character.txt", "r") as character_info:
        data = character_info.read()
        character_info = json.loads(data)
        en_johnson = int(character_info["johnson"]["endurance"])
    en = en_johnson

    # [Variable Convert]

    # Cell Convert
    wce = int(50 / 1600 * w)
    hce = int(50 / 900 * h)

    # Tree Convert
    wt = int(14 / 1600 * w)
    ht = int(14 / 900 * h)

    # Player
    wc = int(24 / 1600 * w)
    hc = int(39 / 900 * h)

    # Crash Site Convert
    wcrs = int(46 / 1600 * w)
    hcrs = int(46 / 900 * h)

    # [Inventory]

    wi = int(509 / 1600 * w)
    hi = int(50 / 900 * h)
    xi = int(60 / 1600 * w)
    yi = int(10 / 900 * h)

    # Cell Inventory
    wcei = int(50 / 1600 * w)
    hcei = int(50 / 1600 * w)

    # Utility
    wu4 = int(4 / 1600 * w)
    hu4 = int(4 / 900 * h)
    wu2 = int(2 / 1600 * w)
    hu2 = int(2 / 900 * h)
    wu13 = int(13 / 1600 * w)
    hu6 = int(6 / 900 * h)

    # [Button Map]

    wbm = int(40 / 1600 * w)
    hbm = int(40 / 900 * h)

    # Button Exit Convert
    xe = int(1550 / 1600 * w)
    ye = int(10 / 900 * h)
    xei = int()
    yei = int()

    # Button Inventory Convert
    xinv = int(10 / 1600 * w)
    yinv = int(10 / 900 * h)

    # [Map Element Import]

    # Background Import
    bg_map = pygame.image.load("Assets\Images\Background\Map.png").convert_alpha()
    bg_map = pygame.transform.scale(bg_map, (w, h))

    # [Inventory]
    cell_inventory = pygame.image.load("Assets\Images\Inventory\Cell Inventory.png").convert_alpha()
    cell_inventory = pygame.transform.scale(cell_inventory, (wcei, hcei))

    # Cell Font Import
    cell = pygame.image.load("Assets\Images\Map\Cell.png").convert_alpha()
    cell = pygame.transform.scale(cell, (wce, hce))

    # Tree Import
    tree = pygame.image.load("Assets\Images\Map\Tree.png").convert_alpha()

    tree_0 = pygame.transform.scale(tree.subsurface(0, 0, 14, 14), (wt, ht))
    tree_1 = pygame.transform.scale(tree.subsurface(14, 0, 14, 14), (wt, ht))
    tree_2 = pygame.transform.scale(tree.subsurface(28, 0, 14, 14), (wt, ht))
    tree_3 = pygame.transform.scale(tree.subsurface(42, 0, 14, 14), (wt, ht))
    tree = [tree_0, tree_1, tree_2, tree_3]

    # Crash Site
    crash_site = pygame.image.load("Assets\Images\map\Crashsite.png").convert_alpha()
    crash_site = pygame.transform.scale(crash_site, (wcrs, hcrs))

    # [Button Map]
    button_map = pygame.image.load("Assets\Images\Button\Button Map.png").convert_alpha()

    # Button Exit
    ef = pygame.transform.scale(button_map.subsurface(0, 0, 9, 9), (wbm, hbm))
    et = pygame.transform.scale(button_map.subsurface(9, 0, 9, 9), (wbm, hbm))

    # Button Inventory
    invf = pygame.transform.scale(button_map.subsurface(18, 0, 9, 9), (wbm, hbm))
    invt = pygame.transform.scale(button_map.subsurface(27, 0, 9, 9), (wbm, hbm))

    # [Character Import]

    if character == 0:

        # Character "Johnson"
        johnson_sprite = pygame.image.load("Assets\Images\Character\Johnson\Johnson Map.png").convert_alpha()

        johnson_0 = pygame.transform.scale(johnson_sprite.subsurface(0, 0, 24, 39), (wc, hc))
        johnson_1 = pygame.transform.scale(johnson_sprite.subsurface(24, 0, 24, 39), (wc, hc))

        johnson_sprite = [johnson_0, johnson_1]

    # Data Map
    with open("Assets\Data\Map.txt") as map_file:
        code_map = json.load(map_file)

    # Sound Import
    s_b = pygame.mixer.Sound("Assets\Sounding\Sound\Button.wav")

    # Display Map
    map_surface = pygame.display.set_mode((w, h), FULLSCREEN)
    pygame.display.set_caption("Neocamp")

    clock = pygame.time.Clock()

    # Run loop
    frame1 = 0
    frame2 = 0
    run_map = True
    song_inv = True
    wait_inv = True
    inventory_up = False
    inventory_updater = True
    while run_map:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_map = False

        # Movement Control
        keys = pygame.key.get_pressed()

        # Exit Control
        if keys[pygame.K_ESCAPE]:
            function_menu()

        if pos > 31:
            if keys[pygame.K_UP]:
                pos = pos - 32
                en = en - 1
        if pos < 480:
            if keys[pygame.K_DOWN]:
                pos = pos + 32
                en = en - 1
        if (pos + 1) % 32 != 0:
            if keys[pygame.K_RIGHT]:
                pos = pos + 1
                en = en - 1
        if pos % 32 != 0:
            if keys[pygame.K_LEFT]:
                pos = pos - 1
                en = en - 1

        # Display Background
        map_surface.blit(bg_map, (0, 0))

        # [Exit Button]

        exit_updater = button(map_surface, xe, ye, wbm, hbm, ef, et)

        if exit_updater:
            pygame.mixer.Sound.play(s_b)
            function_menu()

        # Display Cell
        line = 2 * hce
        u = 0
        frame1 = frame1 + 1
        for i in range(0, 512):
            if u == 32:
                line = line + hce
                u = 0
            v = u * wce
            map_surface.blit(cell, (v, line))
            tr = code_map[i][1]
            if tr != 0:
                for p in range(0, tr):
                    if code_map[i][2] == 0:
                        map_surface.blit(tree[0], (v + (p * ht) + wu4, line + hu4))
                    if code_map[i][2] == 1:
                        map_surface.blit(tree[1], (v + (p * ht) + wu4, line + hu4))
                    if code_map[i][2] == 2:
                        map_surface.blit(tree[2], (v + (p * ht) + wu4, line + hu4))
                    if code_map[i][2] == 3:
                        map_surface.blit(tree[3], (v + (p * ht) + wu4, line + hu4))

            # Crash Site
            if code_map[i][3]:
                map_surface.blit(crash_site, (v + wu2, line + hu2))

            # Character Display Sprite
            if pos == i:
                # Johnson
                if character == 0:
                    if frame1 <= 16:
                        map_surface.blit(johnson_sprite[1], (v + wu13, line + hu6))
                    else:
                        map_surface.blit(johnson_sprite[0], (v + wu13, line + hu6))
                        frame2 = frame2 + 1
                    if frame2 > 16:
                        frame1 = 0
                        frame2 = 0
            u = u + 1

        # [Inventory Button]

        if inventory_up:
            pass

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if inventory_updater:
            if xinv + wbm > mouse[0] > xinv and yinv + hbm > mouse[1] > yinv:
                map_surface.blit(invt, (xinv, yinv))
                if click[0] == 1:
                    pygame.time.delay(200)
                    inventory_updater = False
                    pygame.mixer.Sound.play(s_b)
            else:
                map_surface.blit(invf, (xinv, yinv))

        if not inventory_updater:
            if xinv + wbm > mouse[0] > xinv and yinv + hbm > mouse[1] > yinv:
                map_surface.blit(invf, (xinv, yinv))
                if click[0] == 1:
                    pygame.time.delay(200)
                    inventory_updater = True
                    pygame.mixer.Sound.play(s_b)
            else:
                map_surface.blit(bef, (xinv, yinv))

        update()
    pygame.quit()


def function_character_select():

    # [Info Options]

    with open("Assets\Data\Options.txt", "r") as options:
        data = options.read()
        options = json.loads(data)
        w = int(options["options"]["width"])
        h = int(options["options"]["height"])
        character = int(options["options"]["character"])
    character_selected = character

    # [Variable Convert]

    # Button Left
    xl = int(40 / 1600 * w)
    yl = int(320 / 900 * h)
    wl = int(44 / 1600 * w)
    hl = int(40 / 900 * h)

    # Button Right
    xr = int(224 / 1600 * w)
    yr = int(320 / 900 * h)
    wr = int(44 / 1600 * w)
    hr = int(40 / 900 * h)

    # Button Select
    xs = int(94 / 1600 * w)
    ys = int(320 / 900 * h)
    ws = int(120 / 1600 * w)
    hs = int(40 / 900 * h)

    # Character
    xcs = int(75 / 1600 * w)
    ycs = int(50 / 900 * h)
    wcs = int(160 / 1600 * w)
    hcs = int(260 / 900 * h)

    # Display Profile
    character_surface = pygame.display.set_mode((w, h), FULLSCREEN)
    pygame.display.set_caption("Neocamp")

    # Background Import
    bg_character_select = pygame.image.load("Assets\Images\Background\Character Select.png").convert_alpha()
    bg_character_select = pygame.transform.scale(bg_character_select, (w, h))

    # [Button Character Select]
    button_character_select = pygame.image.load("Assets\Images\Button\Button Character Select.png").convert_alpha()

    # Button Left
    lf = pygame.transform.scale(button_character_select.subsurface(0, 0, 11, 9), (wl, hl))
    lt = pygame.transform.scale(button_character_select.subsurface(11, 0, 11, 9), (wl, hl))

    # Button Select
    sf = pygame.transform.scale(button_character_select.subsurface(22, 0, 30, 9), (ws, hs))
    st = pygame.transform.scale(button_character_select.subsurface(52, 0, 30, 9), (ws, hs))

    # Button Right
    rf = pygame.transform.scale(button_character_select.subsurface(82, 0, 11, 9), (wr, hr))
    rt = pygame.transform.scale(button_character_select.subsurface(93, 0, 11, 9), (wr, hr))

    # [Character Import]

    # Character "Johnson"
    johnson_sprite = pygame.image.load("Assets\Images\Character\Johnson\Johnson Map.png").convert_alpha()
    johnson_0 = pygame.transform.scale(johnson_sprite.subsurface(0, 0, 24, 39), (wcs, hcs))
    johnson_1 = pygame.transform.scale(johnson_sprite.subsurface(24, 0, 24, 39), (wcs, hcs))
    johnson_sprite = [johnson_0, johnson_1]

    character_code = [0, 1]

    # Sound Import
    s_b = pygame.mixer.Sound("Assets\Sounding\Sound\Button.wav")

    clock = pygame.time.Clock()

    # Run Loop and Button Variable
    frame1 = 0
    frame2 = 0
    left_variable = False
    right_variable = False
    select_variable = False
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        # Exit Control
        if keys[pygame.K_ESCAPE]:
            function_options()
            run = False
        if keys[pygame.QUIT]:
            run = False

        # Background Display
        character_surface.blit(bg_character_select, (0, 0))

        # [Left Button]
        if character != character_code[0]:
            left_variable = button(character_surface, xl, yl, wl, hl, lf, lt)
        if left_variable:
            left_variable = False
            pygame.mixer.Sound.play(s_b)
            wait()
            character = character - 1

        # [Right Button]
        if character != character_code[-1]:
            right_variable = button(character_surface, xr, yr, wr, hr, rf, rt)
        if right_variable:
            right_variable = False
            pygame.mixer.Sound.play(s_b)
            wait()
            character = character + 1

        # [Select Button]
        if character_selected != character:
            select_variable = button(character_surface, xs, ys, ws, hs, sf, st)
        if select_variable:
            select_variable = False
            pygame.mixer.Sound.play(s_b)
            wait()

            with open("Assets\Data\Options.txt", "r") as options:
                data = options.read()
                options = json.loads(data)

            (options["options"]["character"]) = str(character)
            data = json.dumps(options)

            with open("Assets\Data\Options.txt", "w") as options:
                options.write(data)
            character_selected = character

        # Sprite Init
        frame1 = frame1 + 1

        # Johnson
        if character == 0:
            if frame1 <= 16:
                character_surface.blit(johnson_sprite[1], (xcs, ycs))
            else:
                character_surface.blit(johnson_sprite[0], (xcs, ycs))
                frame2 = frame2 + 1
            if frame2 > 16:
                frame1 = 0
                frame2 = 0

        update()

    pygame.quit()


def function_options():

    # [Info Options]

    with open("Assets\Data\Options.txt", "r") as options:
        data = options.read()
        options = json.loads(data)
        w = int(options["options"]["width"])
        h = int(options["options"]["height"])

    # [Variable Convert]

    # Button Character Select
    xchs = int(50 / 1600 * w)
    ychs = int(40 / 900 * h)
    wchs = int(332 / 1600 * w)
    hchs = int(40 / 900 * h)

    # Display Options
    options_surface = pygame.display.set_mode((w, h), FULLSCREEN)
    pygame.display.set_caption("Neocamp Options")

    # Background Import
    bg_options = pygame.image.load("Assets\Images\Background\Options.png").convert_alpha()
    bg_options = pygame.transform.scale(bg_options, (w, h))

    # [Button Options]
    button_menu = pygame.image.load("Assets\Images\Button\Button Options.png").convert_alpha()

    # Button Character Select
    chsf = pygame.transform.scale(button_menu.subsurface(0, 0, 83, 9), (wchs, hchs))
    chst = pygame.transform.scale(button_menu.subsurface(83, 0, 83, 9), (wchs, hchs))

    # Sound Import
    s_b = pygame.mixer.Sound("Assets\Sounding\Sound\Button.wav")

    clock = pygame.time.Clock()

    # Run loop
    character_select_updater = False
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        # Exit Control
        if keys[pygame.K_ESCAPE]:
            function_menu()
            run = False
        if keys[pygame.QUIT]:
            run = False

        # Background Display
        options_surface.blit(bg_options, (0, 0))

        character_select_updater = button(options_surface, xchs, ychs, wchs, hchs, chsf, chst)

        # [Character Select Button]
        if character_select_updater:
            pygame.mixer.Sound.play(s_b)
            function_character_select()

        update()

    pygame.quit()


player_txt()
character_txt()
map_txt()
function_menu()