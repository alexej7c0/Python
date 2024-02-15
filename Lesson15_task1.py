class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def auto_param(self):
        return f'Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}'

autobus = Transport('Renault Logan', 180, 12)

print(autobus.auto_param())