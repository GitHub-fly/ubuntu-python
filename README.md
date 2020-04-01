# 学习心得

> **`Python 中所有涉及到区间的操作，始终是左闭右开 [start, end)`**

## 1. 基本方法的使用

- **内置函数**

  - `input()` 方法，从控制台获取数据
  - `print()` 方法，打印方法，可以结合 C 语言中的语法使用

    > `print()` 方法默认为换行输出，可以在括号内传递参数 `end=''` 使其在末尾追加输出。例如：
    >
    > ```python
    > for i in range(5):
    >    print(i, end=' ')
    > # 输出结果为：'1 2 3 4 5 '
    > ```

  - `range(start, stop, step)`
    > 效果：创建一个整数列表，一般用在 for 循环中  
    > 参数：
    >
    > > start: 计数起始值（`包括`），默认从 0 开始。例如 `range(5)` 等价于 `range(0, 5)`
    > > stop: 计数终止值（`不包括`）。例如 `range(5)` 是 `[0,1,2,3,4]` 没有 5
    > > step: 步长（递增长度），默认为 1。例如 `range(0, 5)` 等价于 `range(0, 5, 1)`
  - `enumerate(list)`
    > 效果：通过此函数处理列表之后再遍历可以同时获得元素 `索引` 和 `值`
    > 适用场景：for 循环

    ```python
    for index, elem in enumerate(list):
        print(index, elem)
    ```

- `字符串`相关方法

  - **rindex(str, start_index, end_index)**
    > 效果：返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报出异常  
    > 参数:
    >
    > > str: 子字符串，必填
    > > start_index: 开始查找的索引（包括），默认为 0  
    > > end_index: 结束查找的索引（不包括），默认为字符串的长度
  - **lower()**
    > 效果：将字符串中的所有大写字母转为小写字母  
    > 适用场景：忽略大小写的比较

- `列表`相关方法

  - **append(obj)**
    > 效果：在列表的末尾直接添加 obj
  - **insert(index, obj)**
    > 效果：在 index 索引处插入 obj
  - **extend(list2)**
    > 效果：在调用者列表的末尾追加新的列表 list2
  - **remove(obj)**
    > 效果：在列表中删除 obj
  - **clear()**
    > 效果：清空列表

- `if elif else` 的使用方法
- 在 `for` 循环中，如果循环对象没有使用，可以用 `'_'` 代替，例如：

  ```python
  for _ in range(5):
      print('我被循环了')
  ```

## 2. 不常用的运算符号操作

- '`//`' ：取整除，返回商的整数部分（向下取整）。例如：

  ```python
  # 结果为 4
  print(9 // 2)

  # 结果为 -5
  print(-9 // 2)
  ```

- `成员运算符`

  - **in**

    > 在指定的列表中找到值返回 True，否则返回 False
    >
    > ```python
    > list = [1, 2, 3, 4, 5, 6]
    > number = 10
    > # 结果返回 False
    > print(number in list)
    > ```

  - **not in** (同上，作用相反)

## 思维导图

- [思维导图 url](https://www.processon.com/mindmap/5e805a28e4b06b8530018fd6)
