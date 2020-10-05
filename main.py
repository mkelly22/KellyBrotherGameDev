import pygame
from SpriteCharacter import *
from GameMap import *

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

CHARACTER_SPRITE_FILE = "./images/sprite_sheet1.png"
CHARACTER_COLS = 4
CHARACTER_ROWS = 2
SPRITE_COLS = 3
SPRITE_ROWS = 4
MOVE_SPEED = 2
SPRITE_UPDATE_RATE = 15  # 1 update / X FPS


def main():


    ret = pygame.init()
    if ret[1] > 0:
        pygame.quit()
        raise Exception("Failed to initialize a module")

    play_game = True
    screen_width, screen_height = 1240, 720
    x, y = screen_width / 2, screen_height / 2
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(size=[screen_width, screen_height])
    pygame.display.set_caption("Sprite Tests")
    sprite_character = SpriteCharacter(CHARACTER_SPRITE_FILE, SPRITE_COLS, SPRITE_ROWS, CHARACTER_COLS, CHARACTER_ROWS)
    fps = 60
    direction = SpriteCharacter.CHARACTER_DOWN
    count = 0

    # load first map
    game_map = GameMapFactory.create('./tiled_proj/maps/desert_map.tmx')

    # play game
    while play_game:
        moving = False

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                play_game = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            play_game = False
        elif play_game:
            if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                y = y - MOVE_SPEED
                moving = True
                direction = SpriteCharacter.CHARACTER_UP
                if y < (0 - sprite_character.sprite_sheet.handles[sprite_character.sprite_sheet.CENTER_HANDLE][1]):
                    y = screen_height + sprite_character.sprite_sheet.handles[sprite_character.sprite_sheet.CENTER_HANDLE][1]
            if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
                y = y + MOVE_SPEED
                moving = True
                direction = SpriteCharacter.CHARACTER_DOWN
            if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                x = x - MOVE_SPEED
                moving = True
                direction = SpriteCharacter.CHARACTER_LEFT
            if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                x = x + MOVE_SPEED
                moving = True
                direction = SpriteCharacter.CHARACTER_RIGHT

        if play_game:
            if moving:
                count = count + 1
                if count >= SPRITE_UPDATE_RATE:
                    sprite_character.next_sprite()
                    count = 0
            # TODO - Display actual map
            display.fill(BLACK)
            sprite_character.set_direction(direction)
            sprite_character.draw_character(display, x, y)
            pygame.display.update()
            clock.tick(fps)
            pygame.event.pump()

    pygame.quit()


if __name__ == '__main__':
    main()


