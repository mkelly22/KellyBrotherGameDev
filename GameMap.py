import xml.etree.ElementTree as ET
from SpiritSheet import *

class GameMap:
    def __init__(self, map_data, width, height, tile_width, tile_height, source_file):
        self.map_data = map_data
        self.width = width
        self.height = height
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.source_file = source_file
        self.sprite_sheet = None

    def load_map(self):
        self.sprite_sheet = SpriteSheet(self.source_file, self.height)



class GameMapFactory:

    @staticmethod
    def Create(map_tmx_file):
        tree = ET.parse(map_tmx_file)
        root = tree.getroot()
        objectgroup = root.find('objectgroup')
        for object in objectgroup:
            properties = object.find('properties')
            for property in properties: