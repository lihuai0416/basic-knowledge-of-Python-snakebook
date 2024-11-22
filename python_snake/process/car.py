#用于9.4
class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

class Battery:
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self,battery_size=40):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    
    def get_range(self):                   #添加内容
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        """检查电瓶容量，如果不是就设置为65"""
        if self.battery_size!= 65:
            self.battery_size = 65

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery = Battery() #将实例用作属性

electric_car = ElectricCar('tesla','model s',2019)
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()