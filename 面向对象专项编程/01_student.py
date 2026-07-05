class Student:
    def __init__(self, student_id, name, age, gender, height, weight, score, address, phone):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.score = score
        self.address = address
        self.phone = phone

    def study(self, content, time):
        print(f"{self.name} 正在学习 {content}，学习了 {time} 小时")

    def play_game(self, game_name, time):
        print(f"{self.name} 正在玩 {game_name}，玩了 {time} 小时")

    def run(self):
        print(f"{self.name} 正在跑步，感觉很累")

    def eat(self, food):
        print(f"{self.name} 正在吃 {food}，体重可能会变重")

    def show_info(self):
        print("学生信息：")
        print("学号：", self.student_id)
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("性别：", self.gender)
        print("身高：", self.height)
        print("体重：", self.weight)
        print("成绩：", self.score)
        print("家庭地址：", self.address)
        print("电话：", self.phone)


if __name__ == "__main__":
    stu = Student("1001", "张三", 18, "男", 175, 65, 90, "北京", "13800138000")
    stu.show_info()
    stu.study("Python", 2)
    stu.play_game("王者荣耀", 1)
    stu.run()
    stu.eat("米饭")
