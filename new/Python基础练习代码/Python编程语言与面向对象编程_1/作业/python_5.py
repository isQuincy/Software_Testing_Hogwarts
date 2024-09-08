'''【练习】数据统计
作业要求
列表中保存若干个数字，计算数字的和，最小值，最大值，平均数
解题思路
1. 定义一个函数func1()，在该函数中进行操作。
2. 初始化变量n_sum为0，用于累计求和。
3. 初始化变量n_max和n_min为None，用于保存最大值和最小值。
4. 创建一个列表data，其中保存了要处理的数字数据。
5. 使用while循环遍历列表data中的每个元素，通过遍历获取每个数字。
6. 在循环内部，依次进行以下操作：
7. 循环结束后，得到数字的和、最大值和最小值。
8. 打印输出数字的和、最大值和最小值。
9. 计算平均数
10. 在代码的其他地方调用函数func1()来执行，并获取结果。
'''

def func1():
    n_sum=0
    n_max=None
    n_min=None
    data = [10, 20, 30, 40, 50]  # 示例列表
    index = 0  # 初始化索引

    while index < len(data):
        element = data[index]
        n_sum += element
        index += 1  # 递增索引
    print("当前元素的和",n_sum)  # 打印当前元素的和
    n_max = max(data)# 最大值
    n_min = min(data) # 最小值
    print("最大值",n_max)
    print("最小值",n_min)
    print("平均值",element/len(data)) # 平均数

func1()