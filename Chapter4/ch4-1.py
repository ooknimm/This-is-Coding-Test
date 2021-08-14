class InvalidMapRangeException(Exception):
    """지도 범위를 벗어나면 발생하는 에러"""

class Coordinate:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def coordinates(self):
        return (self._y, self._x)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

class Move(Coordinate):

    def __repr__(self):
        return f'Move Class <y: {self._y}, x: {self._x}>'

class Map(Coordinate):
    def __init__(self, n):
        super().__init__(1,1)
        self.n = n    

    def _move_check(self, number):
        if number < 1 or number > self.n:
            raise InvalidMapRangeException
        return number

    @Coordinate.x.setter
    def x(self, value):
        self._move_check(value)
        self._x = value

    @Coordinate.y.setter
    def y(self, value):
        self._move_check(value)
        self._y = value

    def __repr__(self):
        return f'Man Class <y: {self._y}, x: {self._x}>'

move = {
    'L': Move(-1, 0),
    'R': Move(1, 0),
    'U': Move(0, -1),
    'D': Move(0, 1)
}

n = 5

man = Map(n)
plans = input().split()

plans = ['R', 'R', 'R', 'U', 'D', 'D']

for i, plan in enumerate(plans):
    try:
        my, mx = move[plan].coordinates()
    except KeyError:
        print('적절한 값이 아닙니다')
        break
    try:
        man.x += mx
        man.y += my
    except InvalidMapRangeException:
        print('벗어남')
        continue

print(*man.coordinates())
