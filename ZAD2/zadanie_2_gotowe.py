import random
import math

# Stworzeniu punktów
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
# Wymiary planszy
board_width = 5000
board_height = 5000

#answer = input("Czy chcesz stworzyć własne punkty? (Y/N)")

#Tworzenie randomowychpunktów na planszy
def random_point(width, height):
    return Point(random.randint(0, width), random.randint(0, height))

#Początkowy i końcowy punkt
start_point = random_point(board_width, board_height)
end_point = random_point(board_width, board_height)

#Liczba punktów
num_points_n = random.randint(1, 5000)
points_n = [random_point(board_width, board_height) for _ in range(num_points_n)]

# Losowanie punktów k
k = random.randint(1, num_points_n)
points_to_visit = points_n[:k]


#Obliczanie dystansu przez pitagorasa
def distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

#Dla Astar do szacowania długości między punktami
def heuristic(point):
    return distance(point, end_point)

#Znajdowanie sąsiadów dla punktów
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

#Algorytm Astar
def astar(start, end):
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


    return None

#Znajdywanie ścieżki dla punktów wylosowanych.
def find_optimal_path(start, end, points_to_visit):
    path = []
    current_point = start

    for point_to_visit in points_to_visit:
        #Tutaj wywoływany jest Astar dla punktów do odiwedzenia
        result = astar(current_point, point_to_visit)
        if result:
            path.extend(result[:-1])
            current_point = result[-1]
        else:
            return None
    last_leg = astar(current_point, end, points_to_visit)
    if last_leg:
        path.extend(last_leg)
        return path
    return None


#Wypisanie na konsoli

#print("Punkty n:")
#for point in points_n:
#    print(f"({point.x}, {point.y})")
print("Punkty do odwiedzenia:")
for point in points_to_visit:
    print(f"({point.x}, {point.y})")

print(f"Liczba punktów k: {k}")
print(f"Liczba punktów n: {num_points_n}")

print("Punkt początkowy: ")
print(f"({start_point.x}, {start_point.y})")

print("Punkt końcowy: ")
print(f"({end_point.x}, {end_point.y})")

total_distance=0
# Konwertowanie punktów na int
points_to_visit_int = [Point(int(point.x), int(point.y)) for point in points_to_visit]
# Obliczanie dystansu
for i in range(len(points_to_visit_int) - 1):
    point1 = points_to_visit_int[i]
    point2 = points_to_visit_int[i + 1]
    distance_between_points = distance(point1, point2)
    total_distance += distance_between_points

print(f"Łączna odległość między punktami: {total_distance}")

#Zapisywanie do pliku
file_name = open("Wynik.csv","w")
file_name.write(f'Punkt poczatkowy: {start_point.x}, {start_point.y}\n')
file_name.write(f'Punkt koncowy: {end_point.x}, {end_point.y}\n')
file_name.write(f'Liczba punktow n: {num_points_n}\n')
file_name.write(f'Liczba punktow k: {k}\n')
file_name.write(f"Punkty do odiwedzenia: \n")
for points in points_to_visit:
    file_name.write(f"{point.x},{point.y};")
file_name.write(f"Łączna długość ścieżki: {total_distance}")
file_name.close()

