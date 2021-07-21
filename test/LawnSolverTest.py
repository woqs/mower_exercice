import unittest
from src.LawnSolver import LawnSolver
from src.Mower import Mower


class LawnSolverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = LawnSolver(1, 1)

    def test_return_type(self):
        result = self.solver.solve("1 2 N", "ADGAGDAGADGAG")
        self.assertIsInstance(result, Mower)

    def test_raise_exception(self):
        for bad_start in ["1 1", "1 2 3 5"]:
            with self.assertRaises(AssertionError):
                self.solver.solve(bad_start, "ADGAGDAGADGAG")
