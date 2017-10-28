# 4.函数

## 4.1.函数介绍
什么是函数
> 如果在开发程序时，需要某块代码多次，但是为了提高编写的效率以及代码的重用，所 以把具有独立功能的代码块组织为一个小模块，这就是函数

## 4.2.函数定义、调用
- 定义函数
    
    定义函数的格式如下：

```
ef 函数名():
        代码
```
demo:

```
# 定义一个函数，能够完成打印信息的功能
    def printInfo():
        print '------------------------------------'
        print '         人生苦短，我用Python'
        print '------------------------------------'
```

- 调用函数

    定义了函数之后，就相当于有了一个具有某些功能的代码，想要让这些代码能够执行，需要调用它
    
    调用函数很简单的，通过 函数名() 即可完成调用

demo:

```
# 定义完函数后，函数是不会自动执行的，需要调用它才可以
printInfo()
```

## 4.3.函数的文档说明
函数的文档说明

```
>>> def test(a,b):
...     "用来完成对2个数求和"
...     print("%d"%(a+b))
... 
>>> 
>>> test(11,22)
33
```
如果执行，以下代码

```
>>> help(test)
```
能够看到test函数的相关说明

```
Help on function test in module __main__:

test(a, b)
    用来完成对2个数求和
(END)
```

## 4.4.函数参数(一)
1.定义带有参数的函数

示例如下：

```
def add2num(a, b):
    c = a+b
    print c
```

2.调用带有参数的函数

以调用上面的add2num(a, b)函数为例:

```
def add2num(a, b):
    c = a+b
    print c

add2num(11, 22) #调用带有参数的函数时，需要在小括号中，传递数据
```

3.练一练

要求：定义一个函数，完成前2个数完成加法运算，然后对第3个数，进行减法；然后调用这个函数
- 使用def定义函数，要注意有3个参数
- 调用的时候，这个函数定义时有几个参数，那么就需要传递几个参数

4.调用函数时参数的顺序

```
>>> def test(a,b):
...     print(a,b)
... 
>>> test(1,2)
1 2
>>> test(b=1,a=2)
2 1
>>> 
>>> test(b=1,2)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument
>>> 
>>>
```

5.小总结

- 定义时小括号中的参数，用来接收参数用的，称为 “形参”
- 调用时小括号中的参数，用来传递给函数用的，称为 “实参”

## 4.5.函数返回值(一)
1.“返回值”介绍
- 所谓“返回值”，就是程序中函数完成一件事情后，最后给调用者的结果

2.带有返回值的函数

想要在函数中把结果返回给调用者，需要在函数中使用return

如下示例:

```
def add2num(a, b):
        c = a+b
        return c
```
或者

```
def add2num(a, b):
        return a+b
```

3.保存函数的返回值

保存函数的返回值示例如下:

```
    #定义函数
    def add2num(a, b):
        return a+b

    #调用函数，顺便保存函数的返回值
    result = add2num(100,98)

    #因为result已经保存了add2num的返回值，所以接下来就可以使用了
    print result
```
结果:

```
198
```

## 4.6.4种函数的类型
函数根据有没有参数，有没有返回值，可以相互组合，一共有4种

- 无参数，无返回值
- 无参数，又反回
- 有参数，无返回值
- 有参数，有返回值

1.无参数，无返回值的函数

此类函数，不能接收参数，也没有返回值，一般情况下，打印提示灯类似的功能，使用这类的函数

```
 def printMenu():
        print('--------------------------')
        print('      xx涮涮锅 点菜系统')
        print('')
        print('  1.  羊肉涮涮锅')
        print('  2.  牛肉涮涮锅')
        print('  3.  猪肉涮涮锅')
        print('--------------------------')
```

2.无参数，有返回值的函数

此类函数，不能接收参数，但是可以返回某个数据，一般情况下，像采集数据，用此类函数

```
# 获取温度
    def getTemperature():

        #这里是获取温度的一些处理过程

        #为了简单起见，先模拟返回一个数据
        return 24

    temperature = getTemperature()
    print('当前的温度为:%d'%temperature)
```
结果:

```
当前的温度为: 24
```

3.有参数，无返回值的函数

此类函数，能接收参数，但不可以返回数据，一般情况下，对某些变量设置数据而不需结果时，用此类函数

