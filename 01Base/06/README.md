# 6.文件操作、综合应用

## 6.1.面向对象编程介绍

- 面向过程：根据业务逻辑从上到下写代码
- 面向对象：将数据与函数绑定到一起，进行封装，这样能够更快速的开发程序，减少了重复代码的重写过程

面向对象(object-oriented ;简称: OO) 至今还没有统一的概念 我这里把它定义为: 按人们 认识客观世界的系统思维方式,采用基于对象(实体) 的概念建立模型,模拟客观世界分析、设 计、实现软件的办法。

面向对象编程(Object Oriented Programming-OOP) 是一种解决软件复用的设计和编程方法。 这种方法把软件系统中相近相似的操作逻辑和操作 应用数据、状态,以类的型式描述出来,以对象实例的形式在软件系统中复用,以达到提高软件开发效率的作用。

## 6.2.类和对象
1. 类
    
```
人以类聚 物以群分。
具有相似内部状态和运动规律的实体的集合(或统称为抽象)。 
具有相同属性和行为事物的统称
```
类是抽象的,在使用的时候通常会找到这个类的一个具体的存在,使用这个具体的存在。一个类可以找到多个对象

2. 对象

```
某一个具体事物的存在 ,在现实世界中可以是看得见摸得着的。
可以是直接使用的
```

3.类和对象之间的关系

类就是创建对象的模板

4.练习：区分类和对象

```
奔驰汽车 类
奔驰smart 类 
张三的那辆奔驰smart 对象
狗 类
大黄狗 类 
李四家那只大黄狗 对象 
水果 类
苹果 类 
红苹果 类 红富士苹果 类 
我嘴里吃了一半的苹果 对象
```

5.类的构成

类(Class) 由3个部分构成
    - 类的名称:类名
    - 类的属性:一组数据
    - 类的方法:允许对进行操作的方法 (行为)

举例：
- 人类设计,只关心3样东西: 
    - 事物名称(类名):人(Person)
    - 属性:身高(height)、年龄(age)
    - 方法(行为/功能):跑(run)、打架(fight)
- 狗类的设计
    - 类名:狗(Dog)
    - 属性:品种 、毛色、性别、名字、 腿儿的数量
    - 方法(行为/功能):叫 、跑、咬人、吃、摇尾巴

6.类的抽象

如何把日常生活中的事物抽象成程序中的类?

拥有相同(或者类似)属性和行为的对象都可以抽像出一个类

方法:一般名词都是类(名词提炼法) 
- 坦克发射3颗炮弹轰掉了2架飞机
    - 坦克--》可以抽象成 类 
    - 炮弹--》可以抽象成类
    - 飞机-》可以抽象成类 
- 小明在公车上牵着一条叼着热狗的狗
    - 小明--》 人类
    - 公车--》 交通工具类 
    - 热狗--》 食物类 
    - 狗--》 狗类 
    
## 6.3.定义类

定义一个类，格式如下：

```
class 类名:
    方法列表
```
demo：定义一个Car类

```
# 定义类
class Car:
    # 方法
    def getCarInfo(self):
        print('车轮子个数:%d, 颜色%s'%(self.wheelNum, self.color))

    def move(self):
        print("车正在移动...")

```
说明：

- 定义类时有2种：新式类和经典类，上面的Car为经典类，如果是Car(object)则为新式类
- 类名 的命名规则按照"大驼峰"

## 6.4.创建对象

创建对象的格式为:

```
对象名 = 类名()
```
创建对象demo:

```
# 定义类
class Car:
    # 移动
    def move(self):
        print('车在奔跑...')

    # 鸣笛
    def toot(self):
        print("车在鸣笛...嘟嘟..")


# 创建一个对象，并用变量BMW来保存它的引用
BMW = Car()
BMW.color = '黑色'
BMW.wheelNum = 4 #轮子数量
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelNum)
```
**总结：**
- BMW = Car()，这样就产生了一个Car的实例对象，此时也可以通过实例对象BMW来访问属性或者方法
- 第一次使用BMW.color = '黑色'表示给BMW这个对象添加属性，如果后面再次出现BMW.color = xxx表示对属性进行修改
- BMW是一个对象，它拥有属性（数据）和方法（函数）
- 当创建一个对象时，就是用一个模子，来制造一个实物

## 6.5.__init__方法
1.使用方式

```
def 类名:
    #初始化函数，用来完成一些默认的设定
    def __init__():
        pass

```

2.__init__()方法的调用

```
# 定义汽车类
class Car:

    def __init__(self):
        self.wheelNum = 4
        self.color = '蓝色'

    def move(self):
        print('车在跑，目标:夏威夷')

# 创建对象
BMW = Car()

print('车的颜色为:%s'%BMW.color)
print('车轮胎数量为:%d'%BMW.wheelNum)
```

总结1
> 当创建Car对象后，在没有调用__init__()方法的前提下，BMW就默认拥有了2个属性wheelNum和color，原因是__init__()方法是在创建对象后，就立刻被默认调用了

总结2

- __init__()方法，在创建一个对象时默认被调用，不需要手动调用
- __init__(self)中，默认有1个参数名字为self，如果在创建对象时传递了2个实参，那么__init__(self)中出了self作为第一个形参外还需要2个形参，例如__init__(self,x,y)
- __init__(self)中的self参数，不需要开发者传递，python解释器会自动把当前的对象引用传递进去

## 6.6.应用:创建多个对象

- 根据上两节创建一个Car类
- 创建出多个汽车对象，比如BMW、AUDI等

