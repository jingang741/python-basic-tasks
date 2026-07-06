import sqlite3
from pathlib import Path


DB_FILE = Path(__file__).with_name("person.db")


def create_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        create table if not exists person(
            username varchar(20),
            age int,
            sex char(4),
            high double
        )
    """)

    conn.commit()
    conn.close()


def add_person(username, age, sex, high):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute(
        "insert into person(username, age, sex, high) values(?, ?, ?, ?)",
        (username, age, sex, high)
    )

    conn.commit()
    conn.close()


def show_all_person():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("select username, age, sex, high from person")
    persons = cursor.fetchall()

    print("数据库中的人员信息：")
    for person in persons:
        print(person)

    conn.close()


def main():
    create_table()

    for i in range(10):
        print(f"请输入第 {i + 1} 个人的信息")
        username = input("姓名：")
        age = int(input("年龄："))
        sex = input("性别：")
        high = float(input("身高："))

        add_person(username, age, sex, high)
        print("保存成功")

    show_all_person()


if __name__ == "__main__":
    main()
