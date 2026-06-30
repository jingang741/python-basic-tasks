"""员工数据统计报表：读取 data/employees.csv，直接运行即可。"""
import csv
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "employees.csv"

MOBILE = {"134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "157", "158", "159", "172", "178", "182", "183", "184", "187", "188", "195", "197", "198"}
UNICOM = {"130", "131", "132", "145", "155", "156", "166", "175", "176", "185", "186", "196"}
TELECOM = {"133", "149", "153", "173", "177", "180", "181", "189", "190", "191", "193", "199"}
RISK_AREAS = ["黑龙江", "北京", "福建", "四川"]


def phone_operator(phone):
    prefix = str(phone)[:3]
    if prefix in MOBILE:
        return "移动"
    if prefix in UNICOM:
        return "联通"
    if prefix in TELECOM:
        return "电信"
    return "其他"


def load_rows():
    with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def main():
    rows = load_rows()
    total = len(rows)

    operators = {"电信": 0, "联通": 0, "移动": 0, "其他": 0}
    genders = {}
    older_than_45 = 0
    high_salary = 0
    low_salary = 0
    media_company = 0
    risk_people = 0

    for row in rows:
        operators[phone_operator(row["电话号码"])] += 1
        gender = row["性别"]
        genders[gender] = genders.get(gender, 0) + 1

        age = int(float(row["年龄"]))
        salary = float(row["薪资"])
        address = row["居住地址"]
        company = row["外包公司"]

        if age > 45:
            older_than_45 += 1
        if salary > 8000:
            high_salary += 1
        if salary < 3000:
            low_salary += 1
        if "传媒" in company:
            media_company += 1
        if any(area in address for area in RISK_AREAS):
            risk_people += 1

    print("========== 员工数据统计报表 ==========")
    print("统计表格中有多少人：", total)
    print("\n三大运营商数量和占比：")
    for name in ["电信", "联通", "移动", "其他"]:
        count = operators[name]
        print(f"{name}：{count} 人，占比 {count / total:.2%}")
    print("\n总公司男女人数：")
    for gender, count in genders.items():
        print(f"{gender}：{count} 人")
    print("\n年龄超过45岁的老员工人数：", older_than_45)
    print("薪资高于8000元的高薪人员数量：", high_salary)
    print("薪资低于3000元的低薪人员数量：", low_salary)
    print("去传媒公司工作的人员数量：", media_company)
    print("可能在疫情高危地区的人数：", risk_people)


if __name__ == "__main__":
    main()
