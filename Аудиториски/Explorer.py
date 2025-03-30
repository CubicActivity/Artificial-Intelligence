from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Explorer(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)
        self.grid_size = [8, 6]

    def successor(self, state):

        # (x, y, (x1, y1, d1), (x2, y2, d2) )

        x = state[0]
        y = state[1]

        obs1 = list(state[2]) #torki se nepromenlivi, mora u listi
        obs2 = list(state[3])

        if obs1[2] == 1: #up
            if obs1[1] == self.grid_size[1]:
                obs1[2] = -1
                obs1[1] -= 1
            else:
                obs1[1] +=1
        else: #down
            if obs1[1] == 0:
                obs1[2] = 1
                obs1[1] +=1
            else:
                obs1[1] -= 1


        if obs2[2] == 1: #up
            if obs2[1] == self.grid_size[1]:
                obs2[2] = -1
                obs2[1] -= 1
            else:
                obs2[1] +=1
        else: #down
            if obs2[1] == 0:
                obs2[2] = 1
                obs2[1] +=1
            else:
                obs2[1] -= 1

        obstacles = [(obs1[0], obs1[1]), (obs2[0],obs2[1])]

        successors = {}

        # right, x = x+1
        if x + 1 < self.grid_size[0] and (x+1, y) not in obstacles:
            successors['Right'] = (x+1,y, (obs1[0], obs1[1], obs1[2]), (obs2[0], obs2[1], obs2[2]))

        # left, x = x-1
        if x - 1 > 0 and (x-1, y) not in obstacles:
            successors['Left'] = (x-1,y, (obs1[0], obs1[1], obs1[2]), (obs2[0], obs2[1], obs2[2]))

        # up, y = y+1
        if y + 1 < self.grid_size[1] and (x, y+1) not in obstacles:
            successors['Up'] = (x,y+1, (obs1[0], obs1[1], obs1[2]), (obs2[0], obs2[1], obs2[2]))

        # down, y= y-1
        if y - 1 > 0 and (x, y-1) not in obstacles:
            successors['Down'] = (x,y-1,(obs1[0], obs1[1], obs1[2]), (obs2[0], obs2[1], obs2[2]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]



if __name__ == "__main__":
    obstacle1 = (2,5,-1)
    obstacle2 = (5,0, 1)

    goal = (7,4)
    state = (0,2, obstacle1, obstacle2)

    problem = Explorer(state, goal)
    solution = breadth_first_graph_search(problem)
    print(solution.solution())


