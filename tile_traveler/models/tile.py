from .borders import Borders


class Tile:
    def __init__(self,
                 position: tuple[int],
                 north_border: Borders,
                 south_border: Borders,
                 west_border: Borders,
                 east_border: Borders,) -> None:
        self.x_pos = position[0]
        self.y_pos = position[1]
        self.north_border = north_border
        self.south_border = south_border
        self.west_border = west_border
        self.east_border = east_border
        self.number_of_gold_coins = 0

    @property
    def has_gold(self) -> bool:
        """Returns true if the tile has 1 or more gold coins"""
        return self.number_of_gold_coins > 0

    def __str__(self) -> str:
        if self.has_gold:
            return f" | {self.x_pos} {self.y_pos} G | "
        return f" | {self.x_pos} {self.y_pos}   | "
