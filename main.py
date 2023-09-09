# 入口文件
from calculator import Calculator

if __name__ == "__main__":
    print(f"输入字符串表达式计算结果，输入\\exit则为退出")
    while 1:
        expression = input("请输入表达式: ")

        if expression == "\\exit":
            print(f"Bye~")
            exit()
        
        result = Calculator.calculate(expression)
        print(f"{expression}={result}")
        