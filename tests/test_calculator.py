import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """测试Calculator类"""
    def test_calculate(self):
        """测试Calculator类的calculate方法
        这个地方主要是测试一般性的字符串函数是否正常执行"""
        # 读取测试用例
        import csv
        testcase_list = []
        with open("tests/test_data/calculate.csv") as f:
            for row in csv.DictReader(f, skipinitialspace=True):
                testcase = {"index": int(row["index"]), "expression": row["string"], "result": float(row["result"])}
                testcase_list.append(testcase)
        
        # 对每个测试用例单独测试
        for item in testcase_list:
            with self.subTest(index=item["index"], expression=item["expression"], result=item["result"]):
                result = Calculator.calculate(item["expression"])
                self.assertEqual(result, item["result"])
