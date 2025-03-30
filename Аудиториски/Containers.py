
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Containers(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):

        # state = (j0,j1) kolku ima u j0 i j1

        successors = dict()

        j0, j1 = state
        c0, c1 = self.capacities

        if j0 > 0:
            successors["Isprazni go sadot J0"] = (0, j1)

        if j1 >0:
            successors["Isprazni go sadot J1"] = (j0, 0)

        if j0 > 0 and j1 < c1:
            delta = min(c1-j1, j0) # go zemame pomaloto deka ako j0 ima pomalku od c1-j1, zemame samo toa od j0
            successors["Preturi od J0 vo J1"] = (j0-delta, c1)

        if j1 > 0 and j0 < c0:
            delta = min(c0-j0, j1)
            successors["Preturi od J1 vo J0"] = (c0, j1-delta)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

if __name__ == "__main__":
    capacities = (10,15)
    current = (10,10)
    goal = (5,15)

    problem = Containers(capacities,current, goal)
    solution = depth_first_graph_search(problem)
    print(solution.solve())
    print(solution.solution())