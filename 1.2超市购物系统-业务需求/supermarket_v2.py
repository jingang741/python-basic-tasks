# 超市购物系统 V2.0
# 新增：随机优惠券、优化小票、退货功能

import random
import datetime

money = 10000
products = ["苹果", "香蕉", "牛奶", "面包", "方便面", "空调", "手机", "电脑", "水杯", "书包"]
prices = [5, 3, 8, 6, 4, 3000, 2500, 5000, 20, 80]
cart = []

coupon_product = random.choice(products)
print("你抽到的优惠券是：", coupon_product, "8折")

while True:
    print("\n商品列表：")
    for i in range(len(products)):
        print(i, products[i], prices[i], "元")

    print("\n输入商品名购买，输入 r 退货，输入 q 退出")
    name = input("请输入：")

    if name == "q" or name == "Q":
        print("\n========== 购物小条 ==========")
        print("购物时间：", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        total = 0
        for item in cart:
            print(item[0], "原价：", item[1], "实付：", item[2])
            total += item[2]
        print("购物数量：", len(cart))
        print("购买总价值：", total, "元")
        print("卡余额：", money, "元")
        print("============================")
        break

    if name == "r" or name == "R":
        if len(cart) == 0:
            print("购物车为空，不能退货")
            continue

        print("购物车：")
        for i in range(len(cart)):
            print(i, cart[i][0], "实付：", cart[i][2])

        index = int(input("请输入要退货的编号："))
        if 0 <= index < len(cart):
            item = cart.pop(index)
            money += item[2]
            print("退货成功：", item[0], "退回金额：", item[2], "当前余额：", money)
        else:
            print("编号错误")
        continue

    if name in products:
        index = products.index(name)
        price = prices[index]

        if name == coupon_product:
            real_price = price * 0.8
        else:
            real_price = price

        if money >= real_price:
            cart.append([name, price, real_price])
            money -= real_price
            print("购买成功！您的卡余额还剩", money)
        else:
            print("穷鬼，钱不够！请到其他超市购买！")
    else:
        print("没有这个商品，别瞎弄！")
