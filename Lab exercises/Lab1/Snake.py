from searching_framework import Problem, breadth_first_graph_search


class Snake(Problem):
    def __init__(self, initial, red_apples):
        super().__init__(initial)
        self.red_apples = red_apples
        self.length = 10
        self.moves = ((0, -1),
            (1, 0),
            (0, 1),
            (-1, 0))

    def goal_test(self, state):
        return len(state[2]) == 0

    def successor(self, state):
        successors = dict()
        acts = ("ProdolzhiPravo", "SvrtiDesno", "SvrtiLevo")
        directions = (0, 1, -1)
        for action, direction in zip(acts, directions):
            rez = self.move(state, direction)
            if rez is not None:
                successors[action] = rez

        return successors

    def move(self, state, direction):
        next_snake_direction = (state[1] + direction) % 4
        snake_segments = list(state[0])
        snake_head = (snake_segments[0][0]+self.moves[next_snake_direction][0], snake_segments[0][1]+ self.moves[next_snake_direction][1])
        apples = list(state[2])
        x,y= snake_head
        if x < 0 or x >= self.length \
                or y < 0 or y >= self.length:
            return None
        if (x, y) in self.red_apples:
            return None
        if (x, y) in snake_segments[1:len(snake_segments)-1]:
            return None
        snake_segments.insert(0, snake_head)
        if (x, y) in apples:
            apples.remove((x, y))
        else:
            snake_segments.pop()

        return tuple(snake_segments), next_snake_direction, tuple(apples)

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    n = int(input())

    green_apples = []
    red_apples = []

    for i in range(n):
        cords = input().split(',')
        green_apples.append((int(cords[0]),9-int(cords[1])))
    green_apples = tuple(green_apples)

    n = int(input())
    for i in range(n):
        cords = input().split(',')
        red_apples.append((int(cords[0]),9-int(cords[1])))
    red_apples = tuple(red_apples)

    #Pocetnite delovi od zmijata
    parts = ((0, 2), (0, 1), (0, 0))

    #Initial state so snakeParts, direction, i green apples (x,y)
    initial_state = (parts, 2, green_apples)
    game = Snake(initial_state, red_apples)

    #BFS search
    node = breadth_first_graph_search(game)
    if node is not None:
        print(node.solution())
    else:
        print('[]')