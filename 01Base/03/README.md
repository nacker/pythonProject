# 3.字符串、列表、元组、字典

## 3.1.字符串介绍
python中字符串的格式

如下定义的变量a，存储的是数字类型的值

```
a = 100
```
如下定义的变量b，存储的是字符串类型的值

```
    b = "hello"
    或者
    b = 'hello'

```
**小总结：**
双引号或者单引号中的数据，就是字符串

## 3.2.字符串输出
demo

```
    name = 'xiaoming'
    position = 'CEO'
    address = 'xx公司'

    print('--------------------------------------------------')
    print("姓名：%s"%name)
    print("职位：%s"%position)
    print("公司地址：%s"%address)
    print('--------------------------------------------------')
```
结果:

```
--------------------------------------------------
姓名： xiaoming
职位： CEO
公司地址： xx公司
--------------------------------------------------
```

## 3.3.字符串输入
demo:

```
    userName = input('请输入用户名:')
    print("用户名为：%s"%userName)

    password = input('请输入密码:')
    print("密码为：%s"%password)
```
结果：（根据输入的不同结果也不同）

```
    请输入用户名:dongGe
    用户名为： dongGe
    请输入密码:haohaoxuexitiantianxiangshang
    密码为： haohaoxuexitiantianxiangshang
```

## 3.4.下标和切片
1. 下标索引

字符串中"下标"的使用

python中下标从 0 开始

```
   name = 'abcdef'

   print(name[0])
   print(name[1])
   print(name[2])
```

2. 切片

切片是指对操作的对象截取其中一部分的操作。字符串、列表、元组都支持切片操作。

切片的语法：[起始:结束:步长]

注意：选取的区间属于左闭右开型，即从"起始"位开始，到"结束"位的前一位结束（不包含结束位本身)。

我们以字符串为例讲解。

如果取出一部分，则可以在中括号[]中，使用:

```
name = 'abcdef'
print(name[0:3]) # 取 下标0~2 的字符
```

```
name = 'abcdef'
print(name[0:5]) # 取 下标为0~4 的字符
```

```
name = 'abcdef'
print(name[3:5]) # 取 下标为3、4 的字符
```

```
name = 'abcdef'
print(name[2:]) # 取 下标为2开始到最后的字符
```

```
name = 'abcdef'
print(name[1:-1]) # 取 下标为1开始 到 最后第2个  之间的字符
```

```
 >>> a = "abcdef"
 >>> a[:3]
 'abc'
 >>> a[::2]
 'ace'
 >>> a[5:1:2] 
 ''
 >>> a[1:5:2]
 'bd'
 >>> a[::-2]
 'fdb' 
 >>> a[5:1:-2]
 'fd'
```

## 3.5.字符串常见操作
1.find

检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1

```
mystr.find(str, start=0, end=len(mystr))
```

2.index

跟find()方法一样，只不过如果str不在 mystr中会报一个异常.

```
mystr.index(str, start=0, end=len(mystr)) 
```

3.count

返回 str在start和end之间 在 mystr里面出现的次数

```
mystr.count(str, start=0, end=len(mystr))
```

4.replace

把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

```
mystr.replace(str1, str2,  mystr.count(str1))
```
5.split

以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串

```
mystr.split(str=" ", 2) 
```

6.capitalize

把字符串的第一个字符大写

```
mystr.capitalize()
```

7.title

把字符串的每个单词首字母大写

```
>>> a = "hello word"
>>> a.title()
'Hello Word'
```

8.startswith

检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False

```
mystr.startswith(obj)
```

9.endswith

检查字符串是否以obj结束，如果是返回True,否则返回 False.

```
mystr.endswith(obj)
```

10.lower

转换 mystr 中所有大写字符为小写

```
mystr.upper()
```

11.upper

转换 mystr 中的小写字母为大写

```
mystr.upper()
```

12.ljust

返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串

```
mystr.ljust(width)
```

13.rjust

