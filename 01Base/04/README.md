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
## 4.8.函数应用:打印图形和数学计算
## 4.9.局部变量
## 4.10.全局变量
## 4.11.函数应用:学生管理系统
## 4.12.函数返回值(二)
## 4.13.函数参数(二)
## 4.14.递归函数
## 4.15.匿名函数
## 4.16.函数使用注意事项