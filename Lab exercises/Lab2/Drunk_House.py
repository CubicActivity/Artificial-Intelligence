from searching_framework import Problem, astar_search

class Drunk(Problem):

    def __init__(self, walls, initial, goal=None):
        super().__init__(initial, goal)
        self.walls = walls

    def successor(self, state):

        successors = {}

        px = state[0]
        py = state[1]

        hx = state[2]
        hy = state[3]

        hd = state[4]

        walls = self.walls

        # px, py, hx, hy, obstacles (can climb on)

        #House moving
        if hd == "desno" and hx<4:
            hx+=1

        elif hd == "desno":
            hd = "levo"
            hx-=1

        elif hd == "levo" and hx>0:
            hx-=1

        elif hd == "levo":
            hd = "desno"
            hx+=1


        house = (hx,hy)


        #Move human
        #Stay in place
        successors["Stoj"] = (px, py, hx, hy, hd)

        #UP1
        if (px, py+1) in walls or (px,py+1) == house:
            successors["Gore 1"] = (px, py+1, hx, hy, hd)
        #UP2
        if (px, py + 2) in walls or (px,py+2) == house:
            successors["Gore 2"] = (px, py+2, hx, hy, hd)

        #Gore Desno 1
        if px+1 <= 4 and (px+1, py+1) in walls or (px+1,py+1) == house:
            successors["Gore-desno 1"] = (px+1, py+1, hx, hy, hd)

        #Gore Desno 2
        if px+2 <= 4 and (px+2, py+2) in walls or (px+2,py+2) == house:
            successors["Gore-desno 2"] = (px+2, py+2, hx, hy, hd)

        #Gore levo 1
        if px-1 >=0 and (px-1, py+1) in walls or (px-1,py+1) == house:
            successors["Gore-levo 1"] = (px-1, py+1, hx, hy, hd)

        #Gore levo 2
        if px-2 >=0 and (px-2, py+2) in walls or (px-2,py+2) == house:
            successors["Gore-levo 2"] = (px-2, py+2, hx, hy, hd)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == state[2] and state[1] == state[3]

    def h(self, node):
         return abs(node.state[1]-node.state[3])/2
        #return (abs(node.state[0] - node.state[2]) + abs(node.state[1] - node.state[3]))/5

if __name__ == "__main__":

    playerX, playerY = input().split(',')
    playerX = int(playerX)
    playerY = int(playerY)
    houseX, houseY = input().split(',')
    houseX = int(houseX)
    houseY = int(houseY)

    houseD = input()
    allowed = [(1,0), (2,0), (3,0), (1,1), (2,1), (0,2), (2,2), (4,2), (1,3), (3,3), (4,3), (0,4), (2,4), (2,5), (3,5), (0,6), (2,6), (1,7), (3,7)]


    problem = Drunk(allowed, (playerX,playerY,houseX,houseY, houseD))
    solution = astar_search(problem)

    if solution:
        print(solution.solution())
    else:
        print("No solution")
