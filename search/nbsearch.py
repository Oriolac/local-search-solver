from random import random

from search.definitions.interpretation import Interpretation
import math

from search.solver import Solver


class NeighborSolver(Solver):

    def __init__(self, problem: Interpretation):
        self.problem = problem
        self.best_sol = None
        self.best_cost = math.inf

    def solve(self, max_tries: int = 100, max_restarts: int = 30, rnd_walk: float = 0.1) -> Interpretation:
        for i in range(max_restarts):
            curr_sol = self.problem.get_random_interpretation()
            for mt in range(max_tries):
                if random() < rnd_walk:
                    curr_sol = curr_sol.get_random_walk()
                else:
                    curr_sol = curr_sol.get_best_neighbor()

                if curr_sol.cost() < self.best_cost:
                    self.best_sol = curr_sol.copy()
                    self.best_cost = curr_sol.cost()
                    if self.best_cost == 0:
                        return self.best_sol
        return self.best_sol


def main(model: Interpretation) -> None:
    best_sol = NeighborSolver(model).solve()
    print(best_sol.cost())
    best_sol.print()
