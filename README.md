# 条件判断问题解决的通用脚本 (仅限0-1变量)

> 基于***python***的简易条件判断 \(**多变量多条件**\)

## 基础使用方法

**示例：**

某学校要从a、b、c、d、e五位学生中选派若干人参加暑期社会实践项目。选派中必须满足以下条件：

1）若a去，则b也去。

2）d、e两人中必有一人去。

3）b、c两人中去且仅去一人。

4）c、d两人同去或同不去。

5）若e去，则a、b也同去。
试给出所有的选派方案。


```python
con = [
    ' e or d ',
    ' ( b == 1 and c == 0 ) or ( b == 0 and c == 1 ) ',
    ' ( a == 1 and b == 1 ) or ( a == 0 and b == 0 ) ',
    ' ( c == 1 and d == 1 ) or ( c == 0 and d == 0 ) ',
    ' ( e == 1 and a == 1 and b == 1 ) or ( e == 0 and a == 0 and b == 0 ) '
]

so = (
    solution()
        .initialize(num=5)
        .getCondition(con)
        .solve()
)

print(so.result)
```

**输出：**

```python
{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 0}为正解
{'a': 1, 'b': 1, 'c': 0, 'd': 0, 'e': 1}为正解
结果已保存至self.results
[{'a': 0, 'b': 0, 'c': 1, 'd': 1, 'e': 0}, {'a': 1, 'b': 1, 'c': 0, 'd': 0, 'e': 1}]
```

## 核心
> * 通过 ***递归*** 进行可能性的创建与条件的判断

### 所有可能的创建
```python
_multiPossibilities(self, num, count, l=[])
```

该方法通过传入的 `num` 与 `count` 参数进行变量与可能性的创建与匹配

```python
def _multiPossibilities(self, num, count, l=[]):
    if count == 0:
        self.data += [l]
        l = l[:-1]
        return l
    for i in range(2):
        l += [i]
        l = self._multiPossibilities(num, count=count-1, l=l)
    return l[:-1]
```

使用 `for` 循环每个变量递归创建两个分支，形成递归树

---

### 条件的判断
```python
_solve(self, poss, length, count=0)
```

该函数通过poss传递条件(字符串)

使用 `eval()` 进行字符串的转换，将其与 `if` 合并实现条件判断

```python
def _solve(self, poss, length, count=0):
    if count == length:
        self.results += [poss]
        print(f'{poss}为正解')
        return
    condition = self.condition[count]
    if eval(condition):
        self._solve(poss, length, count+1)
```

与**可能性的生成**不同，条件的判断使用的不是树的思想，仅是简单的条件递进

**[条件判断.py](./条件判断.py)文件**
