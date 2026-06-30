import random

money = 5000
num = random.randint(1, 100)

print("猜数字游戏开始，初始金币：", money)

while money >= 500:
    guess = int(input("请输入你猜的数字："))

    if guess > num:
        money -= 500
        print("大了，扣500金币，剩余金币：", money)
    elif guess < num:
        money -= 500
        print("小了，扣500金币，剩余金币：", money)
    else:
        money += 3000
        print("恭喜猜中，本轮幸运数字：", num)
        print("奖励3000金币，当前金币：", money)
        break

if money < 500:
    print("本金余额不足，游戏退出。")
