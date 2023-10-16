import random
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

board_width = 50
board_height = 50

start_point = Point(0, 0)
end_point = Point(board_width - 1, board_height - 1)

num_points_n = random.randint(1, 10)
points_n = [Point(random.randint(0, board_width - 1), random.randint(0, board_height - 1)) for _ in range(num_points_n)]

def distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

def heuristic(point):
    return distance(point, end_point)

def get_neighbors(point):
    neighbors = []
    if point.x > 0:
        neighbors.append(Point(point.x - 1, point.y))
    if point.x < board_width - 1:
        neighbors.append(Point(point.x + 1, point.y))
    if point.y > 0:
        neighbors.append(Point(point.x, point.y - 1))
    if point.y < board_height - 1:
        neighbors.append(Point(point.x, point.y + 1))
    return neighbors

def astar(start, end, points_to_visit):
    open_list = {start: 0}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start)}
    closed_list = set()

    while open_list:
        current = min(open_list, key=lambda point: f_score[point])

        if current == end:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        del open_list[current]
        closed_list.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_list:
                continue

            tentative_g_score = g_score[current] + distance(current, neighbor)

            if neighbor not in open_list or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor)
                open_list[neighbor] = f_score[neighbor]

    return None

k = random.randint(1, num_points_n)
points_to_visit = points_n[:k]

path = astar(start_point, end_point, points_to_visit)

if path:
    print(f"Liczba punktów k: {k}")
    print(f"Liczba punktów n: {num_points_n}")
    print("Punkty do odwiedzenia:")
    for point in reversed(points_to_visit):
        print(f"({point.x}, {point.y})")
else:
    print("Nie znaleziono ścieżki.")
