import unittest
from src.Mower import Mower


class MowerTest(unittest.TestCase):

    def test_turn_left(self):
        for start, end in {"N": "W", "E": "N", "S": "E", "W": "S"}.items():
            mower = Mower(1, 1, start)
            mower.turn_left()
            self.assertEqual(mower.direction, end)

    def test_turn_right(self):
        for start, end in {"N": "E", "E": "S", "S": "W", "W": "N"}.items():
            mower = Mower(1, 1, start)
            mower.turn_right()
            self.assertEqual(mower.direction, end)

    def test_move_forward(self):
        for direction, position in {"N": 2, "E": 2, "S": 0, "W": 0}.items():
            mower = Mower(1, 1, direction)
            mower.move_forward(5, 5)
            if direction == "E" or direction == "W":
                self.assertEqual(mower.x, position)
            else:
                self.assertEqual(mower.y, position)

    def test_edge_move_forward(self):
        for direction, position in {"N": 5, "E": 5}.items():
            mower = Mower(5, 5, direction)
            mower.move_forward(5, 5)
            if direction == "N":
                self.assertEqual(mower.x, position)
            else:
                self.assertEqual(mower.y, position)

        for direction, position in {"S": 0, "W": 0}.items():
            mower = Mower(0, 0, direction)
            mower.move_forward(5, 5)
            if direction == "S":
                self.assertEqual(mower.x, position)
            else:
                self.assertEqual(mower.y, position)


if __name__ == '__main__':
    unittest.main()
