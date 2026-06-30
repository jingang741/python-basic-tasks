"""方法练习题。"""
from collections import Counter


def sum4(a, b, c, d):
    return a + b + c + d


def list_sum(nums):
    return sum(nums)


def print_99():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}x{i}={i*j}", end="\t")
        print()


def get_by_index(items, index):
    return items[index] if 0 <= index < len(items) else -1


def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)


def department_stats():
    test = ['小明', '小张', '小黄', '小杨']
    develop = ['小黄', '小李', '小王', '小杨', '小周']
    market = ['小杨', '小张', '小吴', '小冯', '小周']
    all_people = test + develop + market
    counter = Counter(all_people)
    only_one = [name for name, count in counter.items() if count == 1]
    two_or_more = [name for name, count in counter.items() if count >= 2]
    return len(counter), only_one, two_or_more


def reverse_multiplication(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(f"{j}x{i}={i*j}", end="\t")
        print()


def main():
    nums = [int(input(f"请输入第 {i} 个数字：")) for i in range(1, 5)]
    print("4个数的和：", sum4(*nums))
    print("列表 [1,2,3,4,5] 的和：", list_sum([1, 2, 3, 4, 5]))
    print("取列表 [10,45,82,32] 下标 2：", get_by_index([10, 45, 82, 32], 2))
    print("1~300 的递归和：", recursive_sum(300))
    total, only_one, two_or_more = department_stats()
    print("部门员工总人数：", total)
    print("只在一个部门的人：", only_one)
    print("在两个部门及以上的人：", two_or_more)
    print("99乘法表：")
    print_99()
    print("5x5倒序乘法表：")
    reverse_multiplication(5)


if __name__ == "__main__":
    main()
