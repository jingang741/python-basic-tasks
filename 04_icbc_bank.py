"""中国工商银行账户管理系统。"""
import random
from dataclasses import dataclass


@dataclass
class Address:
    country: str
    province: str
    street: str
    number: str


@dataclass
class User:
    account: str
    name: str
    password: int
    address: Address
    balance: int
    bank_name: str


class Bank:
    def __init__(self, name):
        self.name = name
        self.users = {}
        self.max_users = 100

    def new_account(self):
        while True:
            account = "".join(str(random.randint(0, 9)) for _ in range(8))
            if account not in self.users:
                return account

    def add_user(self, user):
        if len(self.users) >= self.max_users:
            return 3
        if user.account in self.users:
            return 2
        self.users[user.account] = user
        return 1

    def save_money(self, account, money):
        user = self.users.get(account)
        if not user:
            return False
        user.balance += money
        return True

    def get_money(self, account, password, money):
        user = self.users.get(account)
        if not user:
            return 1
        if user.password != password:
            return 2
        if user.balance < money:
            return 3
        user.balance -= money
        return 0

    def transfer(self, out_account, in_account, password, money):
        out_user = self.users.get(out_account)
        in_user = self.users.get(in_account)
        if not out_user or not in_user:
            return 1
        if out_user.password != password:
            return 2
        if out_user.balance < money:
            return 3
        out_user.balance -= money
        in_user.balance += money
        return 0

    def query(self, account, password):
        user = self.users.get(account)
        if not user:
            print("该用户不存在。")
            return
        if user.password != password:
            print("密码错误。")
            return
        print(f"当前账号：{user.account}，姓名：{user.name}，密码：{user.password}，余额：{user.balance} 元")
        print(f"用户地址：{user.address.country}{user.address.province}{user.address.street}{user.address.number}")
        print(f"开户行：{user.bank_name}")


def open_user(bank):
    account = bank.new_account()
    name = input("姓名：")
    password = int(input("6位密码："))
    balance = int(input("初始存款："))
    address = Address(input("国家："), input("省份："), input("街道："), input("门牌号："))
    user = User(account, name, password, address, balance, bank.name)
    result = bank.add_user(user)
    print("开户成功，账号：" + account if result == 1 else "开户失败，代码：" + str(result))


def main():
    bank = Bank("中国工商银行昌平支行")
    while True:
        print("\n1. 开户  2. 存钱  3. 取钱  4. 转账  5. 查询  0. 退出")
        choice = input("请选择：")
        if choice == "0":
            break
        if choice == "1":
            open_user(bank)
        elif choice == "2":
            ok = bank.save_money(input("账号："), int(input("金额：")))
            print("存钱成功" if ok else "账号不存在")
        elif choice == "3":
            code = bank.get_money(input("账号："), int(input("密码：")), int(input("金额：")))
            print({0: "取钱成功", 1: "账号不存在", 2: "密码不对", 3: "钱不够"}[code])
        elif choice == "4":
            code = bank.transfer(input("转出账号："), input("转入账号："), int(input("密码：")), int(input("金额：")))
            print({0: "转账成功", 1: "账号不对", 2: "密码不对", 3: "钱不够"}[code])
        elif choice == "5":
            bank.query(input("账号："), int(input("密码：")))
        else:
            print("选择错误。")


if __name__ == "__main__":
    main()
