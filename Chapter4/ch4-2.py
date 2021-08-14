class TimeCount:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
        self.limit_h = 0

    def _time_increase(self):
        self.s += 1
        if self.s >= 60:
            self.m += 1
            self.s = 0
        if self.m >= 60:
            self.h = (self.h + 1) % 24
            self.m = 0

    def _str_time(self):
        return '{:02}:{:02}:{:02}'.format(self.h, self.m, self.s)

    def __iter__(self):
        for _ in range(self.limit_h):
            yield self._str_time()
            self._time_increase()

    def __call__(self, h=24):
        if h > 24:
            print('n must be <= 24')
            raise Exception
        self.limit_h = n * 60 * 60
        return self


t = TimeCount()

n = int(input())

count = 0
for i in t(n+1):
    if '3' in i:
        count += 1

print(count)