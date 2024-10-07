import re
from typing import List, Union
import math


class Calculator:
    # 运算符优先级
    priority = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 2, "!": 3, "#": 1}
    # 判断是否右结合
    right_associate = set(["^", "#"])
    # 函数运算符
    functions = set(["sin", "cos", "tan"])
    # 常量
    constant = {"pi": math.pi}

    @classmethod
    def isalpha(cls, c: str):
        if "a" <= c <= "z" or "A" <= c <= "Z":
            return True
        else:
            return False

    @classmethod
    def convert_to_postfix(cls, expression: str) -> List[Union[str, float]]:
        """将中缀表达式转为逆波兰表示"""
        # 符号栈和输出队列
        op_stack, output_queue = [], []
        s = expression.replace(" ", "")

        i, n = 0, len(s)
        while i < n:
            c = s[i]
            if c.isdigit():
                while i+1 < n and (s[i+1].isdigit() or s[i+1] == "."):
                    c += s[i+1]
                    i += 1
                if "." in c:
                    output_queue.append(float(c))
                else:
                    output_queue.append(int(c))
            elif c in "+-*/^%!":
                # 如果是负号，视情况单独处理成右结合的符号，用#号替代
                if c == "-" and (i==0 or s[i-1]=="("):
                    c = "#"

                if c in cls.right_associate:
                    # 右结合算符弹出大于自身优先级的算符
                    while len(op_stack) > 0 and cls.priority[op_stack[-1]] > cls.priority[c]:
                        output_queue.append(op_stack.pop())
                else:
                    # 左结合算符弹出优先级大于等于自身的算符
                    while len(op_stack) > 0 and cls.priority[op_stack[-1]] >= cls.priority[c]:
                        output_queue.append(op_stack.pop())
                # 加入自己到运算栈
                op_stack.append(c)
            elif cls.isalpha(c):
                # 获取字母
                while i+1 < n and cls.isalpha(s[i+1]):
                    c += s[i+1]
                    i += 1
                
                if c in cls.functions:
                    op_stack.append(c)
                elif c in cls.constant:
                    output_queue.append(cls.constant[c])
                else:
                    raise Exception(f"未支持的函数: {c}")
            elif c == "(":
                # 加入自身
                op_stack.append(c)
            elif c == ")":
                # 弹栈直到遇到左括号
                while len(op_stack) > 0 and op_stack[-1] != "(":
                    output_queue.append(op_stack.pop())
                
                # 检查是否遇到左括号了，没有则说明括号不匹配
                if len(op_stack) == 0:
                    raise Exception(f"存在左右括号不匹配!")
                else:
                    op_stack.pop()
                
                # 检查下一个位置是否有函数符号，如果有则弹出
                if len(op_stack) > 0 and op_stack[-1] in cls.functions:
                    output_queue.append(op_stack.pop())
            else:
                raise Exception(f"未知的操作符: {c}")
            i += 1

        # 把栈里的符号弹出到队列中
        while len(op_stack) > 0:
            output_queue.append(op_stack.pop())
        
        return output_queue
    
    @classmethod
    def calculate_postfix(cls, output_queue: List[Union[str, float]]):
        """根据后缀表达式计算结果"""
        # 数字栈
        num_stack = []

        for token in output_queue:
            if isinstance(token, (float, int)):
                # 这边属于加操作数的区域
                num_stack.append(token)
            elif token in "+-*/^%":
                # 对双目运算符都取栈里前两个数
                if len(num_stack) < 2:
                    raise Exception(f"对运算符: {token}需要两个操作数，实际只存在{len(num_stack)}个操作数!")
                a = num_stack.pop()
                b = num_stack.pop()
                # 按不同符号的算就行了
                if token == "+":
                    num_stack.append(b + a)
                elif token == "-":
                    num_stack.append(b - a)
                elif token == "*":
                    num_stack.append(b * a)
                elif token == "/":
                    num_stack.append(b / a)
                elif token == "^":
                    num_stack.append(b ** a)
                elif token == "%":
                    num_stack.append(b % a)
            elif token in ["!", "#"]:
                if len(num_stack) < 1:
                    raise Exception(f"对运算符: {token}需要两个操作数，实际只存在{len(num_stack)}个操作数!")
                b = num_stack.pop()
                if token == "!":
                    num_stack.append(math.factorial(b))
                elif token == "#":
                    num_stack.append(-1*b)
            elif token in cls.functions:
                if len(num_stack) < 1:
                    raise Exception(f"对运算符: {token}需要两个操作数，实际只存在{len(num_stack)}个操作数!")
                b = num_stack.pop()
                if token == "sin":
                    num_stack.append(math.sin(b))
                elif token == "cos":
                    num_stack.append(math.cos(b))
                elif token == "tan":
                    num_stack.append(math.tan(b))
            else:
                raise Exception(f"未知的token: {token}，如果是输入操作数请直接以int/float方式输入!")
        if len(num_stack) > 1 or len(num_stack) == 0:
            raise Exception(f"操作数和运算符数目不匹配!")
        return num_stack[-1]
    
    @classmethod
    def calculate(cls, s: str) -> float:
        """根据表达式计算结果，计算原理是先转成后缀表示/逆波兰表示后再计算结果"""
        postfix = cls.convert_to_postfix(s)
        return cls.calculate_postfix(postfix)
