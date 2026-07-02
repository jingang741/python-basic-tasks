# 字典练习题

print("========== 字典基础 ==========")

# 假设有一个字典 person_info 储存了一个人的信息，包含不少于5个键值对。
person_info = {
    "name": "Alex",
    "age": 30,
    "country": "USA",
    "language": ["English", "Spanish"],
    "is_student": False
}
print("初始字典：", person_info)

# 1. 打印 person_info 字典的 name 值。
print("1：name =", person_info["name"])

# 2. 修改 age 的值为 31。
person_info["age"] = 31
print("2：", person_info)

# 3. 向字典中添加一个新的键值对 height: 175。
person_info["height"] = 175
print("3：", person_info)

# 4. 删除字典中的 is_student 键及其值。
person_info.pop("is_student")
print("4：", person_info)

# 5. 使用循环遍历字典，打印所有的键和值。
print("5：遍历字典")
for key, value in person_info.items():
    print(key, value)

# 6. 检查字典中是否有 email 这个键，如果没有，添加 email: alex@example.com。
if "email" not in person_info:
    person_info["email"] = "alex@example.com"
print("6：", person_info)

# 7. 将 language 的值改为只包含 English。
person_info["language"] = ["English"]
print("7：", person_info)

# 8. 获取并打印字典中 language 列表的长度。
print("8：language长度 =", len(person_info["language"]))

# 9. 向 language 列表中添加一种新语言 French。
person_info["language"].append("French")
print("9：", person_info)

# 10. 循环插入新的键值对到字典：将 hobby + 数字作为键，相应的 hobby + 数字值作为值，数字从1至3。
for i in range(1, 4):
    person_info["hobby" + str(i)] = "hobby" + str(i)
print("10：", person_info)


print("\n========== 字典进阶 ==========")

# 给定员工信息字典 employees。
employees = {
    101: {
        "name": "Alice",
        "age": 30,
        "gender": "Female",
        "position": "Data Scientist",
        "team": "Research",
        "salary_history": [70000, 80000, 90000]
    },
    102: {
        "name": "Bob",
        "age": 24,
        "gender": "Male",
        "position": "Developer",
        "team": "Tech",
        "salary_history": [60000, 65000]
    }
}
print("初始员工信息：", employees)

# 1. 新增一个员工的信息到 employees 字典中。
employees[103] = {
    "name": "Cindy",
    "age": 28,
    "gender": "Female",
    "position": "Tester",
    "team": "QA",
    "salary_history": [50000, 55000]
}
print("1：", employees)

# 2. 删除一个指定的员工的信息。
employees.pop(102)
print("2：", employees)

# 3. 更新员工101的年龄至31。
employees[101]["age"] = 31
print("3：", employees[101])

# 4. 增加员工101薪资历史中的最新薪资至95000。
employees[101]["salary_history"].append(95000)
print("4：", employees[101]["salary_history"])

# 5. 计算员工101的平均薪资。
avg_salary = sum(employees[101]["salary_history"]) / len(employees[101]["salary_history"])
print("5：员工101平均薪资 =", avg_salary)

# 6. 找出所有年龄大于25岁的员工的姓名和ID。
print("6：年龄大于25岁的员工")
for emp_id, info in employees.items():
    if info["age"] > 25:
        print(emp_id, info["name"])

# 7. 对 employees 中的每个员工，添加 bonus 键，其中值是最新薪资的10%。
for emp_id, info in employees.items():
    info["bonus"] = info["salary_history"][-1] * 0.1
print("7：", employees)

# 8. 将员工101的职位更新为 Senior Data Scientist。
employees[101]["position"] = "Senior Data Scientist"
print("8：", employees[101])

# 9. 从员工的信息中移除 gender 键。
for info in employees.values():
    info.pop("gender", None)
print("9：", employees)

# 10. 创建一个新的嵌套字典，该字典仅包含员工的 name 和 position。
simple_employees = {}
for emp_id, info in employees.items():
    simple_employees[emp_id] = {
        "name": info["name"],
        "position": info["position"]
    }
print("10：", simple_employees)
