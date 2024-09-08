'''【练习】字符串综合实战
我的答案：

作业要求
编写一个Python程序，对一个简单的故事进行如下操作：

统计故事中的单词数量。
查找主人公的名字在故事中的位置。
将主人公的名字替换为你的名字。
将故事改写为大写和小写形式。
解题思路
使用字符串的方法来处理数据。
'''
story = "Once upon a time, in a land far away, lived a brave knight named Arthur."
# 去除多余的空白字符并分割成单词列表
words = story.split()

# 计算分割后的单词列表的长度，即单词的数量。
word_count = len(words)

# 输出结果
print(f"故事中的单词总数为: {word_count}")

# -----------------------------------
# 查找主人公的名字在故事中的位置。
print("主人公的名字在故事中的位置:",story.index("Arthur"))
# -----------------------------------
# 将主人公的名字替换为你的名字。
print(story.replace("Arthur", "QIN"))
# -----------------------------------
# 将故事改写为大写形式。
print(story.lower())
# 将故事改写为大写形式。
print(story.upper())
