# 字符串练习题

print("========== 字符串基础 ==========")

# 假设有一个初始字符串 s = "Hello, Python world!"
s = "Hello, Python world!"
print("初始字符串：", s)

# 1. 字符串长度计算。
print("1：长度 =", len(s))

# 2. 计算字符串中 o 字符的个数。
print("2：o的个数 =", s.count("o"))

# 3. 将字符串转换为大写。
print("3：", s.upper())

# 4. 将字符串转换为小写。
print("4：", s.lower())

# 5. 查找 Python 在字符串中的位置。
print("5：Python位置 =", s.find("Python"))

# 6. 替换字符串中的 world 为 universe。
print("6：", s.replace("world", "universe"))

# 7. 检查字符串是否以 Hello 开始。
print("7：", s.startswith("Hello"))

# 8. 检查字符串是否以 ! 结尾。
print("8：", s.endswith("!"))

# 9. 以 , 为分隔符，拆分字符串。
print("9：", s.split(","))

# 10. 去除字符串首尾的 !。
print("10：", s.strip("!"))

# 11. 字符串反转。
print("11：", s[::-1])

# 12. 字符串切片，获取 Python。
print("12：", s[7:13])

# 13. 将字符串 s 中的 Hello, 删除。
print("13：", s.replace("Hello,", ""))

# 14. 拼接两个字符串 Hello, 和 World!。
print("14：", "Hello," + "World!")

# 15. 使用 f-string 合并字符串和数字 2021。
print(f"15：年份是{2021}")

# 16. 找出 a 第一次出现的位置。
print("16：a第一次出现的位置 =", s.find("a"))

# 17. 找出 e 最后一次出现的位置。
print("17：e最后一次出现的位置 =", s.rfind("e"))

# 18. 计算字符串中空格的数量。
print("18：空格数量 =", s.count(" "))

# 19. 使用循环遍历字符串中的每个字符。
print("19：遍历字符串")
for ch in s:
    print(ch)

# 20. 将字符串转为列表形式，每个字符为一个列表元素。
char_list = list(s)
print("20：", char_list)

# 21. 字符串排序，先转换为列表。
print("21：", sorted(char_list))

# 22. 判断字符串是否为数字。
print("22：", s.isdigit())

# 23. 将列表 ['Hello,', 'Python', 'World!'] 使用空格连接为一个字符串。
print("23：", " ".join(['Hello,', 'Python', 'World!']))

# 24. 使用 % 操作符格式化字符串，将数字 100 插入到 Number: 后面。
print("24：Number: %d" % 100)

# 25. 检查字符串是否全部为小写字母。
print("25：", s.islower())

# 26. 检查字符串是否全部为大写字母。
print("26：", s.isupper())

# 27. 将数字列表 [1, 2, 3] 转换成字符串，元素之间用 - 连接。
print("27：", "-".join([str(x) for x in [1, 2, 3]]))

# 28. 找出字符串中所有的 o 的位置。
print("28：", [i for i in range(len(s)) if s[i] == "o"])

# 29. 替换字符串中的第一个 o 为 O。
print("29：", s.replace("o", "O", 1))

# 30. 字符串插入操作，向字符串指定位置插入子字符串 amazing。
print("30：", s[:7] + "amazing " + s[7:])


print("\n========== 字符串进阶 ==========")

# 给定字符串 s = "Python is great!"
s = "Python is great!"
print("初始字符串：", s)

# 1. 字符串反转：不使用任何内置函数，编写代码以反转字符串。
result = ""
for ch in s:
    result = ch + result
print("1：", result)

# 2. 字符计数：计算字符 t 在其中出现的次数。
count = 0
for ch in s:
    if ch == "t":
        count += 1
print("2：t出现次数 =", count)

# 3. 替换字符：把字符串 s 中的所有空格替换成下划线。
print("3：", s.replace(" ", "_"))

# 4. 检查回文：检查 s2 在忽略大小写、标点和空格的情况下是否为回文字符串。
s2 = "A man, a plan, a canal, Panama!"
clean = ""
for ch in s2.lower():
    if ch.isalnum():
        clean += ch
print("4：", clean == clean[::-1])

# 5. 子字符串查找：在 s 中查找第一次出现子字符串 is 的位置。
print("5：is位置 =", s.find("is"))

# 6. 字符串插入：在 s 中第一个 t 字符之后插入子字符串 _inserted。
index = s.find("t")
print("6：", s[:index + 1] + "_inserted" + s[index + 1:])

# 7. 部分替换：替换 s 中第一次出现的 great 为 awesome。
print("7：", s.replace("great", "awesome", 1))

# 8. 切片与拼接：将 s 切分为两部分，再将这两部分以相反顺序拼接起来。
mid = len(s) // 2
print("8：", s[mid:] + s[:mid])

# 9. 创建字符串列表：使用列表生成式，根据字符串 s 创建一个列表，其中包含 s 的每个单词的首字母大写形式。
print("9：", [word.capitalize() for word in s.split()])

# 10. 字符替换加密：编写一个函数 encrypt，使用字典 a:m, b:n ... z:l 的规则加密 s3 = encryption。
def encrypt(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    code = "mnopqrstuvwxyzabcdefghijkl"
    rule = {}

    for i in range(len(letters)):
        rule[letters[i]] = code[i]

    new_text = ""
    for ch in text:
        new_text += rule.get(ch, ch)
    return new_text

s3 = "encryption"
print("10：", encrypt(s3))
