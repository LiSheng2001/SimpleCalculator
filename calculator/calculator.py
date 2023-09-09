import re
from typing import List, Union


class Calculator:
    # 将字符串切分为token
    token_splitter = re.compile(r'(\d+\.\d+|\d+|[-+*/()\^%])')
    # 运算符优先级
    priority = {"(": 0, "+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 2}
    # 判断是否右结合
    right_associate = set(["^"])

    @classmethod
    def convert_to_postfix(cls, expression: str) -> List[Union[str, float]]:
        """将中缀表达式转为逆波兰表示"""
        tokens = cls.token_splitter.findall(expression)

        # 符号栈和输出队列
        op_stack, output_queue = [], []

        for token in tokens:
            if token in "+-*/^%":
                if token in cls.right_associate:
                    # 右结合的算符，区别就是右结合的算符同优先级要从右往左算
                    while len(op_stack) > 0 and cls.priority[op_stack[-1]] > cls.priority[token]:
                        output_queue.append(op_stack.pop())
                else:
                    # 左结合的算符
                    while len(op_stack) > 0 and cls.priority[op_stack[-1]] >= cls.priority[token]:
                        output_queue.append(op_stack.pop())
                op_stack.append(token)
            elif token == "(":
                op_stack.append("(")
            elif token == ")":
                while len(op_stack) > 0 and op_stack[-1] != "(":
                    output_queue.append(op_stack.pop())
                if len(op_stack) == 0:
                    raise Exception("括号不匹配!")
                else:
                    # 去除右括号
                    op_stack.pop()
            else:
                # 操作数
                output_queue.append(float(token))
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
