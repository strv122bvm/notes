1. 条件控制和循环控制

   - 在Python中，条件控制使用if、elif和else语句，用于根据条件执行不同的代码块。
   - 循环控制使用for和while循环，用于重复执行一段代码块直到满足特定条件。

2. 推导式

   - Python中的推导式是一种简洁的语法，用于快速创建列表、字典和集合。
   - 列表推导式示例：[x for x in range(10) if x % 2 == 0]
   - 字典推导式示例：{k: v for k, v in zip(keys, values)}
   - 集合推导式示例：{x for x in range(10)}

3. 错误和异常捕获

   - Python中的错误和异常捕获使用try-except语句，用于处理可能发生的错误，防止程序崩溃。

   - try 语句的工作方式为：

     - 首先，执行 try 子句 （在 try 和 except 关键字之间的部分）；
     - 如果没有异常发生， except 子句 在 try 语句执行完毕后就被忽略了；
     - 如果在 try 子句执行过程中发生了异常，那么该子句其余的部分就会被忽略；
     - 如果异常匹配于 except 关键字后面指定的异常类型，就执行对应的except子句，然后继续执行 try 语句之后的代码；
     - 如果发生了一个异常，在 except 子句中没有与之匹配的分支，它就会传递到上一级 try 语句中；
     - 如果最终仍找不到对应的处理语句，它就成为一个 未处理异常，终止程序运行，显示提示信息。

   - 示例：

     ```
     try:
         # 可能会出现错误的代码
     except SomeException as e:
         # 处理异常的代码
     ```

4. map、lambda和filter函数的使用

   - map函数：将函数应用于可迭代对象的每个元素，并返回结果组成的迭代器。
   - lambda函数：匿名函数，用于快速定义简单的函数。
   - filter函数：根据指定函数的条件过滤可迭代对象的元素。

   示例：

   ```
   # map示例
   result = map(lambda x: x * 2, [1, 2, 3, 4])
   
   # lambda示例
   add = lambda x, y: x + y
   
   # filter示例
   result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
   ```