"""度小满家庭记账系统：登录、记收入、记支出、管理员查看。"""
USERS = {
    "admin": {"pwd": "123456", "role": "admin"},
    "lisi": {"pwd": "123456", "role": "user"},
}

records = [
    {"user": "lisi", "type": "收入", "money": 5000, "note": "工资"},
    {"user": "lisi", "type": "支出", "money": 120, "note": "买菜"},
]


def login():
    for i in range(3):
        username = input("用户名：").strip()
        password = input("密码：").strip()
        if username in USERS and USERS[username]["pwd"] == password:
            print("登录成功。")
            return username, USERS[username]["role"]
        print(f"登录失败，还剩 {2 - i} 次机会。")
    return None, None


def show_records():
    print("\n家庭账单：")
    total = 0
    for r in records:
        sign = 1 if r["type"] == "收入" else -1
        total += sign * r["money"]
        print(f"{r['user']} {r['type']} {r['money']} 元：{r['note']}")
    print("当前结余：", total, "元")


def user_menu(username):
    while True:
        print("\n1. 记收入  2. 记支出  3. 查看账单  0. 退出")
        choice = input("请选择：")
        if choice == "0":
            break
        if choice in ("1", "2"):
            money = float(input("金额："))
            note = input("备注：")
            records.append({
                "user": username,
                "type": "收入" if choice == "1" else "支出",
                "money": money,
                "note": note,
            })
            print("记录成功。")
        elif choice == "3":
            show_records()
        else:
            print("选择错误。")


def admin_menu():
    while True:
        print("\n1. 查看所有用户  2. 打印日常理财流程  3. 查看账单  0. 退出")
        choice = input("请选择：")
        if choice == "0":
            break
        if choice == "1":
            print("用户列表：", list(USERS))
        elif choice == "2":
            print("理财流程：登录 -> 记录收入/支出 -> 查看账单 -> 分析结余。")
        elif choice == "3":
            show_records()
        else:
            print("选择错误。")


def main():
    username, role = login()
    if not username:
        print("三次登录失败，系统退出。")
        return
    admin_menu() if role == "admin" else user_menu(username)


if __name__ == "__main__":
    main()
