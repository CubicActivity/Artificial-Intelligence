from searching_framework import Problem, astar_search

class House(Problem):
    def __init__(self, grid_size, obstacles, initial, goal):
        super().__init__(initial,goal)
        self.grid_size = grid_size
        self.obstacles = obstacles

    def successor(self, state):
        successors = {}

        px = state[0]
        py = state[1]

        #Move human

        # Move up
        if py+1 < self.grid_size and (px, py+1) not in self.obstacles:
            successors['Gore'] = (px, py+1)

        # Move down
        if py-1 >=0 and (px, py-1) not in self.obstacles:
            successors['Dolu'] = (px, py-1)

        # Move Left
        if px-1 >=0 and (px-1, py) not in self.obstacles:
            successors['Levo'] = (px-1, py)

        # Move Right 2
        if px+2 < self.grid_size and (px+1, py) not in self.obstacles and (px+2, py) not in self.obstacles:
            successors['Desno 2'] = (px+2, py)

        # Move Right 3
        if px + 3 < self.grid_size and (px+1, py) not in self.obstacles and (px+2, py) not in self.obstacles and (px + 3, py) not in self.obstacles:
            successors['Desno 3'] = (px + 3, py)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]

    def h(self, node):
        return (abs(node.state[0] - self.goal[0]) + abs(node.state[1] - self.goal[1]))/3



if __name__ == '__main__':
    size = int(input())
    numofwalls = int(input())
    walls = []

    for n in range(numofwalls):
        x, y = input().split(",")
        x = int(x)
        y = int(y)
        walls.append((x,y))

    playerX,playerY = input().split(",")
    playerX=int(playerX)
    playerY=int(playerY)

    hX, hY = input().split(",")
    hX = int(hX)
    hY = int(hY)

    problem = House(size, walls, (playerX,playerY), (hX,hY))
    solution = astar_search(problem)
    if solution:
        print(solution.solution())
    else:
        print("No solution!")