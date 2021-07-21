class Mower:
    directions = ('N', 'E', 'S', 'W')
    move_to = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def __init__(self, x: int, y: int, direction: str):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self) -> None:
        self.direction = self.directions[self.directions.index(self.direction) - 1]

    def turn_right(self) -> None:
        if self.directions[len(self.directions) - 1] == self.direction:
            self.direction = self.directions[0]
        else:
            self.direction = self.directions[self.directions.index(self.direction) + 1]

    def move_forward(self, max_x: int, max_y: int) -> None:
        new_position = self.move_to[self.directions.index(self.direction)]
        next_x = self.x + new_position[0]
        if max_x >= next_x >= 0:
            self.x = next_x
        next_y = self.y + new_position[1]
        if max_y >= next_y >= 0:
            self.y = next_y

    def __str__(self) -> str:
        return "{} {} {}".format(self.x, self.y, self.direction)
