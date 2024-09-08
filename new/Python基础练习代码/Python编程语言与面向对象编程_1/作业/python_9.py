#v1.0版本【练习】计算器
#作业要求，编写一个简单的Python程序，实现一个简易的计算器。用户可以输入两个数字和一个运算符（+、-、*、/），程序将根据运算符执行相应的计算操作，并输出结果。
#解题思路，1. 提示用户输入要进行的运算操作的运算符。2. 根据输入的运算符，使用条件语句执行相应的计算操作，并将结果存储在一个变量中。3. 输出计算结果。
num1 = float(input("第一个数字"))
num2 = float(input("第二个数字"))
operator = str(input("运算符:+-*/"))
def operation():
    if operator == "+":
        result = num1 + num2;
        print("结果是",result)
    elif operator == "-":
        result = num1 - num2;
        print("结果是",result)
    elif operator == "*":
        result = num1 * num2;
        print("结果是",result)
    elif operator == "/":
        result = num1 / num2;
        print("结果是",result)
    else:
        print("运算符错误")
    return
operation()