def count_string_info(s):
    """计算字符串中数字、字母、空格、其他字符的个数。"""
    digit_count = 0
    alpha_count = 0
    space_count = 0
    other_count = 0

    for ch in s:
        if ch.isdigit():
            digit_count += 1
        elif ch.isalpha():
            alpha_count += 1
        elif ch.isspace():
            space_count += 1
        else:
            other_count += 1

    return digit_count, alpha_count, space_count, other_count


def length_more_than_5(obj):
    """判断传入对象的长度是否大于5。"""
    return len(obj) > 5


def check_empty_content(obj):
    """
    检查字符串、列表、元组中是否有空内容。
    字符串：空字符串或全是空格，算空内容。
    列表/元组：元素是空字符串、None、空列表、空元组、空字典，算空内容。
    """
    if isinstance(obj, str):
        return obj.strip() == ""

    if isinstance(obj, (list, tuple)):
        for item in obj:
            if item is None:
                return True
            if item == "" or item == [] or item == () or item == {}:
                return True
        return False

    return False


def keep_first_two(li):
    """如果列表长度大于2，只保留前两个元素。"""
    if len(li) > 2:
        return li[:2]
    return li


def get_odd_index_items(obj):
    """获取列表或元组中所有奇数索引对应的元素，并作为新列表返回。"""
    result = []
    for i in range(len(obj)):
        if i % 2 == 1:
            result.append(obj[i])
    return result


if __name__ == "__main__":
    print("1. 统计字符串：")
    print(count_string_info("abc 123 !@# 中国"))

    print("2. 判断长度是否大于5：")
    print(length_more_than_5("abcdef"))
    print(length_more_than_5([1, 2, 3]))
    print(length_more_than_5((1, 2, 3, 4, 5, 6)))

    print("3. 检查是否有空内容：")
    print(check_empty_content("   "))
    print(check_empty_content([1, "", 3]))
    print(check_empty_content((1, 2, 3)))

    print("4. 只保留列表前两个元素：")
    print(keep_first_two([12, 12, 45, 78, 32, 12]))

    print("5. 获取奇数索引元素：")
    print(get_odd_index_items([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(get_odd_index_items((1, 2, 3, 11, 21, 4, 5, 6, 7)))
