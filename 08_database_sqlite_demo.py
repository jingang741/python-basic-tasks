"""数据库任务可运行版：使用 Python 自带 sqlite3，不需要安装 MySQL。"""
import csv
import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_FILE = BASE / "data" / "demo.db"
CSV_FILE = BASE / "data" / "user_info_2000.csv"


def connect():
    return sqlite3.connect(DB_FILE)


def create_tables():
    conn = connect()
    cur = conn.cursor()
    cur.execute("drop table if exists person")
    cur.execute("create table person(username text, age int, sex text, high int)")
    cur.execute("drop table if exists user_info")
    cur.execute("""
        create table user_info(
            id int, idcard text, username text, realname text, pwd text,
            telphone text, email text, age int, sex text, address text,
            hiredate text, sal real, job text, company text
        )
    """)
    conn.commit()
    conn.close()


def input_10_persons():
    conn = connect()
    cur = conn.cursor()
    for i in range(10):
        print(f"请输入第 {i + 1} 个人的信息")
        username = input("姓名：")
        age = int(input("年龄："))
        sex = input("性别：")
        high = int(input("身高："))
        cur.execute("insert into person values(?,?,?,?)", (username, age, sex, high))
    conn.commit()
    conn.close()
    print("10个人的信息已保存到数据库。")


def make_2000_rows_csv():
    CSV_FILE.parent.mkdir(exist_ok=True)
    headers = ["id", "idcard", "username", "realname", "pwd", "telphone", "email", "age", "sex", "address", "hiredate", "sal", "job", "company"]
    with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(1, 2001):
            writer.writerow([i, f"ID{i:06d}", f"user{i}", f"姓名{i}", "123456", "13800000000", f"user{i}@baidu.com", 20 + i % 40, "男" if i % 2 else "女", "北京", "2024-01-01", 3000 + i, "开发", "百度"])
    print("已生成 2000 行 CSV：", CSV_FILE)


def batch_insert_user_info():
    conn = connect()
    cur = conn.cursor()
    with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    data = [tuple(row.values()) for row in rows]
    cur.executemany("insert into user_info values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
    conn.commit()
    conn.close()
    print("2000行数据已批量写入数据库。")


def show_counts():
    conn = connect()
    cur = conn.cursor()
    for table in ["person", "user_info"]:
        cur.execute(f"select count(*) from {table}")
        print(table, "表数据量：", cur.fetchone()[0])
    conn.close()


def main():
    create_tables()
    make_2000_rows_csv()
    batch_insert_user_info()
    show_counts()
    print("如需录入10个人，请在代码最后手动调用 input_10_persons()。")


if __name__ == "__main__":
    main()
