import random

num = random.randint(1, 100)

while True:
    guess = int(input("请输入你猜的数字："))

    if guess > num:
        print("大了")
    elif guess < num:
        print("小了")
    else:
        print("恭喜猜中，本轮幸运数字：", num)
        break
