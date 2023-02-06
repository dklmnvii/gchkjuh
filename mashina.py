class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.type = car_type
        self.year = year
        
    def start(self):
        print('Двигатель автомобиля заведен')
        
    def stop(self):
        print('Двигатель автомобиля остановлен')
        
    def set_year(self, year):
        self.year = year
        print(year)
        
    def set_type(self, car_type):
        self.type = car_type
        print(car_type)
        
    def set_color(self, color):
        self.color = color
        print(color)
        
car = Car('green', 'BMW', 2023)
car.start()
car.stop()
car.set_year(2023)
car.set_type('BMW')
car.set_color('green')