## 6.7."魔法"方法
1.打印id()

如果把BMW使用print进行输出的话，会看到如下的信息

![打印id(](image/6.7.1.png)

即看到的是创建出来的BMW对象在内存中的地址

2.定义__str__()方法

```
class Car:

    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    def __str__(self):
        msg = "嘿。。。我的颜色是" + self.color + "我有" + int(self.wheelNum) + "个轮胎..."
        return msg

    def move(self):
        print('车在跑，目标:夏威夷')


BMW = Car(4, "白色")
print(BMW)
```
![定义__str__()方法](image/6.7.2.png)

**总结**

- 在python中方法名如果是__xxxx__()的，那么就有特殊的功能，因此叫做“魔法”方法
- 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据

## 6.8.self

理解self

看如下示例:

```
# 定义一个类
class Animal:

    # 方法
    def __init__(self, name):
        self.name = name

    def printName(self):
        print('名字为:%s'%self.name)

# 定义一个函数
def myPrint(animal):
    animal.printName()


dog1 = Animal('西西')
myPrint(dog1)

dog2 = Animal('北北')
myPrint(dog2)
```
运行结果:

![理解self](image/6.8.1.png)

**总结**

- 所谓的self，可以理解为自己
- 可以把self当做C++中类里面的this指针一样理解，就是对象自身的意思
- 某个对象调用其方法时，python解释器会把这个对象作为第一个参数传递给self，所以开发者只需要传递后面的参数即可

## 6.9.应用:烤地瓜
1.分析“烤地瓜”的属性和方法

示例属性如下:

- cookedLevel : 这是数字；0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，超过8表示已经烤成木炭了！我们的地瓜开始时时生的
- cookedString : 这是字符串；描述地瓜的生熟程度
- condiments : 这是地瓜的配料列表，比如番茄酱、芥末酱等

示例方法如下:

- cook() : 把地瓜烤一段时间
- addCondiments() : 给地瓜添加配料
- __init__() : 设置默认的属性
- __str__() : 让print的结果看起来更好一些

2.定义类，并且定义__init__()方法

```
#定义`地瓜`类
class SweetPotato:
    '这是烤地瓜的类'

    #定义初始化方法
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []
```

3.添加"烤地瓜"方法

```
    #烤地瓜方法
    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = "烤成灰了"
        elif self.cookedLevel > 5:
            self.cookedString = "烤好了"    
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"
```

4.基本的功能已经有了一部分，赶紧测试一下

把上面2块代码合并为一个程序后，在代码的下面添加以下代码进行测试

```
mySweetPotato = SweetPotato()
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiments)
```
完整的代码为:

```
class SweetPotato:
    '这是烤地瓜的类'

    #定义初始化方法
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

        #烤地瓜方法
    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = "烤成灰了"
        elif self.cookedLevel > 5:
            self.cookedString = "烤好了"    
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

# 用来进行测试
mySweetPotato = SweetPotato()
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiments)
```
![地瓜](image/6.9.1.png)

5.测试cook方法是否好用

在上面的代码最后面添加如下代码:

```
print("------接下来要进行烤地瓜了-----")
mySweetPotato.cook(4) #烤4分钟
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
```
![地瓜](image/6.9.2.png)

6.定义addCondiments()方法和__str__()方法

```
    def __str__(self):
        msg = self.cookedString + " 地瓜"
        if len(self.condiments) > 0:
            msg = msg + "("
            for temp in self.condiments:
                msg = msg + temp + ", "
            msg = msg.strip(", ")

            msg = msg + ")"
        return msg

    def addCondiments(self, condiments):
        self.condiments.append(condiments)
```

7.再次测试

完整的代码如下:

```
class SweetPotato:
    "这是烤地瓜的类"

    #定义初始化方法
    def __init__(self):
        self.cookedLevel = 0
        self.cookedString = "生的"
        self.condiments = []

    #定制print时的显示内容
    def __str__(self):
        msg = self.cookedString + " 地瓜"
        if len(self.condiments) > 0:
            msg = msg + "("

            for temp in self.condiments:
                msg = msg + temp + ", "
            msg = msg.strip(", ")

            msg = msg + ")"
        return msg

    #烤地瓜方法
    def cook(self, time):
        self.cookedLevel += time
        if self.cookedLevel > 8:
            self.cookedString = "烤成灰了"
        elif self.cookedLevel > 5:
            self.cookedString = "烤好了"    
        elif self.cookedLevel > 3:
            self.cookedString = "半生不熟"
        else:
            self.cookedString = "生的"

    #添加配料
    def addCondiments(self, condiments):
        self.condiments.append(condiments)

# 用来进行测试
mySweetPotato = SweetPotato()
print("------有了一个地瓜，还没有烤-----")
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiments)
print("------接下来要进行烤地瓜了-----")
print("------地瓜经烤了4分钟-----")
mySweetPotato.cook(4) #烤4分钟
print(mySweetPotato)
print("------地瓜又经烤了3分钟-----")
mySweetPotato.cook(3) #又烤了3分钟
print(mySweetPotato)
print("------接下来要添加配料-番茄酱------")
mySweetPotato.addCondiments("番茄酱")
print(mySweetPotato)
print("------地瓜又经烤了5分钟-----")
mySweetPotato.cook(5) #又烤了5分钟
print(mySweetPotato)
print("------接下来要添加配料-芥末酱------")
mySweetPotato.addCondiments("芥末酱")
print(mySweetPotato)
```
![地瓜](image/6.9.3.png)

## 6.10.隐藏数据
## 6.11.应用:存放家具