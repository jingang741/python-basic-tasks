# 超市购物系统 V1.0
# 要求：账户有钱、购物车、买商品、退出时打印购物小条

money = 1000
products = ["苹果", "香蕉", "牛奶", "面包", "方便面"]
prices = [5, 3, 8, 6, 4]
cart = []

while True:
    print("\n商品列表：")
    for i in range(len(products)):
        print(i, products[i], prices[i], "元")

    name = input("请输入要购买的商品名，输入 q 退出：")

    if name == "q" or name == "Q":
        print("\n====== 购物小条 ======")
        total = 0
        for item in cart:
            print(item[0], item[1], "元")
            total += item[1]
        print("消费总额：", total, "元")
        print("卡余额：", money, "元")
        print("====================")
        break

    if name in products:
        index = products.index(name)
        price = prices[index]
        if money >= price:
            cart.append([name, price])
            money -= price
            print("恭喜，购买成功！您的卡余额还剩", money)
        else:
            print("穷鬼，钱不够！请到其他超市购买！")
    else:
        print("没有这个商品，别瞎弄！")
