import random


class Address:
    """地址类：保存国家、省份、街道、门牌号。"""

    def __init__(self, country, province, street, door_number):
        self.country = country
        self.province = province
        self.street = street
        self.door_number = door_number

    def __str__(self):
        return self.country + self.province + self.street + self.door_number


class User:
    """用户类：保存账户的基本信息。"""

    def __init__(self, account, account_type, name, password, address, balance, bank_name):
        self.account = account
        self.account_type = account_type
        self.name = name
        self.password = str(password)
        self.address = address
        self.balance = balance
        self.bank_name = bank_name

    def show_info(self):
        print("当前账号：", self.account)
        print("账户类型：", self.account_type)
        print("姓名：", self.name)
        print("密码：", self.password)
        print("余额：", self.balance, "元")
        print("用户居住地址：", self.address)
        print("当前账户的开户行：", self.bank_name)


class Bank:
    """银行类：保存用户库，并提供开户、存钱、取钱、转账、查询功能。"""

    MAX_USER_COUNT = 100

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.users = {}

    def create_account(self):
        """随机生成一个不重复的8位账号。"""
        while True:
            account = str(random.randint(10000000, 99999999))
            if account not in self.users:
                return account

    def open_account(self, user):
        """
        开户。
        返回值：
        1：成功
        2：用户已存在
        3：用户库已满
        """
        if user.account in self.users:
            return 2

        if len(self.users) >= self.MAX_USER_COUNT:
            return 3

        self.users[user.account] = user
        return 1

    def save_money(self, account, money):
        """
        存钱。
        返回值：True 成功，False 账号不存在。
        """
        if account not in self.users:
            return False

        self.users[account].balance += money
        return True

    def get_money(self, account, password, money):
        """
        取钱。
        返回值：
        0：正常
        1：账号不存在
        2：密码不对
        3：余额不足
        """
        if account not in self.users:
            return 1

        user = self.users[account]

        if user.password != str(password):
            return 2

        if user.balance < money:
            return 3

        user.balance -= money
        return 0

    def transfer_money(self, out_account, in_account, password, money):
        """
        转账。
        返回值：
        0：正常
        1：账号不对
        2：密码不对
        3：余额不足
        """
        if out_account not in self.users or in_account not in self.users:
            return 1

        out_user = self.users[out_account]
        in_user = self.users[in_account]

        if out_user.password != str(password):
            return 2

        if out_user.balance < money:
            return 3

        out_user.balance -= money
        in_user.balance += money
        return 0

    def search_account(self, account, password):
        """查询账户。按照题目要求：只打印，不返回具体数据。"""
        if account not in self.users:
            print("该用户不存在。")
            return

        user = self.users[account]

        if user.password != str(password):
            print("密码错误。")
            return

        user.show_info()


class ATM:
    """ATM界面类：负责菜单和用户输入。"""

    def __init__(self, bank):
        self.bank = bank

    def show_menu(self):
        print("=" * 30)
        print("欢迎使用", self.bank.bank_name)
        print("1. 开户")
        print("2. 存钱")
        print("3. 取钱")
        print("4. 转账")
        print("5. 查询账户")
        print("0. 退出")
        print("=" * 30)

    def input_money(self, tip):
        money = int(input(tip))
        if money <= 0:
            print("金额必须大于0。")
            return None
        return money

    def input_password(self):
        while True:
            password = input("请输入6位数字密码：")
            if len(password) == 6 and password.isdigit():
                return password
            print("密码必须是6位数字，请重新输入。")

    def do_open_account(self):
        print("开始开户")
        account = self.bank.create_account()
        account_type = int(input("请输入账户类型："))
        name = input("请输入姓名：")
        password = self.input_password()

        country = input("请输入国家：")
        province = input("请输入省份：")
        street = input("请输入街道：")
        door_number = input("请输入门牌号：")
        address = Address(country, province, street, door_number)

        balance = self.input_money("请输入开户金额：")
        if balance is None:
            return

        user = User(account, account_type, name, password, address, balance, self.bank.bank_name)
        code = self.bank.open_account(user)

        if code == 1:
            print("开户成功！您的账号是：", account)
        elif code == 2:
            print("开户失败：用户已存在。")
        elif code == 3:
            print("开户失败：用户库已满。")

    def do_save_money(self):
        account = input("请输入账号：")
        money = self.input_money("请输入存款金额：")
        if money is None:
            return

        result = self.bank.save_money(account, money)
        if result:
            print("存钱成功！")
        else:
            print("存钱失败：账号不存在。")

    def do_get_money(self):
        account = input("请输入账号：")
        password = input("请输入密码：")
        money = self.input_money("请输入取款金额：")
        if money is None:
            return

        code = self.bank.get_money(account, password, money)
        if code == 0:
            print("取钱成功！")
        elif code == 1:
            print("取钱失败：账号不存在。")
        elif code == 2:
            print("取钱失败：密码不对。")
        elif code == 3:
            print("取钱失败：余额不足。")

    def do_transfer_money(self):
        out_account = input("请输入转出账号：")
        in_account = input("请输入转入账号：")
        password = input("请输入转出账号密码：")
        money = self.input_money("请输入转账金额：")
        if money is None:
            return

        code = self.bank.transfer_money(out_account, in_account, password, money)
        if code == 0:
            print("转账成功！")
        elif code == 1:
            print("转账失败：账号不对。")
        elif code == 2:
            print("转账失败：密码不对。")
        elif code == 3:
            print("转账失败：余额不足。")

    def do_search_account(self):
        account = input("请输入账号：")
        password = input("请输入密码：")
        self.bank.search_account(account, password)

    def run(self):
        while True:
            self.show_menu()
            choice = input("请输入业务编号：")

            if choice == "1":
                self.do_open_account()
            elif choice == "2":
                self.do_save_money()
            elif choice == "3":
                self.do_get_money()
            elif choice == "4":
                self.do_transfer_money()
            elif choice == "5":
                self.do_search_account()
            elif choice == "0":
                print("感谢使用，再见！")
                break
            else:
                print("输入错误，请重新选择。")


if __name__ == "__main__":
    bank = Bank("中国农业银行的昌平沙河支行")
    atm = ATM(bank)
    atm.run()
