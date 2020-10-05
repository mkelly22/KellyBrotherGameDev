from os import path
import xml.etree.ElementTree as ET

from MapClasses.GameMap import *
from MapClasses.MapObject import *

VERSION = '1.4'
TILED_VERSION = '1.4.2'


class GameMapFactory:

    @staticmethod
    def create(map_tmx_file):
        # check if map tmx file exits
        if not path.exists(map_tmx_file):
            raise Exception('map tmx file does not exist')

        tree = ET.parse(map_tmx_file)
        root = tree.getroot()

        try:
            if root is None:
                raise Exception("map tsx file is not compatible, no root found")

            # check versions
            if root.attrib['version'] != VERSION or root.attrib['tiledversion'] != TILED_VERSION:
                raise Exception('Version of map is not compatible, current supported version is: ' + VERSION +
                                ', current supported tile version is: ' + TILED_VERSION)

            width = int(root.attrib['width'])
            height = int(root.attrib['height'])

            # get map data
            layer = root.find('layer')
            data_element = layer.find('data')
            map_data = data_element.text

            # parse objects
            objectgroup = root.find('objectgroup')
            game_objs_env = []
            game_objs_entry_exit = []
            game_objs_hazard = []
            for map_object in objectgroup:
                object_properties = map_object.find('properties')
                blocked = None
                movement = EnMovementProperty.NONE
                start_zone = None
                map_exit = None
                for object_property in object_properties:
                    property_name = object_property.attrib['name']
                    if property_name == 'exit':
                        map_exit = object_property.attrib['value']
                    if property_name == 'blocked':
                        blocked = True
                    if property_name == 'start_zone':
                        start_zone = True
                    if property_name == 'movement':
                        if object_property.attrib['value'] == 'slowed':
                            movement = EnMovementProperty.SLOWED
                        else:
                            raise Exception('object property is not compatible: ' + object_property.attrib['value'])

                if blocked is not None:
                    game_objs_env.append(MapObject(blocked, movement, start_zone, map_exit))
                elif movement is not EnMovementProperty.NONE:
                    game_objs_hazard.append(MapObject(blocked, movement, start_zone, map_exit))
                else:
                    game_objs_entry_exit.append(MapObject(blocked, movement, start_zone, map_exit))

            # find tileset to get source tsx file
            tileset = root.find('tileset')
            source_tsx_file = './tiled_proj/maps/' + tileset.attrib['source']
        except TypeError:
            raise Exception('Input tmx file is not valid')

        # parse tsx file
        if not path.exists(source_tsx_file):
            raise Exception('Source tsx file does not exist')

        try:
            tree = ET.parse(source_tsx_file)
            root = tree.getroot()

            image = root.find('image')
            sprite_map_file_path = './tiled_proj/maps/' + image.attrib['source']
            sprite_map_cols = int(root.attrib['columns'])
            sprite_map_rows = int(int(root.attrib['tilecount']) / sprite_map_cols)

        except TypeError:
            raise Exception('Referenced tsx file is not valid')

        return GameMap(map_data, width, height, sprite_map_file_path, sprite_map_cols, sprite_map_rows, game_objs_env,
                       game_objs_entry_exit, game_objs_hazard)
