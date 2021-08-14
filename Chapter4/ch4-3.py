class Map:
    def __init__(self, size_y, size_x):
        self.size_x = size_x
        self.size_y = size_y
        self._x = 1
        self._y = 1


    def size(self):
        return f'{self.size_y} x {self.size_x}'

    @property
    def current_coordinates(self):
        return (self._y, self._x)

    @current_coordinates.setter
    def current_coordinates(self, coordinates):
        self._x = coordinates[0]
        self._y = coordinates[1]

    def available_action_count(self, piece):
        count = 0
        for action in piece.actions:
            y, x = self.current_coordinates
            action_y, acion_x = action()
            now_y, now_x = y + action_y, x + acion_x
            if self.size_y >= now_y >= 1 and self.size_x >= now_x >= 1:
                count += 1
        return count

class Knite:
    def __init__(self):
        self.actions = [self.up_l, self.up_r, self.down_l, self.down_r, self.left_u, self.left_d, self.right_u, self.right_d]

    def up_l(self):
        return (-2, -1)
    
    def up_r(self):
        return (-2, 1)

    def down_l(self):
        return (2, -1)

    def down_r(self):
        return (2, 1)

    def left_u(self):
        return (-1, -2)

    def left_d(self):
        return (1, -2)

    def right_u(self):
        return (-1, 2)

    def right_d(self):
        return (1, 2)


input_data = input()
column = int(ord(input_data[0])) - int(ord('a')) + 1
row = int(input_data[1])

k = Knite()

m = Map(8,8)

m.current_coordinates = (column, row)

print(m.available_action_count(k))