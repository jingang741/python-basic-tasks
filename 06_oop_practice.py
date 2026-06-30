"""面向对象专项编程。"""

class Student:
    def __init__(self, sid, name, age, sex, height, weight, score, address, phone):
        self.sid = sid
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.score = score
        self.address = address
        self.phone = phone

    def study(self, hours):
        print(f"{self.name} 学习了 {hours} 小时。")

    def play_game(self, game):
        print(f"{self.name} 正在玩 {game}。")

    def code(self, lines):
        print(f"{self.name} 写了 {lines} 行代码。")

    def sum_numbers(self, *nums):
        return sum(nums)


class Car:
    def __init__(self, model, wheels, color, weight, tank):
        self.model = model
        self.wheels = wheels
        self.color = color
        self.weight = weight
        self.tank = tank

    def run(self, feature):
        print(f"{self.color}{self.model} 正在跑，特点：{feature}")


class Laptop:
    def __init__(self, model, standby, color, weight, cpu, memory, disk):
        self.model = model
        self.standby = standby
        self.color = color
        self.weight = weight
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def play_game(self, game):
        print(f"{self.model} 正在运行游戏：{game}")

    def work(self):
        print(f"{self.model} 正在办公。")


class Monkey:
    def __init__(self, kind, sex, color, weight):
        self.kind = kind
        self.sex = sex
        self.color = color
        self.weight = weight

    def make_fire(self, material):
        print(f"{self.kind} 用 {material} 造火。")

    def learn(self, *things):
        print(f"{self.kind} 学习了：{things}")


class Person:
    def __init__(self, name, sex, age, money, phone_brand, battery, screen, standby, points=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.money = money
        self.phone_brand = phone_brand
        self.battery = battery
        self.screen = screen
        self.standby = standby
        self.points = points

    def send_message(self, text):
        print(f"{self.name} 发送短信：{text}")

    def call(self, phone_number, minutes):
        if not phone_number:
            print("电话号码不能为空。")
            return
        if self.money < 1:
            print("话费不足。")
            return
        if minutes <= 10:
            price, point = 1, 15
        elif minutes <= 20:
            price, point = 0.8, 39
        else:
            price, point = 0.65, 48
        cost = minutes * price
        if self.money < cost:
            print("话费不够本次通话。")
            return
        self.money -= cost
        self.points += minutes * point
        print(f"拨通 {phone_number}，通话 {minutes} 分钟，扣费 {cost:.2f} 元，积分 {self.points}。")


def main():
    stu = Student("001", "小明", 18, "男", 175, 65, 90, "北京", "13800000000")
    stu.study(2)
    stu.play_game("王者荣耀")
    stu.code(100)
    print("求和结果：", stu.sum_numbers(1, 2, 3, 4, 5))

    for car in ["法拉利", "宝马", "铃木", "五菱", "拖拉机"]:
        Car(car, 4, "红色", "1吨", "50L").run("代步")

    Laptop("ThinkPad", "10小时", "黑色", "1.5kg", "i5", "16G", "512G").work()
    Monkey("金丝猴", "公", "金色", "30kg").learn("写字", "算数")
    p = Person("张三", "男", 20, 100, "华为", "5000mAh", "6.7寸", "24小时")
    p.send_message("你好")
    p.call("13800000000", 12)


if __name__ == "__main__":
    main()
