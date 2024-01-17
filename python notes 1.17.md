# Python 学习笔记

## 基础语法与缩进

- Python 使用缩进来表示代码块，通常使用四个空格作为缩进
- 缩进的一致性对于 Python 代码的正确性至关重要

## 数字类型

1. int：整数类型，如 5, -3, 0
2. float：浮点数类型，如 3.14, -0.001, 2.0
3. bool：布尔类型，表示 True 或 False
4. complex：复数类型，如 3+4j, -2-5j  
   用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。  
   **参数说明：**
   - real -- int, long, float或字符串；
   - imag -- int, long, float；

## 数据结构

1. 字符串（String）：用单引号或双引号括起来的文本数据，如 'Hello', "Python"  

   **Python字符串运算符**

   下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：

   | 操作符   | 描述       | 实例       |
   | :--------- | :-------------------------------------------------- | :----------------------------------- |
   | +      | 字符串连接                                                   | >>>a + b<br /> 'HelloPython'         |
   | *      | 重复输出字符串                                               | >>>a * 2 <br />'HelloHello'          |
   | []     | 通过索引获取字符串中字符                                     | >>>a[1]<br /> 'e'                    |
   | [ : ]  | 截取字符串中的一部分                                         | >>>a[1:4]<br /> 'ell'                |
   | in     | 成员运算符 - 如果字符串中包含给定的字符返回 True             | >>>"H" in a <br />True               |
   | not in | 成员运算符 - 如果字符串中不包含给定的字符返回 True           | >>>"M" not in a<br /> True           |
   | r/R    | 原始字符串 - 原始字符串：所有的字符串都是直接按照<br />字面的意思来使用，没有转义特殊或不能打印的字符。 <br />原始字符串除在字符串的第一个引号前加上字母"r"<br />（可以大小写）以外，与普通字符串有着几乎完全相同的语法。 | >>>print r'\n' \n <br />>>> print R'\n' \n |

2. 列表（List）：有序的可变集合，使用方括号括起来，如 [1, 2, 3, 'hello']

   list() 方法可用于将元组转换为列表。  

   | Python 表达式                | 结果                         | 描述                 |
   | :--------------------------- | :--------------------------- | :------------------- |
   | len([1, 2, 3])               | 3                            | 长度                 |
   | [1, 2, 3] + [4, 5, 6]        | [1, 2, 3, 4, 5, 6]           | 组合                 |
   | ['Hi!'] * 4                  | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复                 |
   | 3 in [1, 2, 3]               | True                         | 元素是否存在于列表中 |
   | for x in [1, 2, 3]: print x, | 1 2 3                        | 迭代                 |

3. 元组（Tuple）：有序的不可变集合，使用小括号括起来，如 (1, 2, 3, 'world')

   与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。  
   **运算符同列表**

4. 字典（Dictionary）：无序的键值对集合，使用大括号括起来，如 {'name': 'Alice', 'age': 25}

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