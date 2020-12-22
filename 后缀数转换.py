# 运算规则，先乘除，后加减.
ops_rule = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}
def middle_to_after(s):
    """
    中缀表达式转化后缀表达式.
    :param s: 中缀表达式的字符串表示，本程序中采用操作符跟数值之间用空格分开，例如:
    "9 + ( 3 - 1 ) * 3 + 10 / 2"
    :return: 后缀表达式，数组的形式，每个数值或者操作符占一个数组下标.
    """
    expression = []
    ops = []
    ss = s.split(' ')
    for item in ss:
        if item in ['+', '-', '*', '/']:   # 操作符
            while len(ops) >= 0:
                if len(ops) == 0:
                    ops.append(item)
                    break
                op = ops.pop()
                if op == '(' or ops_rule[item] > ops_rule[op]:
                    ops.append(op)
                    ops.append(item)
                    break
                else:
                    expression.append(op)
        elif item == '(':  # 左括号，直接入操作符栈
            ops.append(item)
        elif item == ')':  # 右括号，循环出栈道
            while len(ops) > 0:
                op = ops.pop()
                if op == '(':
                    break
                else:
                    expression.append(op)
        else:
            expression.append(item)   # 数值，直接入表达式栈
    while len(ops) > 0:
        expression.append(ops.pop())
    return expression
    
print (middle_to_after(" a * ( b - c * d ) + e - f / g * ( h + i * j - k ) "))
