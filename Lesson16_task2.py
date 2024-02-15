import math


class Turtle:
    x = 0
    y = 0
    s = 1

    # - увеличивает y на s
    def go_up(self):
        self.y += self.s

    #  - уменьшает y на s
    def go_down(self):
        self.y -= self.s

    #  - уменьшает x на s
    def go_left(self):
        self.x -= self.s

    # - увеличивает x на s
    def go_right(self):
        self.x += self.s

    # - увеличивает s на 1
    def evolve(self):
        self.s += 1

    # - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
    def degrade(self):
        if self.s > 1:
            self.s -= 1

        else:
            print('"s" не может принимать значене ≤ 0')

    # - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        return math.ceil(dx / self.s) + math.ceil(dy / self.s)