返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

```
mystr.rjust(width)
```

14.center

返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

```
mystr.center(width)
```

15.lstrip

删除 mystr 左边的空白字符

```
mystr.lstrip()
```

16.rstrip

删除 mystr 字符串末尾的空白字符

```
mystr.rstrip()
```

17.strip

删除mystr字符串两端的空白字符

```
>>> a = "\n\t hello \t\n"
>>> a.strip()
'hello'
```

18.rfind

类似于 find()函数，不过是从右边开始查找.

```
mystr.rfind(str, start=0,end=len(mystr) )
```

19.rindex

类似于 index()，不过是从右边开始.

```
mystr.rindex( str, start=0,end=len(mystr))
```

20.partition

把mystr以str分割成三部分,str前，str和str后

```
mystr.partition(str)
```
21.rpartition

类似于 partition()函数,不过是从右边开始.

```
mystr.rpartition(str)
```

22.splitlines

按照行分隔，返回一个包含各行作为元素的列表

```
mystr.splitlines()
```

23.isalpha

如果 mystr 所有字符都是字母 则返回 True,否则返回 False

```
mystr.isalpha()
```

24.isdigit

如果 mystr 只包含数字则返回 True 否则返回 False.

```
mystr.isdigit()
```

25.isalnum

如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False

```
mystr.isalnum()
```

26.isspace

如果 mystr 中只包含空格，则返回 True，否则返回 False.

```
mystr.isspace()
```

27.join

mystr 中每个字符后面插入str,构造出一个新的字符串

```
mystr.join(str)
```
## 3.6.列表介绍
1.列表的格式

变量A的类型为列表

```
namesList = ['xiaoWang','xiaoZhang','xiaoHua']
```
比C语言的数组强大的地方在于列表中的元素可以是不同类型的

```
testList = [1, 'a']
```
2.打印列表
demo:

```
    namesList = ['xiaoWang','xiaoZhang','xiaoHua']
    print(namesList[0])
    print(namesList[1])
    print(namesList[2])
```
结果：

```
    xiaoWang
    xiaoZhang
    xiaoHua
```

## 3.7.列表的循环遍历
1. 使用for循环

为了更有效率的输出列表的每个数据，可以使用循环来完成

demo:

```
    namesList = ['xiaoWang','xiaoZhang','xiaoHua']
    for name in namesList:
        print(name)
```
结果:

```
    xiaoWang
    xiaoZhang
    xiaoHua
```


2. 使用while循环

为了更有效率的输出列表的每个数据，可以使用循环来完成

demo:

```
    namesList = ['xiaoWang','xiaoZhang','xiaoHua']

    length = len(namesList)

    i = 0

    while i<length:
        print(namesList[i])
        i+=1
```
结果:

```
    xiaoWang
    xiaoZhang
    xiaoHua
```

## 3.8.列表的常见操作
1.添加元素("增"append, extend, insert)

- append

通过append可以向列表添加元素

demo:

```
    #定义变量A，默认有3个元素
    A = ['xiaoWang','xiaoZhang','xiaoHua']

    print("-----添加之前，列表A的数据-----")
    for tempName in A:
        print(tempName)

    #提示、并添加元素
    temp = input('请输入要添加的学生姓名:')
    A.append(temp)

    print("-----添加之后，列表A的数据-----")
    for tempName in A:
        print(tempName)
```

- extend

通过extend可以将另一个集合中的元素逐一添加到列表中

```
>>> a = [1, 2]
>>> b = [3, 4]
>>> a.append(b)
>>> a
[1, 2, [3, 4]]
>>> a.extend(b)
>>> a
[1, 2, [3, 4], 3, 4]
```

- insert

insert(index, object) 在指定位置index前插入元素object

```
>>> a = [0, 1, 2]
>>> a.insert(1, 3)
>>> a
[0, 3, 1, 2]
```

2.修改元素("改")