4.有参数，有返回值的函数

此类函数，不仅能接收参数，还可以返回某个数据，一般情况下，像数据处理并需要结果的应用，用此类函数

```
    # 计算1~num的累积和
    def calculateNum(num):

        result = 0
        i = 1
        while i<=num:

            result = result + i

            i+=1

        return result

    result = calculateNum(100)
    print('1~100的累积和为:%d'%result)
```
结果:

```
1~100的累积和为: 5050
```

5.小总结

- 函数根据有没有参数，有没有返回值可以相互组合
- 定义函数时，是根据实际的功能需求来设计的，所以不同开发人员编写的函数类型各不相同

## 4.7.函数的嵌套调用
函数的嵌套调用


```
    def testB():
        print('---- testB start----')
        print('这里是testB函数执行的代码...(省略)...')
        print('---- testB end----')


    def testA():

        print('---- testA start----')

        testB()

        print('---- testA end----')

    testA()
```
结果：

```
    ---- testA start----
    ---- testB start----
    这里是testB函数执行的代码...(省略)...
    ---- testB end----
    ---- testA end----
```
小总结：
- 一个函数里面又调用了另外一个函数，这就是所谓的函数嵌套调用 
- 如果函数A中，调用了另外一个函数B，那么先把函数B中的任务都执行完毕之后才会回到上次 函数A执行的位置

## 4.8.函数应用:打印图形和数学计算
目标

- 感受函数的嵌套调用
- 感受程序设计的思路,复杂问题分解为简单问题
 
思考&实现1

- 写一个函数打印一条横线
- 打印自定义行数的横线

参考代码1

```
# 打印一条横线
def printOneLine():
    print("-"*30)

# 打印多条横线
def printNumLine(num):
    i=0

    # 因为printOneLine函数已经完成了打印横线的功能，
    # 只需要多次调用此函数即可
    while i<num:
        printOneLine()
        i+=1

printNumLine(3)
```

思考&实现2

- 写一个函数求三个数的和
- 写一个函数求三个数的平均值

参考代码2

```
# 求3个数的和
def sum3Number(a,b,c):
    return a+b+c # return 的后面可以是数值，也可是一个表达式

# 完成对3个数求平均值
def average3Number(a,b,c):

    # 因为sum3Number函数已经完成了3个数的就和，所以只需调用即可
    # 即把接收到的3个数，当做实参传递即可
    sumResult = sum3Number(a,b,c)
    aveResult = sumResult/3.0
    return aveResult

# 调用函数，完成对3个数求平均值
result = average3Number(11,2,55)
print("average is %d"%result)
```

## 4.9.局部变量

- 局部变量，就是在函数内部定义的变量
- 不同的函数，可以定义相同的名字的局部变量，但是各用个的不会产生影响
- 局部变量的作用，为了临时保存数据需要在函数中定义变量来进行存储，这就是它的作用

## 4.10.全局变量
1.什么是全局变量

如果一个变量，既能在一个函数中使用，也能在其他的函数中使用，这样的变量就是全局变量

demo如下:

```
    # 定义全局变量
    a = 100

    def test1():
        print(a)

    def test2():
        print(a)

    # 调用函数
    test1()
    test2()
```

2.全局变量和局部变量名字相同问题

![全局变量和局部变量名字相同问题](Image/1.png)

3.修改全局变量

![修改全局变量](Image/2.png)

4.总结1

- 在函数外边定义的变量叫做全局变量
- 全局变量能够在所有的函数中进行访问
- 如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
- 如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，小技巧强龙不压地头蛇

5.可变类型的全局变量

```
>>> a = 1
>>> def f():
...     a += 1
...     print a
...
>>> f()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in f
UnboundLocalError: local variable 'a' referenced before assignment
>>>
>>>
>>> li = [1,]
>>> def f2():
...     li.append(1)
...     print li
...
>>> f2()
[1, 1]
>>> li
[1, 1]
```

6.总结2：

- 在函数中不使用global声明全局变量时不能修改全局变量的本质是不能修改全局变量的指向，即不能将全局变量指向新的数据。
- 对于不可变类型的全局变量来说，因其指向的数据不能修改，所以不使用global时无法修改全局变量。
- 对于可变类型的全局变量来说，因其指向的数据可以修改，所以不使用global时也可修改全局变量。

