"""快速检查：不需要输入，验证主要代码能被 Python 正常导入和调用。"""
import importlib.util
from pathlib import Path

BASE = Path(__file__).parent


def load(name):
    path = BASE / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    methods = load("05_methods_practice.py")
    assert methods.sum4(1, 2, 3, 4) == 10
    assert methods.list_sum([1, 2, 3]) == 6
    assert methods.get_by_index([10, 45, 82, 32], 2) == 82
    assert methods.get_by_index([10, 45, 82, 32], 6) == -1
    assert methods.recursive_sum(300) == 45150

    data_report = load("07_data_report.py")
    rows = data_report.load_rows()
    assert len(rows) > 0

    db = load("08_database_sqlite_demo.py")
    db.create_tables()
    db.make_2000_rows_csv()
    db.batch_insert_user_info()

    print("全部检查通过，代码可以运行。")


if __name__ == "__main__":
    main()