修改元素的时候，要通过下标来确定要修改的是哪个元素，然后才能进行修改

demo:

```
    #定义变量A，默认有3个元素
    A = ['xiaoWang','xiaoZhang','xiaoHua']

    print("-----修改之前，列表A的数据-----")
    for tempName in A:
        print(tempName)

    #修改元素
    A[1] = 'xiaoLu'

    print("-----修改之后，列表A的数据-----")
    for tempName in A:
        print(tempName)
```

结果:

```
    -----修改之前，列表A的数据-----
    xiaoWang
    xiaoZhang
    xiaoHua
    -----修改之后，列表A的数据-----
    xiaoWang
    xiaoLu
    xiaoHua
```

3.查找元素("查"in, not in, index, count)

所谓的查找，就是看看指定的元素是否存在

##### in, not in

python中查找的常用方法为：

> - in（存在）,如果存在那么结果为true，否则为false <br>
> - not in（不存在），如果不存在那么结果为true，否则false

demo

```
    #待查找的列表
    nameList = ['xiaoWang','xiaoZhang','xiaoHua']

    #获取用户要查找的名字
    findName = input('请输入要查找的姓名:')

    #查找是否存在
    if findName in nameList:
        print('在字典中找到了相同的名字')
    else:
        print('没有找到')
```
说明：
> in的方法只要会用了，那么not in也是同样的用法，只不过not in判断的是不存在

##### index, count

index和count与字符串中的用法相同

```
>>> a = ['a', 'b', 'c', 'a', 'b']
>>> a.index('a', 1, 3) # 注意是左闭右开区间
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'a' is not in list
>>> a.index('a', 1, 4)
3
>>> a.count('b')
2
>>> a.count('d')
0
```

4.删除元素("删"del, pop, remove)

列表元素的常用删除方法有：

- del：根据下标进行删除
- pop：删除最后一个元素
- remove：根据元素的值进行删除

demo:(del)

```
    movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

    print('------删除之前------')
    for tempName in movieName:
        print(tempName)

    del movieName[2]

    print('------删除之后------')
    for tempName in movieName:
        print(tempName)
```
结果:

```
    ------删除之前------
    加勒比海盗
    骇客帝国
    第一滴血
    指环王
    霍比特人
    速度与激情
    ------删除之后------
    加勒比海盗
    骇客帝国
    指环王
    霍比特人
    速度与激情

```

demo:(pop)

```
   movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

    print('------删除之前------')
    for tempName in movieName:
        print(tempName)

    movieName.pop()

    print('------删除之后------')
    for tempName in movieName:
        print(tempName)
```

结果:

```
    ------删除之前------
    加勒比海盗
    骇客帝国
    第一滴血
    指环王
    霍比特人
    速度与激情
    ------删除之后------
    加勒比海盗
    骇客帝国
    第一滴血
    指环王
    霍比特人
```

demo:(remove)

```
    movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

    print('------删除之前------')
    for tempName in movieName:
        print(tempName)

    movieName.remove('指环王')

    print('------删除之后------')
    for tempName in movieName:
        print(tempName)
```

结果:

```
    ------删除之前------
    加勒比海盗
    骇客帝国
    第一滴血
    指环王
    霍比特人
    速度与激情
    ------删除之后------
    加勒比海盗
    骇客帝国
    第一滴血
    霍比特人
    速度与激情
```

5.排序(sort, reverse)

sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。

reverse方法是将list逆置。

```
>>> a = [1, 4, 2, 3]
>>> a
[1, 4, 2, 3]
>>> a.reverse()
>>> a
[3, 2, 4, 1]
>>> a.sort()
>>> a
[1, 2, 3, 4]
>>> a.sort(reverse=True)
>>> a
[4, 3, 2, 1]
```

## 3.9.列表的嵌套
1.列表嵌套

类似while循环的嵌套，列表也是支持嵌套的

一个列表中的元素又是一个列表，那么这就是列表的嵌套

