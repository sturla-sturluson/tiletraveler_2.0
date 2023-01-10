from ..logic import PlayerLogic

from ..models.user_moves import UserMove
from ..constants import YES_ANS, NO_ANS
from .tile_drawer import TileDrawer
import os


def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class UiHandler:
    def __init__(self, player_logic: PlayerLogic) -> None:
        self.player_logic = player_logic
        self.player = self.player_logic.player
        self.tiledrawer = TileDrawer()


    def print_game_status(self, invalid_input_string: str,show_tile_string:bool = False):
        """Clears the terminal and prints the gold amount string and available moves"""
        clear_terminal()
        print(invalid_input_string)
        if show_tile_string:
            tile_string = self.tiledrawer.get_tile_screen_string(self.player_logic.current_tile)
            print(tile_string)
        print(self.gold_amount_string)
        print(self.available_moves_string)

    def print_level_prompt_string(self, invalid_input_string: str,show_tile_string:bool = False):
        """Clears terminal and prints out the lever prompt string"""
        clear_terminal()
        print(invalid_input_string)
        if show_tile_string:
            tile_string = self.tiledrawer.get_tile_screen_string(self.player_logic.current_tile)
            print(tile_string)
        print(self.gold_amount_string)
        print(self.lever_prompt_string)



    @property
    def lever_prompt_string(self) -> str:
        """Returns a formatted lever prompt st ring"""
        return f"You see a lever.\nPULL LEVER {YES_ANS}/{NO_ANS}"

    @property
    def gold_amount_string(self) -> str:
        """Returns a string with the current amount of gold coins the player has"""
        return f"You have {self.player.gold} gold coins"

    @property
    def available_moves_string(self):
        """Returns a formatted string with all available moves"""
        avail_dir_list = self.player_logic.get_available_moves()
        direction_to_name = {
            UserMove.NORTH: "(N)orth",
            UserMove.EAST: "(E)ast",
            UserMove.WEST: "(W)est",
            UserMove.SOUTH: "(S)outh",
        }

        return_str = "You can travel: "

        for direction in avail_dir_list:
            return_str += direction_to_name[direction]
            return_str += " or "

        return_str = return_str.rstrip(" or ")
        return return_str + "."
