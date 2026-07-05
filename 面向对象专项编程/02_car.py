class Car:
    def __init__(self, brand, model, price, color, fuel, size, function):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.fuel = fuel
        self.size = size
        self.function = function

    def run(self):
        print(f"{self.color} 的 {self.brand}{self.model} 正在行驶")

    def show_function(self):
        print(f"这辆车的功能是：{self.function}")

    def off_road(self):
        print(f"{self.brand}{self.model} 可以越野")

    def show_info(self):
        print("汽车信息：")
        print("品牌：", self.brand)
        print("型号：", self.model)
        print("价格：", self.price)
        print("颜色：", self.color)
        print("燃料：", self.fuel)
        print("大小：", self.size)
        print("功能：", self.function)


if __name__ == "__main__":
    car = Car("长城", "坦克300", 200000, "黑色", "汽油", "中型", "代步和越野")
    car.show_info()
    car.run()
    car.show_function()
    car.off_road()
