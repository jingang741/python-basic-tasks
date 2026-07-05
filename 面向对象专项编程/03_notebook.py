class Notebook:
    def __init__(self, model, standby_time, color, weight, cpu, memory, disk):
        self.model = model
        self.standby_time = standby_time
        self.color = color
        self.weight = weight
        self.cpu = cpu
        self.memory = memory
        self.disk = disk

    def play_game(self, game_name):
        print(f"正在使用笔记本玩 {game_name}")

    def work(self):
        print("正在使用笔记本办公")

    def show_info(self):
        print("笔记本信息：")
        print("型号：", self.model)
        print("待机时间：", self.standby_time)
        print("颜色：", self.color)
        print("重量：", self.weight)
        print("CPU型号：", self.cpu)
        print("内存大小：", self.memory)
        print("硬盘大小：", self.disk)


if __name__ == "__main__":
    notebook = Notebook("联想小新", "8小时", "银色", "1.5kg", "i5", "16G", "512G")
    notebook.show_info()
    notebook.play_game("英雄联盟")
    notebook.work()
