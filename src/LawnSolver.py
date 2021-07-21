from src.Mower import Mower


class LawnSolver:
    def __init__(self, max_x: int, max_y: int):
        self.max_x = max_x
        self.max_y = max_y

    def solve(self, initial_position: str, directions: str) -> Mower:
        arguments = initial_position.split()
        if len(arguments) != 3:
            raise AssertionError('The starting position should look like 1, 1, N')

        mower = Mower(int(arguments[0]), int(arguments[1]), arguments[2])
        for mower_input in directions:
            if mower_input == "A":
                mower.move_forward(self.max_x, self.max_y)
            if mower_input == "G":
                mower.turn_left()
            if mower_input == "D":
                mower.turn_right()

        return mower
