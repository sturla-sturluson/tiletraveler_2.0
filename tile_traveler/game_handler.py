from .logic.player_logic import PlayerLogic
from .ui.ui_handler import UiHandler, clear_terminal
from .models.user_moves import UserMove
from .logic.board import BoardLogic
from .constants import YES_ANS, NO_ANS, QUIT_COMMAND, INPUT_FIELD

INVALID_CHOICE = "Not valid input try again."
INVALID_DIRECTION = "Not valid direction try again."


def setup_default_board() -> BoardLogic:
    """Sets up default board size, wall locations and gold locations"""
    board_generator = BoardLogic(3)
    board_generator.add_wall((1, 1), (2, 1))
    board_generator.add_wall((2, 1), (3, 1))
    board_generator.add_wall((2, 2), (3, 2))
    board_generator.add_wall((2, 3), (2, 2))
    board_generator.add_gold((1, 2))
    board_generator.add_gold((2, 2))
    board_generator.add_gold((2, 3))
    board_generator.add_gold((3, 3))
    return board_generator


def user_move_converter(user_move: str):
    """Translates the moves from the user to the UserMove enum"""
    if user_move == "n":
        return UserMove.NORTH
    if user_move == "s":
        return UserMove.SOUTH
    if user_move == "e":
        return UserMove.EAST
    if user_move == "w":
        return UserMove.WEST
    return ""


def game_loop():
    """Runs a default setup of the game"""
    win_pos = (3, 1)
    start_pos = (1, 1)
    default_board = setup_default_board()
    logic = PlayerLogic(start_pos, win_pos, default_board)
    ui_handler = UiHandler(logic)
    game_status = True
    user_answer = ""
    invalid_input_string = ""
    player = logic.player
    while game_status:
        while True:
            ui_handler.print_game_status(invalid_input_string)
            user_answer = input(INPUT_FIELD).lower().strip()
            if user_answer == QUIT_COMMAND:
                return QUIT_COMMAND
            user_answer = user_move_converter(user_answer)
            avail_moves = logic.get_available_moves()
            if user_answer in avail_moves:
                invalid_input_string = ""
                break
            invalid_input_string = INVALID_DIRECTION

        logic.move_player(user_answer)
        if logic.cur_tile_has_gold:
            while True:
                ui_handler.print_level_prompt_string(invalid_input_string)
                user_answer = input(INPUT_FIELD).strip().lower()
                if user_answer == QUIT_COMMAND:
                    return QUIT_COMMAND
                if user_answer == YES_ANS:
                    logic.pull_lever()
                    invalid_input_string = ""
                    break
                elif user_answer == NO_ANS:
                    invalid_input_string = ""
                    break

                invalid_input_string = INVALID_CHOICE
        if player.current_pos == logic.win_pos:
            break
    print("You won!")
    print(f"You ended with {player.gold} gold coins.")
    print(f"You completed the game in {player.number_of_moves} moves.")


def run_game():
    """Runs the main game loop"""
    clear_terminal()
    print(f"Welcome to Tile Traveler\nPress any key to start, {QUIT_COMMAND} to quit at any point")
    input(INPUT_FIELD)
    game_loop()
    while True:
        answer = input(f"Do you want to play again?(Y/N)\n{INPUT_FIELD}")
        if answer == YES_ANS:
            game_loop()
        else:
            break
