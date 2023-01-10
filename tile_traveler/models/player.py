class Player:
    def __init__(self, start_pos: list[int]) -> None:
        self.current_pos = start_pos
        self.gold = 0
        self.number_of_moves = 0
