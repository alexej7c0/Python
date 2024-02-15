class Box_office:
    total = 0
    def top_up(self, x):
        Box_office.total += x
    def count_1000(self):
        print('В кассе недостаточно денег' if Box_office.total < 1000 else f'В кассе осталось {Box_office.total // 1000} целых тысяч')
    def take_away(self, x):
        Box_office.total -= x