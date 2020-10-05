from os import path

from SpriteSheet import *

FLIPPED_HORIZONTALLY_FLAG = 0x80000000
FLIPPED_VERTICALLY_FLAG = 0x40000000
FLIPPED_DIAGONALLY_FLAG = 0x20000000


class GameMap:
    def __init__(self, map_data, width, height, sprite_map_file_path, sprite_map_cols, sprite_map_rows, game_objs_env,
                 game_objs_entry_exit, game_objs_hazard):
        self.map_data = map_data.replace('\n', '')
        self.width = width
        self.height = height
        self.sprite_map_cols = sprite_map_cols
        self.sprite_map_rows = sprite_map_rows
        self.sprite_map_file_path = sprite_map_file_path
        self.game_objs_env = game_objs_env
        self.game_objs_entry_exit = game_objs_entry_exit
        self.game_objs_hazard = game_objs_hazard
        self.sprite_sheet = None
        self.background = None

    def load_sprite_sheet(self):
        if self.sprite_sheet is not None:
            raise Exception('Sprite sheet already loaded')

        if not path.exists(self.sprite_map_file_path):
            raise Exception('Source file does not exist')

        self.sprite_sheet = SpriteSheet(self.sprite_map_file_path, self.sprite_map_cols, self.sprite_map_rows, False,
                                        True)

    def draw_background(self, surface):
        if self.sprite_sheet is None:
            raise Exception('Sprite sheet not yet loaded')

        x = 0
        y = 0
        for tile in self.map_data.split(','):
            tile_val = int(tile)
            flipped_horizontally = False
            flipped_vertically = False
            flipped_diagonally = False
            if tile_val > (self.sprite_map_cols * self.sprite_map_rows):
                if (FLIPPED_HORIZONTALLY_FLAG & tile_val) != 0:
                    flipped_horizontally = True
                    tile_val = (~FLIPPED_HORIZONTALLY_FLAG) & tile_val
                if (FLIPPED_VERTICALLY_FLAG & tile_val) != 0:
                    flipped_vertically = True
                    tile_val = (~FLIPPED_VERTICALLY_FLAG) & tile_val
                if (FLIPPED_DIAGONALLY_FLAG & tile_val) != 0:
                    flipped_diagonally = True
                    tile_val = (~FLIPPED_DIAGONALLY_FLAG) & tile_val

            # subtract 1 to make the value 0 indexed
            tile_val = tile_val - 1

            self.sprite_sheet.draw(surface, tile_val, x, y)
            x = (x + 32) % (32 * self.width)
            if x == 0:
                y = y + 32

    def print(self):
        print('------------------------------------------------------')
        print('Map variables')
        print('------------------------------------------------------')

        print('map_data:')
        print(self.map_data)
        print('')

        print('width:')
        print(self.width)
        print('')

        print('height:')
        print(self.height)
        print('')

        print('sprite_map_file_path:')
        print(self.sprite_map_file_path)
        print('')

        print('sprite_map_cols:')
        print(self.sprite_map_cols)
        print('')

        print('sprite_map_rows:')
        print(self.sprite_map_rows)
        print('')

        print('------------------------------------------------------')
        print('Map objects')
        print('------------------------------------------------------')
        for map_object in self.game_objs_env:
            print(map_object.to_string())
            print('')

        for map_object in self.game_objs_entry_exit:
            print(map_object.to_string())
            print('')

        for map_object in self.game_objs_hazard:
            print(map_object.to_string())
            print('')

