from .tile_logic import TileLogic
from ..models.player import Player
from ..models.user_moves import UserMove
from ..models.tile import Tile
from ..models.borders import Borders


class PlayerLogic:
    """Logic for the player"""

    def __init__(
        self, start_pos: tuple[int], win_pos: tuple[int], tile_logic: TileLogic
    ) -> None:

        self.tile_logic = tile_logic
        self.tile_dict: dict[tuple[int], Tile] = self.tile_logic.tile_dict
        self.win_pos = win_pos
        self.player = Player(start_pos)

    def pull_lever(self) -> bool:
        """Pulls the lever, increments the gold the player has and removes it from the current tile"""

        if self.tile_logic.pull_gold_lever(self.current_tile):
            self.player.gold += 1
            return True
        return False

    @property
    def current_player_pos(self) -> tuple[int]:
        """Returns the current player position"""
        return self.player.current_pos

    @property
    def current_tile(self) -> Tile:
        """Returns the tile object of where the player currently is"""
        return self.tile_dict[self.current_player_pos]

    @property
    def cur_tile_has_gold(self) -> bool:
        """Returns true if the current tile has gold"""
        return self.current_tile.has_gold

    def get_available_moves(self) -> list[UserMove]:
        """Returns a list of all available moves that the current tile has"""
        current_tile = self.current_tile
        avail_list = list()
        if current_tile.north_border == Borders.CLEAR:
            avail_list.append(UserMove.NORTH)
        if current_tile.south_border == Borders.CLEAR:
            avail_list.append(UserMove.SOUTH)
        if current_tile.east_border == Borders.CLEAR:
            avail_list.append(UserMove.EAST)
        if current_tile.west_border == Borders.CLEAR:
            avail_list.append(UserMove.WEST)
        return avail_list

    def move_player(self, user_move: UserMove) -> None:
        """Moves the player and updates player position and increments the player moves by one"""
        y_pos = self.current_player_pos[1]
        x_pos = self.current_player_pos[0]

        if user_move == UserMove.NORTH:

            y_pos += 1
        if user_move == UserMove.SOUTH:
            y_pos -= 1
        if user_move == UserMove.WEST:
            x_pos -= 1
        if user_move == UserMove.EAST:
            x_pos += 1

        self.player.current_pos = (x_pos, y_pos)
        self.player.number_of_moves += 1
