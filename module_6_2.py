# Задача "Изменять нельзя получать":
class Vehicle: # любой транспорт
    # owner(str) = True # владелец транспорта. (владелец может меняться)
    # __model(str) = True # модель (марка) транспорта. (мы не можем менять название модели)
    # __engine_power(int) = True # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    # __color(str) = True # название цвета. (мы не можем менять цвет автомобиля своими руками)
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white'] # список допустимых цветов для окрашивания. (Цвета написать свои)
    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print('Владелец: ', self.owner)
    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle): # седан и наследник класса Vehicle
    __PASSENGERS_LIMIT = 5 # в седан может поместиться только 5 пассажиров


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

# Вывод на консоль:
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: blue
# Владелец: Fedos
# Нельзя сменить цвет на Pink
# Модель: Toyota Mark II
# Мощность двигателя: 500
# Цвет: BLACK
# Владелец: Vasyok