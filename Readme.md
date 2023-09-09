一个python实现的字符串简易计算器，支持四则运算、次方(^)、阶乘(!)和使用括号区分优先级的操作。

实现方法是先通过调度场算法将输入的中缀表达式转换为后缀表达式，之后再依次计算后缀表达式的值。

为了提高方法的可靠性，将通过python的unittest模块测试计算结果的正确性。


要运行demo，在根目录执行命令:
```bash
python main.py
```

要运行测试，在根目录执行命令:
```bash
python -m unittest
```

目前还不支持的特性: 
1. 将"-"作为单目运算符，比如输入"-2"会被认为非法输入。
2. 目前还未支持"!"，打算解决特性1之后一并引入。
3. 对错误输入的检测还不完善，比如除0等检测还没有很完善。