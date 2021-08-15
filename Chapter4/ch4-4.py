from collections.abc import Sequence
from enum import Enum

class MapEnum(Enum):
    SEA = 1
    RAND = 0
    MOVED = 9

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Map:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.map = []

    def print_map(self):
        for m in self.map:
            print(' '.join(map(str, m)))

    def update_map(self, row):
        if not isinstance(row, Sequence):
            raise Exception('적절한 값이 아닙니다.')
        for i in row:
            if isinstance(i, Sequence):
                self.update_map(i)
                continue
            if i != MapEnum.SEA.value and i != MapEnum.RAND.value:
                raise Exception('적절한 값이 아닙니다.')
        self.map.append(row)

class Character:
    def __init__(self, map, current_location=(1,1), direction=Direction.NORTH):
        self.step_count = 1
        self.block = 0
        self.current_map = map
        self.direction = direction
        self.current_location = current_location
        self.trace = [self.current_location]
        self.set_moved(*self.current_location)

    def change_direction(self):
        if self.block > 4:
            return False
        self.direction = (self.direction - 1) % 4
        self.block += 1
        return True
    
    def search_location(self):
        y, x = self.current_location
        if self.direction == Direction.NORTH.value:
            y -= 1
        elif self.direction == Direction.EAST.value:
            x += 1
        elif self.direction == Direction.SOUTH.value:
            y += 1
        elif self.direction == Direction.WEST.value:
            x -= 1
        return (y, x)
        
    def set_moved(self, y, x):
        self.current_map[y][x] = MapEnum.MOVED.value

    def move(self, coordinates):
        y, x = coordinates
        try:
            target = self.current_map[y][x]
        except KeyError:
            print('존재하지 않는 지역입니다.')
            return False
        if target == MapEnum.SEA.value or target == MapEnum.MOVED.value:
            return False
        self.set_moved(y,x)
        self.step_count += 1
        self.trace.append(coordinates)
        self.current_location = coordinates
        self.block = 0
        return True

        
n, m = map(int, input().split())

m = Map(n,m)

y, x, d = map(int, input().split())

rows = [list(map(int, input().split())) for i in range(n)]
m.update_map(rows)
m.print_map()

c = Character(m.map, current_location=(y, x), direction=d)

while True:
    available = c.change_direction()
    if not available:
        print('result: ', c.step_count)
        print(c.trace)
        break
    
    coordinates = c.search_location()
    c.move(coordinates)


