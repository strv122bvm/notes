# Python 学习笔记

## 基础语法与缩进

- Python 使用缩进来表示代码块，通常使用四个空格作为缩进
- 缩进的一致性对于 Python 代码的正确性至关重要

## 数字类型

1. int：整数类型，如 5, -3, 0

2. float：浮点数类型，如 3.14, -0.001, 2.0

3. bool：布尔类型，表示 True 或 False

4. complex：复数类型，如 3+4j, -2-5j

   返回值为 *real* + *imag* *1j 的复数，或将字符串或数字转换为复数。如果第一个形参是字符串，则它被解释为一个复数，并且函数调用时必须没有第二个形参。第二个形参不能是字符串。每个实参都可以是任意的数值类型（包括复数）。如果省略了 *imag*，则默认值为零，构造函数会像 [`int`](https://docs.python.org/zh-cn/3/library/functions.html?highlight=complex#int) 和 [`float`](https://docs.python.org/zh-cn/3/library/functions.html?highlight=complex#float) 一样进行数值转换。如果两个实参都省略，则返回 `0j`。

## 数据结构

1. 字符串（String）：用单引号或双引号括起来的文本数据，如 'Hello', "Python"

2. 列表（List）：有序的可变集合，使用方括号括起来，如 [1, 2, 3, 'hello']

   list() 方法可用于将元组转换为列表。

3. 字典（Dictionary）：无序的键值对集合，使用大括号括起来，如 {'name': 'Alice', 'age': 25}

4. 元组（Tuple）：有序的不可变集合，使用小括号括起来，如 (1, 2, 3, 'world')

   与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

   | Python 表达式                | 结果                         | 描述         |
   | :--------------------------- | :--------------------------- | :----------- |
   | len((1, 2, 3))               | 3                            | 计算元素个数 |
   | (1, 2, 3) + (4, 5, 6)        | (1, 2, 3, 4, 5, 6)           | 连接         |
   | ('Hi!',) * 4                 | ('Hi!', 'Hi!', 'Hi!', 'Hi!') | 复制         |
   | 3 in (1, 2, 3)               | True                         | 元素是否存在 |
   | for x in (1, 2, 3): print x, | 1 2 3                        | 迭代         |

5. 集合（Set）：无序的不重复元素集合，使用大括号括起来，如 {1, 2, 3, 4, 5}

6. 切片（Slice）：用于从序列中获取子序列的一种方法，如 list[1:3], string[2:], tuple[:4]

   返回一个表示由 `range(start, stop, step)` 指定的索引集的 [slice](https://docs.python.org/zh-cn/3/glossary.html#term-slice) 对象。*start* 参数默认为 `0` ,*step* 参数默认为 `1`。

   ``` 
   a[start:stop]       # 从 index=start 开始（即包含start），到 index=stop-1（即不包含stop） 
   a[start:]      	    # 从 index=start 开始（包含 start ），到最后 
   a[:stop]       	    # 从头开始，到 stop-1 
   a[:]                # 取整个 List
   a[start:stop:step]  # 从 index=start 到 index=stop-1，每隔 step 取一个，不超过 stop-1

## 示例

```
# 数据结构示例
string_example = 'Hello, Python!'
list_example = [1, 2, 3, 'hello']
dictionary_example = {'name': 'Alice', 'age': 25}
tuple_example = (1, 2, 3, 'world')
set_example = {1, 2, 3, 4, 5}
slice_example = list_example[1:3]
```