from ..models.user_moves import UserMove
from ..models.tile import Tile
from ..models.borders import Borders
from ..constants import YES_ANS, NO_ANS


class TileDrawer:
    """Class that returns a string representation for the tile to display on a terminal"""

    def __init__(
        self,
        square_size: int = 10,
        wall_icon: str = "W",
        edge_icon: str = "V",
        gold_icon: str = "G",
        corner_icon: str = "O",
    ) -> None:
        self.square_size = square_size
        self.wall_icon = wall_icon[0:1]
        self.edge_icon = edge_icon[0:1]
        self.gold_icon = gold_icon[0:1]
        self.corner_icon = corner_icon[0:1]

    def get_tile_screen_string(self, tile: Tile) -> str:
        north_south_width = self.square_size
        north_wall = self.__get_horizontal_edge(tile.north_border, north_south_width)
        south_wall = self.__get_horizontal_edge(tile.south_border, north_south_width)
        west_wall = self.__get_edge_icon(tile.west_border)
        east_wall = self.__get_edge_icon(tile.east_border)
        row_modifier = self.square_size % 2
        tile_string = str()
        for row in range((self.square_size) // 3):
            if row == 0:
                tile_string += f"{self.corner_icon}" + f"{north_wall}" + f"{self.corner_icon}" + "\n"
            else:
                tile_string += f"{west_wall}" + f" " * north_south_width + f"{east_wall}" + "\n"
        tile_string += self.__get_vertical_door_row_string(west_wall, east_wall, tile, north_south_width)
        for row in range((self.square_size - row_modifier) // 3):
            tile_string += f"{west_wall}" + f" " * north_south_width + f"{east_wall}" + "\n"
        tile_string += f"{self.corner_icon}" + f"{south_wall}" + f"{self.corner_icon}" + "\n"
        return tile_string

    def __get_vertical_door_row_string(
            self,
            west_wall: str,
            east_wall: str,
            tile: Tile,
            north_south_width: int):
        temp_west = west_wall
        temp_east = east_wall
        if tile.west_border == Borders.CLEAR:
            temp_west = " "
        if tile.east_border == Borders.CLEAR:
            temp_east = " "
        return f"{temp_west}" + f" " * north_south_width + f"{temp_east}" + "\n"

    def __get_edge_icon(self, border_type: Borders) -> str:
        if border_type == Borders.OUT_OF_BOUNDS:
            return self.edge_icon
        return self.wall_icon

    def __get_horizontal_edge(self, border_type: Borders, width: int) -> str:
        if border_type == Borders.OUT_OF_BOUNDS:
            return self.edge_icon * width

        if border_type == Borders.WALL:
            return self.wall_icon * width

        wall_edge = self.wall_icon * ((width // 2) - 1)
        wall_edge = wall_edge[0:-1]

        wall_edge += " " * 2
        wall_edge += "" + " " * (width % 2)  # Incase its an odd number adds another door
        wall_edge += self.wall_icon * (width // 2)
        return wall_edge
