from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def move_right(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 < 8 and [x1+1, y1] not in obstacles and [x1+1,y1] != [x2,y2] and [x1+1, y1] != [x3,y3]:
        x1+=1
    return x1

def move_left(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 >0 and [x1-1, y1] not in obstacles and [x1-1,y1] != [x2,y2] and [x1-1, y1] != [x3,y3]:
        x1-=1
    return x1

def move_up(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 < 8 and [x1, y1+1] not in obstacles and [x1,y1+1] != [x2,y2] and [x1, y1+1] != [x3,y3]:
        y1+=1
    return y1

def move_down(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 >0 and [x1, y1-1] not in obstacles and [x1,y1-1] != [x2,y2] and [x1, y1-1] != [x3,y3]:
        y1-=1
    return y1


class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial,goal)
        self.obstacles = obstacles

    def successor(self, state):
        succ = {}

        h1x, h1y, = state[0], state[1]
        ox, oy = state[2], state[3]
        h2x, h2y = state[4], state[5]

        # Movement for H1
        x_new = move_right(h1x, h1y, ox, oy, h2x, h2y,  self.obstacles)
        if x_new != h1x:
            succ["RightH1"] = (x_new, h1y, ox, oy, h2x, h2y)

        x_new = move_left(h1x, h1y, h2x, h2y, ox, oy, self.obstacles)
        if x_new != h1x:
            succ["LeftH1"] = (x_new, h1y, ox, oy, h2x, h2y)

        y_new = move_up(h1x, h1y, h2x, h2y, ox, oy, self.obstacles)
        if y_new != h1x:
            succ["UpH1"] = (h1x, y_new, ox, oy, h2x, h2y)

        y_new = move_down(h1x, h1y, h2x, h2y, ox, oy, self.obstacles)
        if y_new != h1x:
            succ["DownH1"] = (h1x, y_new, ox, oy, h2x, h2y)

        # Movement for Oxygen
        x_new = move_right(ox, oy, h2x, h2y, h1x, h1y, self.obstacles)
        if x_new != ox:
            succ["RightO"] = (h1x, h1y, x_new, oy, h2x, h2y)

        x_new = move_left(ox, oy, h2x, h2y, h1x, h1y, self.obstacles)
        if x_new != ox:
            succ["LeftO"] = (h1x, h1y, x_new, oy, h2x, h2y)

        y_new = move_up(ox, oy, h2x, h2y, h1x, h1y, self.obstacles)
        if y_new != h1x:
            succ["UpO"] = (h1x, h1y, ox, x_new, h2x, h2y)

        y_new = move_down(ox, oy, h2x, h2y, h1x, h1y, self.obstacles)
        if y_new != h1x:
            succ["DownO"] = (h1x, h1y, ox, x_new, h2x, h2y)

        # Movement for H2
        x_new = move_right(h2x, h2y, h1x,h1y, ox,oy, self.obstacles)
        if x_new != h2x:
            succ["RightH2"] = (h1x, h1y, ox, oy, x_new, h2y)

        x_new = move_left(h2x, h2y, h1x, h1y, ox, oy, self.obstacles)
        if x_new != h2x:
            succ["LeftH2"] = (h1x, h1y, ox, oy, x_new, h2y)

        y_new = move_up(h2x, h2y, h1x, h1y, ox, oy, self.obstacles)
        if y_new != h2y:
            succ["UpH2"] = (h1x, h1y, ox, oy, h2x, y_new)

        y_new = move_down(h2x, h2y, h1x, h1y, ox, oy, self.obstacles)
        if y_new != h2y:
            succ["DownH2"] = (h1x, h1y, ox, oy, h2x, y_new)

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0]+1 == state[2] and state[2]+1 == state[4] and \
               state[1] == state[3] and state[3] == state[5]


if __name__ == "__main__":

    h1x, h1y = [2,1]
    h2x, h2y = [2, 6]
    ox, oy = [7, 2]

    obstacle = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2],
                 [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]

    state = (h1x, h1y, ox, oy, h2x, h2y)

    problem = Molecule(obstacle, state, )
    solution = breadth_first_graph_search(problem)
    print(solution.solution())
