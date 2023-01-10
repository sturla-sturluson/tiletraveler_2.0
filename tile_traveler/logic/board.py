from ..models.tile import Tile
from ..models.borders import Borders


class Board:
    def __init__(self, map_width: int, map_height: int = None) -> None:
        self.map_width = map_width
        # If map height isnt specified Board will assume the user wants a square and uses width as the height
        if map_height == None:
            self.map_height = map_width
        else:
            self.map_height = map_height

        self.tile_dict: dict[tuple[int], Tile] = dict()
        self.create_board()

    def add_gold(self, tile_pos: tuple[int]) -> None:
        """Adds gold to the specified tile"""
        tile_to_set = self.get_tile(tile_pos)
        tile_to_set.has_gold = True

    def get_tile(self, tile_pos: list[int]) -> Tile:
        """Returns the tile from the provided position"""
        return self.tile_dict[tuple(tile_pos)]

    def add_wall(self, tile_pos_1: tuple[int], tile_pos_2: tuple[int]) -> None:
        """Adds walls between the provided positions\n
        The method checks the difference between both x and y values\n.
        If the difference between x is -1 that means the provided tiles were for example:\n
        (1,2),(2,2), which means the wall should be located east of tile_1, and west of tile_2
        """
        if tile_pos_1 == tile_pos_2:
            # Will return if the same pos are provided
            return None
        tile_1: Tile = self.get_tile(tile_pos_1)
        tile_2: Tile = self.get_tile(tile_pos_2)

        x_diff = tile_pos_1[0] - tile_pos_2[0]
        # Checks if the x diff is not 0, to make sure only adjacent tiles are being adjusted
        if x_diff:
            if x_diff == -1:
                tile_1.east_border = Borders.WALL
                tile_2.west_border = Borders.WALL
            elif x_diff == 1:
                tile_1.west_border = Borders.WALL
                tile_2.east_border = Borders.WALL
            return

        y_diff = tile_pos_1[1] - tile_pos_2[1]
        if y_diff == -1:
            tile_1.north_border = Borders.WALL
            tile_2.south_border = Borders.WALL
        elif y_diff == 1:
            tile_1.south_border = Borders.WALL
            tile_2.north_border = Borders.WALL

    def create_board(self):
        """Creates a board with unmodified tiles"""
        for x in range(self.map_height):
            # Loops through the map height in a descending order since the bottom of the map has a y value of 1
            y_converted = self.map_height - x

            self.add_tile_row(y_converted, self.map_width)

    def get_border_list(self, y: int, x: int) -> list[Borders]:
        """Gets a list of all the edge borders for the tile position"""
        border_list = list()
        border_list.append(self.get_north_border(y))
        border_list.append(self.get_south_border(y))
        border_list.append(self.get_west_border(x))
        border_list.append(self.get_east_border(x))
        return border_list

    def add_tile_row(self, y_converted: int, map_width: int):
        """Loops through the map width and creates the tiles and adds them to the tile dict"""
        for x in range(map_width):
            x_converted = x + 1
            border_list = self.get_border_list(y_converted, x_converted)

            self.tile_dict[x_converted, y_converted] = Tile(
                (x_converted, y_converted), *border_list
            )

    def get_north_border(self, y_pos: int) -> Borders:
        """Returns out of bounds if y is the same as the height, which means tile is at the top"""
        if y_pos == self.map_height:
            return Borders.OUT_OF_BOUNDS
        return Borders.CLEAR

    def get_south_border(self, y_pos: int) -> Borders:
        """Returns out of bounds if y is 1, meaning the tile is at the bottom"""
        if y_pos == 1:
            return Borders.OUT_OF_BOUNDS
        return Borders.CLEAR

    def get_west_border(self, x_pos: int) -> Borders:
        """Returns out of bounds if x is the same as the map_width, which is all the way to the west"""
        if x_pos == 1:
            return Borders.OUT_OF_BOUNDS
        return Borders.CLEAR

    def get_east_border(self, x_pos: int) -> Borders:
        """Returns out of bounds if x is 1, meaning the tile is all the way to the east"""
        if x_pos == self.map_width:
            return Borders.OUT_OF_BOUNDS
        return Borders.CLEAR
