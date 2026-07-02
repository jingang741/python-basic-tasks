# 列表操作练习题

import random

print("========== 列表练习题-初始 ==========")

# 1. 创建一个列表 list1，其包含元素 1, 2, 3, 4, 5。
list1 = [1, 2, 3, 4, 5]
print("1：", list1)

# 2. 向 list1 添加一个元素 6。
list1.append(6)
print("2：", list1)

# 3. 从 list1 中删除元素 3。
list1.remove(3)
print("3：", list1)

# 4. 修改 list1 中的第二个元素值为 8。
list1[1] = 8
print("4：", list1)

# 5. 找出 list1 中值为 8 的元素索引。
print("5：8的索引是", list1.index(8))

# 6. 遍历 list1，打印每个元素的值。
print("6：遍历list1")
for x in list1:
    print(x)

# 7. 利用循环，将一个新列表 [7, 8, 9] 的每个元素添加到 list1 的末尾。
for x in [7, 8, 9]:
    list1.append(x)
print("7：", list1)

# 8. 使用一个命令，将列表 [10, 11, 12] 添加到 list1 的末尾。
list1.extend([10, 11, 12])
print("8：", list1)

# 9. 使用切片操作，获取 list1 第三个元素到第五个元素（包含第五个元素）。
print("9：", list1[2:5])

# 10. 将 list1 的第三个元素修改为两个新元素 [13, 14]。
list1[2:3] = [13, 14]
print("10：", list1)


print("\n========== 列表练习题-进阶 ==========")

# 给定初始列表 my_list。
my_list = [3, "apple", 9, "banana", 7, "cherry", 2, "date", 5, "elderberry"]
print("初始列表：", my_list)

# 1. 向 my_list 中添加一个元素 "fig"。
my_list.append("fig")
print("1：", my_list)

# 2. 从 my_list 中删除元素 "banana"。
my_list.remove("banana")
print("2：", my_list)

# 3. 将元素 7 修改为字符串 "grape"。
my_list[my_list.index(7)] = "grape"
print("3：", my_list)

# 4. 查找并打印元素 "cherry" 的索引值。
print("4：cherry的索引是", my_list.index("cherry"))

# 5. 遍历 my_list 并打印每个元素。
print("5：遍历my_list")
for x in my_list:
    print(x)

# 6. 在 "cherry" 后面插入新元素 "kiwi"。
my_list.insert(my_list.index("cherry") + 1, "kiwi")
print("6：", my_list)

# 7. 使用索引查找并打印第三个元素。
print("7：第三个元素是", my_list[2])

# 8. 使用负数索引找到并打印倒数第二个元素。
print("8：倒数第二个元素是", my_list[-2])

# 9. 使用切片操作获取第三个至第七个元素并打印结果。
print("9：", my_list[2:7])

# 10. 使用切片操作反转整个列表并打印结果。
print("10：", my_list[::-1])

# 11. 对列表中的字符串进行排序，并保留数字在原位。
strings = sorted([x for x in my_list if isinstance(x, str)])
new_list = []
index = 0
for x in my_list:
    if isinstance(x, str):
        new_list.append(strings[index])
        index += 1
    else:
        new_list.append(x)
print("11：", new_list)

# 12. 将 my_list 中的数字替换为它们对应的字符串形式，不改变列表中原有的字符串。
num_to_word = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine"
}
my_list = [num_to_word.get(x, x) if isinstance(x, int) else x for x in my_list]
print("12：", my_list)


print("\n========== 列表练习题-复杂 ==========")

# 1. 创建一个列表包含从 1 到 100 的所有偶数。
nums = list(range(2, 101, 2))
print("1：", nums)

# 2. 将上述列表中所有偶数替换为它们的平方。
nums = [x * x for x in nums]
print("2：", nums)

# 3. 从上述列表中删除所有大于 1000 的数字。
nums = [x for x in nums if x <= 1000]
print("3：", nums)

# 4. 将列表逆序。
nums.reverse()
print("4：", nums)

# 5. 使用切片操作取出列表中的前 10 个元素。
print("5：", nums[:10])

# 6. 将一个新列表 [101, 102, 103] 加到现有列表的末尾。
nums.extend([101, 102, 103])
print("6：", nums)

# 7. 计算列表中元素的平均值。
print("7：平均值是", sum(nums) / len(nums))

# 8. 找到列表中的最大值和最小值。
print("8：最大值是", max(nums), "最小值是", min(nums))

# 9. 找出列表中第一次出现的 11 的索引位置。
if 11 in nums:
    print("9：11的索引是", nums.index(11))
else:
    print("9：没有11，返回 -1")

# 10. 用循环遍历列表，把每个数字替换为其对应的字符形式。
str_nums = []
for x in nums:
    str_nums.append(str(x))
print("10：", str_nums)

# 11. 将列表中的所有元素转换成浮点数形式。
float_nums = [float(x) for x in str_nums]
print("11：", float_nums)

# 12. 找出列表中所有大于 50 的元素个数。
count = len([x for x in float_nums if x > 50])
print("12：大于50的数量是", count)

# 13. 在列表的第 3 个位置插入数字 99。
float_nums.insert(2, 99)
print("13：", float_nums)

# 14. 删除列表中的最后一个元素。
float_nums.pop()
print("14：", float_nums)

# 15. 使用列表推导式创建一个新列表，包含原列表中每个数字乘以 2 的结果。
double_nums = [x * 2 for x in float_nums]
print("15：", double_nums)

# 16. 将列表分成两部分，一部分是小于等于 50 的数，另一部分是大于 50 的数。
small = [x for x in float_nums if x <= 50]
big = [x for x in float_nums if x > 50]
print("16：小于等于50：", small)
print("16：大于50：", big)

# 17. 将列表转换为一个字典，其中列表元素作为键，其在列表中的索引作为值。
num_dict = {float_nums[i]: i for i in range(len(float_nums))}
print("17：", num_dict)

# 18. 使用 enumerate 函数遍历列表，并打印元素及其索引。
print("18：")
for i, x in enumerate(float_nums):
    print(i, x)

# 19. 从列表中随机取出一个元素。
print("19：随机元素是", random.choice(float_nums))

# 20. 将列表保存到一个 txt 文件里，每个元素占一行。
with open("list_result.txt", "w", encoding="utf-8") as f:
    for x in float_nums:
        f.write(str(x) + "\n")
print("20：已保存到 list_result.txt")
