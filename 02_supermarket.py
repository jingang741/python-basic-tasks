"""超市购物系统：购物、优惠券、退货、小票。"""
import random
from datetime import datetime

GOODS = {
    "苹果": 5,
    "牛奶": 8,
    "面包": 6,
    "空调": 3000,
    "电脑": 5000,
    "手机": 2500,
}


def print_goods():
    print("\n商品列表：")
    for name, price in GOODS.items():
        print(f"- {name}：{price} 元")


def print_receipt(cart, money):
    print("\n========== 购物小票 ==========")
    print("购物时间：", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    total = sum(item["pay"] for item in cart)
    for item in cart:
        print(f"{item['name']} 原价:{item['price']} 实付:{item['pay']:.2f}")
    print("购物数量：", len(cart))
    print(f"商品总价值：{total:.2f} 元")
    print(f"卡余额：{money:.2f} 元")
    print("==============================")


def shopping():
    money = 10000
    cart = []
    coupon_good = random.choice(list(GOODS))
    discount = 0.8
    print(f"进店成功，余额 {money} 元。你抽到优惠券：{coupon_good} 打 8 折。")

    while True:
        print_goods()
        cmd = input("输入商品名购买；输入 r 退货；输入 q 结账退出：").strip()

        if cmd.lower() == "q":
            print_receipt(cart, money)
            break

        if cmd.lower() == "r":
            if not cart:
                print("购物车为空，不能退货。")
                continue
            for i, item in enumerate(cart):
                print(f"{i}. {item['name']} 实付 {item['pay']:.2f}")
            try:
                index = int(input("输入要退货的编号："))
                item = cart.pop(index)
                money += item["pay"]
                print(f"已退货：{item['name']}，退回 {item['pay']:.2f} 元，余额 {money:.2f}")
            except (ValueError, IndexError):
                print("编号错误。")
            continue

        if cmd not in GOODS:
            print("没有这个商品，别瞎弄！")
            continue

        price = GOODS[cmd]
        pay = price * discount if cmd == coupon_good else price
        if money < pay:
            print("穷鬼，钱不够！请到其他超市购买！")
            continue

        money -= pay
        cart.append({"name": cmd, "price": price, "pay": pay})
        print(f"购买成功：{cmd}，实付 {pay:.2f} 元，余额 {money:.2f} 元。")


if __name__ == "__main__":
    shopping()
