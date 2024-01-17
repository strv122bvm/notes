# 基本语法

## 1.标题语法

n个# 代表n级标题

## 2.段落语法

用空白行创建新段落

## 3.换行语法

双空格+回车（直接回车也可以）

## 4.强调语法

*斜体*(`* *`)         **粗体**(`** **`)          ***粗斜体*** (`*** ***`)

## 5.引用语法

> 块引用

> 多个段落
>
> 块引用（回车直接换两行）

> 嵌套
>
> > 块引用
> >
> > > n层嵌套

块引用可使用其他markdown格式的元素（如强调等）

## 6.列表语法

要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点。数字不必按数学顺序排列，但是列表应当以数字 1 起始。

句点后加内容（包括空格）后回车自动列出下一个，tab进行嵌套，一次回车向前缩进一次

***例：***

1.   
   1. 123  
   2.   
      1.   
2.   
3. 

## 7.代码语法

要将单词或短语表示为代码，请将其包裹在反引号 (`) 中

***例：***

At the command prompt, type `nano`

### 转义反引号

如果你要表示为代码的单词或短语中包含一个或多个反引号，则可以通过将单词或短语包裹在双反引号(``)中

***例：***

```
Use `code` in your Markdown file.
```

## 8.分隔线语法

要创建分隔线，请在单独一行上使用三个或多个星号 (`***`)、破折号 (`---`) 或下划线 (`___`) ，并且不能包含其他内容。

****

## 9.链接语法

链接文本放在中括号内，链接地址放在后面的括号中，链接title可选。

超链接Markdown语法代码：`[超链接显示名](超链接地址 "超链接title")`

### 给链接增加 Title

链接title是当鼠标悬停在链接上时会出现的文字，这个title是可选的，它放在圆括号中链接地址后面，跟链接地址之间以空格分隔。

### 网址和Email地址

使用尖括号(`< >`)可以很方便地把URL或者email地址变成可点击的链接。

### 带格式化的链接

*强调*链接, 在链接语法前后增加星号。 要将链接表示为代码，请在方括号中添加反引号。

***例：***

![img](https://github.com/strv122bvm/typora.img/blob/main/QQ%E6%88%AA%E5%9B%BE20240117014340.png "带格式化的链接")

### 引用类型链接

引用样式链接是一种特殊的链接，它使URL在Markdown中更易于显示和阅读。参考样式链接分为两部分：与文本保持内联的部分以及存储在文件中其他位置的部分，以使文本易于阅读。

#### 链接的第一部分格式

引用类型的链接的第一部分使用两组括号进行格式设置。第一组方括号包围应显示为链接的文本。第二组括号显示了一个标签，该标签用于指向您存储在文档其他位置的链接。

尽管不是必需的，可以在第一组和第二组括号之间包含一个空格。第二组括号中的标签不区分大小写，可以包含字母，数字，空格或标点符号。

以下示例格式对于链接的第一部分效果相同：

- `[hobbit-hole][1]`
- `[hobbit-hole] [1]`

#### 链接的第二部分格式

引用类型链接的第二部分使用以下属性设置格式：

1. 放在括号中的标签，其后紧跟一个冒号和至少一个空格（例如`[label]:`）。
2. 链接的URL，可以选择将其括在尖括号中。
3. 链接的可选标题，可以将其括在双引号，单引号或括号中。

以下示例格式对于链接的第二部分效果相同：

- `[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle`
- `[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"`
- `[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'`
- `[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)`
- `[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"`
- `[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> 'Hobbit lifestyles'`
- `[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> (Hobbit lifestyles)`

可以将链接的第二部分放在Markdown文档中的任何位置。有些人将它们放在出现的段落之后，有些人则将它们放在文档的末尾（例如尾注或脚注）

## 10.图片语法

[![沙漠中的岩石图片](/assets/img/shiprock.jpg "Shiprock")](https://markdown.com.cn )
