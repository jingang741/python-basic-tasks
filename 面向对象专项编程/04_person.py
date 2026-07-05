class Person:
    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def work(self, material):
        print(f"{self.name} 正在搬运 {material}")

    def learn_language(self, languages):
        print(f"{self.name} 正在学习语言：")
        for language in languages:
            print(language)

    def show_info(self):
        print("人员信息：")
        print("姓名：", self.name)
        print("年龄：", self.age)
        print("性别：", self.gender)
        print("体重：", self.weight)


if __name__ == "__main__":
    person = Person("李四", 20, "男", 70)
    person.show_info()
    person.work("木头")
    person.work("石头")
    person.learn_language(["中文", "英语", "日语"])
