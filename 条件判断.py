# 比较笨的方法，创建所有可能一个一个去试。这个在有计算机运行速度的条件下成为快速的实现方法

# 我写了两个处理方法，一种直接的 面向过程 的单次问题解决方法
# 另外一种是将类问题做成了一个类(class)，通过递归的方式进行变量可能性的创建与结果的判断


# 第一种实现是通过手动for循环，一个变量一个 for 循环
import re
l = []

# 创建所有可能性
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    l += [{'a': a, 'b': b, 'c': c, 'd': d, "e": e}]

# 一个可能一个可能进行判断
for i in l:
    if i['e'] or i['d']:
        if (i['b'] == 1 and i['c'] == 0) or (i['b'] == 0 and i['c'] == 1):
            if (i['a'] == 1 and i['b'] == 1) or (i['a'] == 0 and i['b'] == 0):
                if (i['c'] == 1 and i['d'] == 1) or (i['c'] == 0 and i['d'] == 0):
                    if (i['e'] == 1 and i['a'] == 1 and i['b'] == 1) or (i['e'] == 0 and i['a'] == 0 and i['b'] == 0):
                        print('组合:', end='')
                        [print(f'{x}-{i[x]}', '', end='') for x in i]
                        print()
# 需要说明的是：
# 上述方法对于变量多的环境很不友好，例如可能性的创建，我们需要进行多次的 for 循环来创建所有的可能性
# 对于结果的判断同样，需要多种条件的话就需要写多个 if 语句判断
# 在代码上(如果会代码的人写是没问题的但是对于普通用户(如果创建成处理问题的包给别人用)来说并不友好)


# 这是第二种，通过class进行同类问题的求解
# 下面是对整个类的注释：
# initilize是对所有可能性进行初始化的方法。中间通过num参数进行变量数量与可能性中的变量数量匹配
# 首先调用_multiPossibilities(命名的写法都是按照js的驼峰样式来的)进行递归创建所有的可能性(0-1)，保存在self.data中
# 再通过ascii编码获取从'a'字母开始计数的所有变量，保存在self.words
# 将两者按照 字母:(0-1) 的样式保存为字典，在self.dic中
# getCondition方法用于传入判断条件(字符串方式)，condition的字符串需要特殊的格式(为了下面进行格式化方便)：
#     1.变量使用a b c d等小写字母
#     2.变量前后必须有空格与其他字符分开
# getCondition传入后进行格式化，通过与_solve方法传入的可能性参数(self.dic中的一种可能性字典)名的合作，使用str.replace将变量转化为字典调用的格式
# 使用solve主方法作为判断的主入口，for循环遍历所有可能性，调用_solve进行单个可能性的递归判断。核心函数时eval()进行的字符串转语句，eval()函数可以将字符串转为语句配合if进行条件判断。
class solution:
    def __init__(self):
        self.words = []
        self.data = []
        self.condition = []
        self.dic = []
        self.results = []

    def initialize(self, num):
        self._multiPossibilities(num=num, count=num)
        for i in range(num):
            self.words += [chr(97+i)]
        for i in self.data:
            dic = {}
            for x in range(len(i)):
                dic[self.words[x]] = i[x]
            self.dic += [dic]
        return self

    def _multiPossibilities(self, num, count, l=[]):
        if count == 0:
            self.data += [l]
            l = l[:-1]
            return l
        for i in range(2):
            l += [i]
            l = self._multiPossibilities(num, count=count-1, l=l)
        return l[:-1]

    def getCondition(self, conditions):
        for i in conditions:
            con = i
            for x in self.words:
                con = con.replace(' ' +
                                  x+' ', f' poss[\'{x}\'] ')
            self.condition += [con]
        return self

    def solve(self):
        length = len(self.condition)
        for i in self.dic:
            self._solve(i, length)
        print('结果已保存至self.results')
        return self

    def _solve(self, poss, length, count=0):
        if count == length:
            self.results += [poss]
            print(f'{poss}为正解')
            return
        condition = self.condition[count]
        if eval(condition):
            self._solve(poss, length, count+1)


if __name__ == '__main__':
    so = solution()
    so.initialize(num=5)
    # print(so.dic)
    con = [
        ' e or d ',
        ' ( b == 1 and c == 0 ) or ( b == 0 and c == 1 ) ',
        ' ( a == 1 and b == 1 ) or ( a == 0 and b == 0 ) ',
        ' ( c == 1 and d == 1 ) or ( c == 0 and d == 0 ) ',
        ' ( e == 1 and a == 1 and b == 1 ) or ( e == 0 and a == 0 and b == 0 ) ']
    so.getCondition(con)
    print(so.condition)
    so.solve()


# x = {'a': 0, 'b': 0, 'c': 0}
# con = ' ( a == 0 and b == 0 ) and c == 1'
# for i in ['a', 'b', 'c']:
#     con = con.replace(' '+i+' ', f' x[\'{i}\'] ')
# print(con)
# print(eval(con))


# a = 4
# if eval('a == 5'):
#     print('shit')
# fl = []


# def _create(num, count, l=[]):
#     global fl
#     if count == 0:
#         fl += [l]
#         l = l[:-1]
#         return l
#     for i in range(2):
#         l += [i]
#         l = _create(num, count=count-1, l=l)
#     return l[:-1]


# print(_create(num=5, count=5))
# print(fl)


# def gg(num=5,count=5):
#     count=count
#     l=[chr(97+i) for i in range(num)]
#     fl=[]+
