面向对象编程（OOP）是一种常用的编程范式，它特别强调数据（对象）和操作数据的方法（函数）的封装。Python是一种支持OOP的语言。下面是一份关于Python中面向对象编程的基础知识点的学习笔记：

### 1. 类与实例化
- **类（Class）**：是创建对象的模板，它定义了一组属性和方法。
- **实例（Instance）**：是根据类创建的对象，每个实例都有独立的属性集合。

```python
class MyClass:
    def __init__(self, value):  # 构造函数
        self.my_attribute = value

instance = MyClass(5)
```

### 2. 类变量与实例变量
- **类变量**：是类的所有实例共享的变量。
- **实例变量**：是属于每个独立实例的变量。

```python
class MyClass:
    class_variable = "共享的变量"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
```

### 3. 方法
- **方法**：定义在类内部的函数，用于实现类的行为。

```python
class MyClass:
    def my_method(self):
        return "这是一个类的方法"
```

### 4. 私有变量和私有方法
- **私有变量和私有方法**：以双下划线（`__`）开头，只能在类的内部访问。

```python
class MyClass:
    def __init__(self):
        self.__private_variable = "私有变量"

    def __private_method(self):
        return "私有方法"
```

### 5. 封装
- **封装**：是将数据（属性）和行为（方法）捆绑在一起的过程。

### 6. 继承
- **继承**：允许一个类继承另一个类的特性。

```python
class ParentClass:
    pass

class ChildClass(ParentClass):  # 继承ParentClass
    pass
```

### 7. 多态
- **多态**：指派生类的实例可以替代其基类的实例。

```python
class ParentClass:
    def my_method(self):
        return "Parent"

class ChildClass(ParentClass):
    def my_method(self):
        return "Child"

def example_function(obj):
    print(obj.my_method())

parent = ParentClass()
child = ChildClass()

example_function(parent)  # 输出 Parent
example_function(child)  # 输出 Child
```