```
    schoolNames = [['北京大学','清华大学'],
                    ['南开大学','天津大学','天津师范大学'],
                    ['山东大学','中国海洋大学']]
```

2.应用

一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配

```
#encoding=utf-8

import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

i = 0
for name in names:
    index = random.randint(0,2)    
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)
```

## 3.10.元组
Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。

```
>>> aTuple = ('et',77,99.9)
>>> aTuple
('et',77,99.9)
```
1.访问元组

```
>>>tuple = ('hello',100,3.14)
>>>tuple[0]
'hello'
>>>tuple[1]
100
>>>tuple[2]
3.14
>>>
```

2.修改元组

```
>>> tuple[2] = 188
```
说明： python中不允许修改元组的数据，包括不能删除其中的元素。

3.元组的内置函数count, index

index和count与字符串和列表中的用法相同

```
>>> a = ('a', 'b', 'c', 'a', 'b')
>>> a.index('a', 1, 3) # 注意是左闭右开区间
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple
>>> a.index('a', 1, 4)
3
>>> a.count('b')
2
>>> a.count('d')
0
```

## 3.11.字典介绍
1.软件开发中的字典

变量info为字典类型：

```
info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
```
说明：
- 字典和列表一样，也能够存储多个数据
- 列表中找某个元素时，是根据下标进行的
- 字典中找某个元素时，是根据'名字'（就是冒号:前面的那个值，例如上面代码中的'name'、'id'、'sex'）
- 字典的每个元素由2部分组成，键:值。例如 'name':'班长' ,'name'为键，'班长'为值

2.根据键访问值

```
info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

print(info['name'])
print(info['address'])
```
结果:

```
班长
    地球亚洲中国北京
```
若访问不存在的键，则会报错：

```
>>> info['age']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
```
在我们不确定字典中是否存在某个键而又想获取其值时，可以使用get方法，还可以设置默认值：

```
>>> age = info.get('age')
>>> age #'age'键不存在，所以age为None
>>> type(age)
<type 'NoneType'>
>>> age = info.get('age', 18) # 若info中不存在'age'这个键，就返回默认值18
>>> age
18
```

## 3.12.字典的常见操作1
1.修改元素

字典的每个元素中的数据是可以修改的，只要通过key找到，即可修改

demo:

```
info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

    newId = input('请输入新的学号')

    info['id'] = int(newId)

    print('修改之后的id为%d:'%info['id'])
```

2.添加元素

demo:访问不存在的元素

```
info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}

print('id为:%d'%info['id'])
```

如果在使用 变量名['键'] = 数据 时，这个“键”在字典中，不存在，那么就会新增这个元素

demo:添加新的元素

```
info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}

    # print('id为:%d'%info['id'])#程序会终端运行，因为访问了不存在的键

    newId = input('请输入新的学号')

    info['id'] = newId

    print('添加之后的id为:%d'%info['id'])
```
结果:

```
请输入新的学号188
添加之后的id为: 188
```

3.删除元素

对字典进行删除操作，有一下几种：
- del
- clear()

demo:del删除指定的元素

```
    info = {'name':'班长', 'sex':'f', 'address':'地球亚洲中国北京'}

    print('删除前,%s'%info['name'])

    del info['name']

    print('删除后,%s'%info['name'])
```

demo:del删除整个字典

```
    info = {'name':'monitor', 'sex':'f', 'address':'China'}

    print('删除前,%s'%info)

    del info

    print('删除后,%s'%info)
```

demo:clear清空整个字典

```
    info = {'name':'monitor', 'sex':'f', 'address':'China'}

    print('清空前,%s'%info)

    info.clear()

    print('清空后,%s'%info)
```

## 3.13.字典的常见操作2
1.len()

测量字典中，键值对的个数

```
>>> dict = {"name":'zhangsan','sex':'m'}
>>> len(dict)
2
>>>
```

2.keys

返回一个包含字典所有KEY的列表

