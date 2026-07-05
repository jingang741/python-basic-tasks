class PhoneUser:
    def __init__(self, name, gender, age, phone_number, balance, brand, phone_type, screen_size, standby_time, score):
        self.name = name
        self.gender = gender
        self.age = age
        self.phone_number = phone_number
        self.balance = balance
        self.brand = brand
        self.phone_type = phone_type
        self.screen_size = screen_size
        self.standby_time = standby_time
        self.score = score

    def send_message(self, content):
        if content == "":
            print("短信内容不能为空")
        else:
            print(f"{self.name} 发送短信：{content}")

    def call(self, target_phone, minutes):
        if target_phone == "":
            print("电话号码不能为空")
            return 0
        if self.balance < 1:
            print("话费小于1元，不能打电话")
            return 0

        if minutes <= 10:
            money = minutes * 1
            score = minutes * 15
        elif minutes <= 20:
            money = minutes * 0.8
            score = minutes * 39
        else:
            money = minutes * 0.65
            score = minutes * 48

        if self.balance < money:
            print("话费不足，不能通话这么久")
            return 0

        self.balance -= money
        self.score += score
        print(f"给 {target_phone} 打电话 {minutes} 分钟，扣费 {money} 元，获得 {score} 积分")
        return money

    def show_info(self):
        print("用户手机信息：")
        print("姓名：", self.name)
        print("性别：", self.gender)
        print("年龄：", self.age)
        print("手机号：", self.phone_number)
        print("话费：", self.balance)
        print("手机品牌：", self.brand)
        print("手机型号：", self.phone_type)
        print("屏幕大小：", self.screen_size)
        print("待机时间：", self.standby_time)
        print("积分：", self.score)


if __name__ == "__main__":
    user = PhoneUser("王五", "男", 22, "13900139000", 100, "华为", "Mate", "6.7英寸", "24小时", 0)
    user.show_info()
    user.send_message("你好")
    user.call("13800138000", 8)
    user.call("13700137000", 15)
    user.call("13600136000", 30)
    user.show_info()
