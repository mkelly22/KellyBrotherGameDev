from CharacterClasses.PlayerCharacter import *
from MapClasses.GameMapFactory import *

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

CHARACTER_SPRITE_DICT = {
    'file_name': './images/sprite_sheet1.png',
    'sprite_cols': 3,
    'sprite_rows': 4,
    'character_cols': 4,
    'character_rows': 2,
}


def main():
    ret = pygame.init()
    if ret[1] > 0:
        pygame.quit()
        raise Exception("Failed to initialize a module")

    play_game = True
    screen_width, screen_height = 1920, 1080
    x, y = screen_width / 2, screen_height / 2
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(size=[screen_width, screen_height])
    pygame.display.set_caption("Sprite Tests")
    player_character = PlayerCharacter([x, y], (screen_width, screen_height), CHARACTER_SPRITE_DICT)
    fps = 60

    # load first map
    game_map = GameMapFactory.create('./tiled_proj/maps/desert_map.tmx')
    game_map.load_sprite_sheet()

    new_map = True

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
        if play_game:
            move_left = False
            move_right = False
            move_up = False
            move_down = False
            if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                move_up = True
            if keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
                move_down = True
            if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                move_left = True
            if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
                move_right = True

            player_character.move(move_left, move_right, move_up, move_down)

            if new_map:
                display.fill(BLACK)
                game_map.draw_background(display)
                new_map = False

            if player_character.is_moving():
                game_map.draw_area(display, player_character.get_movement_area(game_map.get_tile_size()))
            player_character.draw_character(display)
            pygame.display.update()
            print(clock.get_fps())
            clock.tick(fps)
            pygame.event.pump()

    pygame.quit()


if __name__ == '__main__':
    main()


