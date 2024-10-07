一个python实现的字符串简易计算器，支持四则运算、次方(^)、阶乘(!)和使用括号区分优先级的操作。

实现方法是先通过调度场算法将输入的中缀表达式转换为后缀表达式，之后再依次计算后缀表达式的值。

为了提高方法的可靠性，将通过python的unittest模块测试计算结果的正确性。

2024.10.07更新：
不使用正则表达式切分token了，而使用更加灵活的文法分析以更灵活地计算。
1. 支持负数输入，如"-2"、"-3"等。
2. 支持单目运算符如"!"
3. 支持有限的函数运算，如`sin`, `cos`和`tan`，主要为了演示方法，实际可以支持更多。
4. 支持有限的常数，如`pi`。


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