```
>>> dict = {"name":'zhangsan','sex':'m'}
>>> dict.keys()
['name','sex']
>>>
```

3.values

返回一个包含字典所有value的列表

```
>>> dict = {"name":'zhangsan','sex':'m'}
>>> dict.values()
['zhangsan','m']
>>>
```

4.items

返回一个包含所有（键，值）元祖的列表

```
>>> dict = {"name":'zhangsan','sex':'m'}
>>> dict.items()
[('name','zhangsan'),('sex','m')]
>>>
```

5.has_key

dict.has_key(key)如果key在字典中，返回True，否则返回False

```
>>> dict = {"name":'zhangsan','sex':'m'}
>>> dict.has_key('name')
True
>>> dict.has_key('phone')
False
>>>
```


## 3.14.字典的遍历
通过for ... in ...:的语法结构，我们可以遍历字符串、列表、元组、字典等数据结构。

注意python语法的缩进

### 字符串遍历

```
>>> a_str = "hello word"
>>> for char in a_str:
...     print(char,end=' ')
...
h e l l o   w o r d
```

### 列表遍历

```
>>> a_list = [1, 2, 3, 4, 5]
>>> for num in a_list:
...     print(num,end=' ')
...
1 2 3 4 5

```

### 元组遍历

```
>>> a_turple = (1, 2, 3, 4, 5)
>>> for num in a_turple:
...     print(num,end=" ")
1 2 3 4 5
```

### 字典遍历
- 遍历字典的key（键）

```
>>> dict = {"name":'zhangsan','sex':'m'}
>>> for key in dict.keys():
...     print key
... 
name
sex
>>>
```

- 遍历字典的value（值）

```
>>> dict = {"name":'zhangsan','sex':'m'}
>>> for value in dict.keys():
...     print value
... 
zhangsan
m
>>>
```

- 遍历字典的项（元素）

```
>>> dict = {"name":'zhangsan','sex':'m'}
>>> for item in dict.items():
...     print item
... 
('name','zhangsan')
('sex','m')
```

- 遍历字典的key-value（键值对）

```
>>> dict = {"name":'zhangsan','sex':'m'}
>>> for key,value in dict.items():
...     print("key=%s,value=%s"%(key,value))
... 
key=name,value=zhangsan
key=sex,value=m
>>>
```

如何实现带下标索引的遍历

```
>>> chars = ['a', 'b', 'c', 'd']
>>> i = 0
>>> for chr in chars:
...     print("%d %s"%(i, chr))
...     i += 1
...
0 a
1 b
2 c
3 d
```

enumerate()

```
>>> chars = ['a', 'b', 'c', 'd']
>>> for i, chr in enumerate(chars):
...     print i, chr
...
0 a
1 b
2 c
3 d
```

## 3.15.公共方法
运算符
    <table>
        <tr>
            <th>运算符</th>
            <th>Python 表达式</th>
            <th>结果</th>
            <th>描述</th>
            <th>支持的数据类型</th>
        </tr>
        <tr>
            <th>+</th>
            <th>[1, 2] + [3, 4]</th>
            <th>[1, 2, 3, 4]</th>
            <th>合并</th>
            <th>字符串、列表、元组</th>
        </tr>
        <tr>
            <th>*</th>
            <th>'Hi!' * 4</th>
            <th>['Hi!', 'Hi!', 'Hi!', 'Hi!']</th>
            <th>复制</th>
            <th>字符串、列表、元组</th>
        </tr>
        <tr>
            <th>in</th>
            <th>3 in (1, 2, 3)</th>
            <th>True</th>
            <th>元素是否存在</th>
            <th>字符串、列表、元组、字典</th>
        </tr>
        <tr>
            <th>not in</th>
            <th>4 not in (1, 2, 3)</th>
            <th>True</th>
            <th>元素是否不存在</th>
            <th>字符串、列表、元组、字典</th>
        </tr>
    </table>
    
## 3.16.引用

