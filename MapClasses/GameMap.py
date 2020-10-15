"""
Represents a Tiled map with all map objects.
"""
from os import path

from CharacterClasses import SpriteSheet

FLIPPED_HORIZONTALLY_FLAG = 0x80000000
FLIPPED_VERTICALLY_FLAG = 0x40000000
FLIPPED_DIAGONALLY_FLAG = 0x20000000


class GameMap:
    """
    Represents a Tiled map with all map objects.
    """

    def __init__(self, map_data, width, height, sprite_map_file_path, sprite_map_cols,
                 sprite_map_rows, game_objs_env, game_objs_entry_exit, game_objs_hazard):
        self.map_data = map_data.replace('\n', '')
        """
        Represents a Tiled map with all map objects.
        """
        self.size = (width, height)
        self.sprite_map_size = (sprite_map_cols, sprite_map_rows)
        self.sprite_map_file_path = sprite_map_file_path
        self.game_objs = [game_objs_env, game_objs_entry_exit, game_objs_hazard]
        self.sprite_sheet = None
        self.background = None

    def load_sprite_sheet(self):
        """
        Loads the sprite sheet.
        """
        if self.sprite_sheet is not None:
            raise Exception('Sprite sheet already loaded')

        if not path.exists(self.sprite_map_file_path):
            raise Exception('Source file does not exist')

        self.sprite_sheet = SpriteSheet.SpriteSheet(self.sprite_map_file_path,
                                                    self.sprite_map_size[0],
                                                    self.sprite_map_size[1], False, True)

    def draw_background(self, surface):
        """
        Draws the map onto a surface.
        """
        if self.sprite_sheet is None:
            raise Exception('Sprite sheet not yet loaded')

        x_cord = 0
        y_cord = 0
        for tile in self.map_data.split(','):
            tile_val = int(tile)
            # TODO support flipping
            # flipped_horizontally = False
            # flipped_vertically = False
            # flipped_diagonally = False
            if tile_val > (self.sprite_map_size[0] * self.sprite_map_size[1]):
                if (FLIPPED_HORIZONTALLY_FLAG & tile_val) != 0:
                    # flipped_horizontally = True
                    tile_val = (~FLIPPED_HORIZONTALLY_FLAG) & tile_val
                if (FLIPPED_VERTICALLY_FLAG & tile_val) != 0:
                    # flipped_vertically = True
                    tile_val = (~FLIPPED_VERTICALLY_FLAG) & tile_val
                if (FLIPPED_DIAGONALLY_FLAG & tile_val) != 0:
                    # flipped_diagonally = True
                    tile_val = (~FLIPPED_DIAGONALLY_FLAG) & tile_val

            # subtract 1 to make the value 0 indexed
            tile_val = tile_val - 1

            self.sprite_sheet.draw(surface, tile_val, x_cord, y_cord)
            x_cord = (x_cord + 32) % (32 * self.size[0])
            if x_cord == 0:
                y_cord = y_cord + 32

    def draw_area(self, surface, rect):
        """
        Draws the section of the map contained within a given rectangle.
        """
        if self.sprite_sheet is None:
            raise Exception('Sprite sheet not yet loaded')

        x_cord = 0
        y_cord = 0

        for tile in self.map_data.split(','):
            if in_rect((x_cord + (self.sprite_sheet.cell_width / 2),
                        y_cord + (self.sprite_sheet.cell_height / 2)), rect):
                tile_val = int(tile)
                # TODO support flipping
                # flipped_horizontally = False
                # flipped_vertically = False
                # flipped_diagonally = False
                if tile_val > (self.sprite_map_size[0] * self.sprite_map_size[1]):
                    if (FLIPPED_HORIZONTALLY_FLAG & tile_val) != 0:
                        # flipped_horizontally = True
                        tile_val = (~FLIPPED_HORIZONTALLY_FLAG) & tile_val
                    if (FLIPPED_VERTICALLY_FLAG & tile_val) != 0:
                        # flipped_vertically = True
                        tile_val = (~FLIPPED_VERTICALLY_FLAG) & tile_val
                    if (FLIPPED_DIAGONALLY_FLAG & tile_val) != 0:
                        # flipped_diagonally = True
                        tile_val = (~FLIPPED_DIAGONALLY_FLAG) & tile_val

                # subtract 1 to make the value 0 indexed
                tile_val = tile_val - 1

                self.sprite_sheet.draw(surface, tile_val, x_cord, y_cord)
            x_cord = (x_cord + 32) % (32 * self.size[0])
            if x_cord == 0:
                y_cord = y_cord + 32

    def get_tile_size(self):
        """
        Returns the tile size of a map.
        """
        return self.sprite_sheet.cell_width, self.sprite_sheet.cell_height

    def print(self):
        """
        Prints the map and all objects to the console.
        """
        print('------------------------------------------------------')
        print('Map variables')
        print('------------------------------------------------------')

        print('map_data:')
        print(self.map_data)
        print('')

        print('size:')
        print(self.size)
        print('')

        print('sprite_map_file_path:')
        print(self.sprite_map_file_path)
        print('')

        print('sprite_map_size:')
        print(self.sprite_map_size)

        print('------------------------------------------------------')
        print('Map objects')
        print('------------------------------------------------------')
        for map_object in self.game_objs[0]:
            print(map_object.to_string())
            print('')

        for map_object in self.game_objs[1]:
            print(map_object.to_string())
            print('')

        for map_object in self.game_objs[2]:
            print(map_object.to_string())
            print('')


def in_rect(cord, rect):
    """
    Determines if a given set of coordinates are contained within a rectangle
    """
    if cord[0] < rect[0] or cord[0] > (rect[0] + rect[2]):
        return False
    if cord[1] < rect[1] or cord[1] > (rect[1] + rect[3]):
        return False
    return True