## 4.11.函数应用:学生管理系统
## 4.12.函数返回值(二)
在python中我们可不可以返回多个值？

```
>>> def divid(a, b):
...     shang = a//b
...     yushu = a%b 
...     return shang, yushu
...
>>> sh, yu = divid(5, 2)
>>> sh
5
>>> yu
1
```
本质是利用了元组

## 4.13.函数参数(二)
1. 缺省参数

调用函数时，缺省参数的值如果没有传入，则被认为是默认值。下例会打印默认的age，如果age没有被传入：

```
def printinfo( name, age = 35 ):
   # 打印任何传入的字符串
   print "Name: ", name
   print "Age ", age

# 调用printinfo函数
printinfo(name="miki" )
printinfo( age=9,name="miki" )
```
以上实例输出结果：

```
Name:  miki
Age  35
Name:  miki
Age  9
```
注意：带有默认值的参数一定要位于参数列表的最后面。

```
>>> def printinfo(name, age=35, sex):
...     print name
...
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```

2.不定长参数

有时可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，声明时不会命名。

基本语法如下：

```
    def functionname([formal_args,] *args, **kwargs):
       "函数_文档字符串"
       function_suite
       return [expression]
```

加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。

```
>>> def fun(a, b, *args, **kwargs):
...     """可变参数演示示例"""
...     print "a =", a
...     print "b =", b
...     print "args =", args
...     print "kwargs: "
...     for key, value in kwargs.items():
...         print key, "=", value
...
>>> fun(1, 2, 3, 4, 5, m=6, n=7, p=8)  # 注意传递的参数对应
a = 1
b = 2
args = (3, 4, 5)
kwargs: 
p = 8
m = 6
n = 7
>>>
>>>
>>>
>>> c = (3, 4, 5)
>>> d = {"m":6, "n":7, "p":8}
>>> fun(1, 2, *c, **d)    # 注意元组与字典的传参方式
a = 1
b = 2
args = (3, 4, 5)
kwargs: 
p = 8
m = 6
n = 7
>>>
>>>
>>>
>>> fun(1, 2, c, d) # 注意不加星号与上面的区别
a = 1
b = 2
args = ((3, 4, 5), {'p': 8, 'm': 6, 'n': 7})
kwargs:
>>>
>>>
```

3.引用传参

- 可变类型与不可变类型的变量分别作为函数参数时，会有什么不同吗？
- Python有没有类似C语言中的指针传参呢？

```
>>> def selfAdd(a):
...     """自增"""
...     a += a
...
>>> a_int = 1
>>> a_int
1
>>> selfAdd(a_int)
>>> a_int
1
>>> a_list = [1, 2]
>>> a_list
[1, 2]
>>> selfAdd(a_list)
>>> a_list
[1, 2, 1, 2]

```
**Python中函数参数是引用传递（注意不是值传递）。对于不可变类型，因变量不能修改，所以运算不会影响到变量自身；而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。**

想一想为什么

```
>>> def selfAdd(a):
...     """自增"""
...     a = a + a   # 我们更改了函数体的这句话
...
>>> a_int = 1
>>> a_int
1
>>> selfAdd(a_int)
>>> a_int
1
>>> a_list = [1, 2]
>>> a_list
[1, 2]
>>> selfAdd(a_list)
>>> a_list
[1, 2]      # 想一想为什么没有变呢？
```

## 4.14.递归函数
1.什么是递归函数

通过前面的学习知道一个函数可以调用其他函数。

如果一个函数在内部不调用其它的函数，而是自己本身的话，这个函数就是递归函数。

2.递归函数的作用

举个例子，我们来计算阶乘 n! = 1 * 2 * 3 * ... * n

解决办法1:

![解决办法1](Image/3.png)

看阶乘的规律

```
1! = 1
2! = 2 × 1 = 2 × 1!
3! = 3 × 2 × 1 = 3 × 2!
4! = 4 × 3 × 2 × 1 = 4 × 3!
...
n! = n × (n-1)!

```
解决办法2:

![解决办法2](Image/4.png)

原理

![原理](Image/digui_jiecheng.png)

## 4.15.匿名函数
## 4.16.函数使用注意事项