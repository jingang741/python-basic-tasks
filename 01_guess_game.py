"""猜数字游戏：金币版。"""
import random


def play():
    money = 5000
    print("猜数字游戏开始：初始金币 5000，每猜错一次扣 500，猜对奖励 3000。")

    while money >= 500:
        answer = random.randint(1, 100)
        print("\n新一轮开始，请猜 1~100 之间的数字。")

        while money >= 500:
            try:
                guess = int(input("请输入数字："))
            except ValueError:
                print("请输入正确的整数。")
                continue

            if guess > answer:
                money -= 500
                print(f"大了，扣 500 金币，当前余额：{money}")
            elif guess < answer:
                money -= 500
                print(f"小了，扣 500 金币，当前余额：{money}")
            else:
                money += 3000
                print(f"恭喜猜中，本轮幸运数字：{answer}，奖励 3000，当前余额：{money}")
                break

        if money < 500:
            print("余额不足 500，游戏结束。")
            break

        again = input("是否继续下一轮？输入 y 继续，其他退出：")
        if again.lower() != "y":
            break

    print(f"游戏结束，最终金币：{money}")


if __name__ == "__main__":
    play()
