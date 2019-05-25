'''
功能：多个参数的格式化字符串
重点：多个参数的格式化字符串、认识元组
作者：薛景
最后修改于：2019/05/24
'''

import math

r = float(input("请输入圆的半径："))

S = math.pi * r * r
C = 2 * math.pi * r

print('半径为%.2f的圆的的面积是%.2f，周长是%.2f。' % (r, S, C))
# 如果格式化字符串中有多个格式符，那么“%”之后对应的多个数据一定要用圆括号包含起来
# 这种用圆括号包含起来的数据被称为元组，比如(a, b, c)就是一个三元组