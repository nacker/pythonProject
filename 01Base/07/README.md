# 7.面向对象2

## 7.1.应用
1. 人
    - 属
        - 姓名
        - 血量
        - 持有的枪
    - 方法
        - 安子弹
        - 安弹夹
        - 拿枪（持有抢）
        - 开枪
2. 子弹类
    - 属性
        - 杀伤力
    - 方法
        - 伤害敌人(让敌人掉血)
3. 弹夹类
    - 属性
        - 容量（子弹存储的最大值）
        - 当前保存的子弹
    - 方法
        - 保存子弹（安装子弹的时候）
        - 弹出子弹（开枪的时候）
4. 枪类
    - 属性
        - 弹夹（默认没有弹夹，需要安装）
    - 方法
        - 连接弹夹（保存弹夹）
        - 射子弹

参考代码

```
#人类
class Ren:
    def __init__(self,name):
        self.name = name
        self.xue = 100
        self.qiang = None

    def __str__(self):
        return self.name + "剩余血量为:" + str(self.xue)

    def anzidan(self,danjia,zidan):
        danjia.baocunzidan(zidan)

    def andanjia(self,qiang,danjia):
        qiang.lianjiedanjia(danjia)

    def naqiang(self,qiang):
        self.qiang = qiang

    def kaiqiang(self,diren):
        self.qiang.she(diren)

    def diaoxue(self,shashangli):
        self.xue -= shashangli

#弹夹类
class Danjia:
    def __init__(self, rongliang):
        self.rongliang = rongliang
        self.rongnaList = []

    def __str__(self):
        return "弹夹当前的子弹数量为:" + str(len(self.rongnaList)) + "/" + str(self.rongliang)

    def baocunzidan(self,zidan):
        if len(self.rongnaList) < self.rongliang:
            self.rongnaList.append(zidan)

    def chuzidan(self):
        #判断当前弹夹中是否还有子弹
        if len(self.rongnaList) > 0:
            #获取最后压入到单间中的子弹
            zidan = self.rongnaList[-1]
            self.rongnaList.pop()
            return zidan
        else:
            return None

#子弹类
class Zidan:
    def __init__(self,shashangli):
        self.shashangli = shashangli

    def shanghai(self,diren):
        diren.diaoxue(self.shashangli)

#枪类
class Qiang:
    def __init__(self):
        self.danjia = None

    def __str__(self):
        if self.danjia:
            return "枪当前有弹夹"
        else:
            return "枪没有弹夹"

    def lianjiedanjia(self,danjia):
        if not self.danjia:
            self.danjia = danjia


    def she(self,diren):
        zidan = self.danjia.chuzidan()
        if zidan:
            zidan.shanghai(diren)
        else:
            print("没有子弹了，放了空枪....")


#创建一个人对象
laowang = Ren("老王")

#创建一个弹夹
danjia = Danjia(20)
print(danjia)

#循环的方式创建一颗子弹，然后让老王把这颗子弹压入到弹夹中
i=0
while i<5:
    zidan = Zidan(5)
    laowang.anzidan(danjia,zidan)
    i+=1
#测试一下，安装完子弹后，弹夹中的信息
print(danjia)

#创建一个枪对象
qiang = Qiang()
print(qiang)
#让老王，把弹夹连接到枪中
laowang.andanjia(qiang,danjia)
print(qiang)


#创建一个敌人
diren = Ren("敌人")
print(diren)

#让老王拿起枪
laowang.naqiang(qiang)

#老王开枪射敌人
laowang.kaiqiang(diren)
print(diren)
print(danjia)

laowang.kaiqiang(diren)
print(diren)
print(danjia)
```

## 7.2.保护对象的属性

如果有一个对象，当需要对其进行修改属性时，有2种方法

- 对象名.属性名 = 数据 ---->直接修改
- 对象名.方法名() ---->间接修改

为了更好的保存属性安全，即不能随意修改，一般的处理方式为

- 将属性定义为私有属性
- 添加一个可以调用的方法，供调用

```
class People(object):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("error:名字长度需要大于或者等于5")

xiaoming = People("dongGe")
print(xiaoming.__name)
```

![image description](Image/7.2.1.png)

```
class People(object):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("error:名字长度需要大于或者等于5")

xiaoming = People("dongGe")

xiaoming.setName("wanger")
print(xiaoming.getName())

xiaoming.setName("lisi")
print(xiaoming.getName())
```

![image description](Image/7.2.2.png)

**总结**

- Python中没有像C++中public和private这些关键字来区别公有属性和私有属性
- 它是以属性命名方式来区分，如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）。

## 7.3.__del__方法
创建对象后，python解释器默认调用__init__()方法；

当删除一个对象时，python解释器也会默认调用一个方法，这个方法为__del__()方法

```
import time
class Animal(object):

    # 初始化方法
    # 创建完对象后会自动被调用
    def __init__(self, name):
        print('__init__方法被调用')
        self.__name = name


    # 析构方法
    # 当对象被删除时，会自动被调用
    def __del__(self):
        print("__del__方法被调用")
        print("%s对象马上被干掉了..."%self.__name)

# 创建对象
dog = Animal("哈皮狗")

# 删除对象
del dog


cat = Animal("波斯猫")
cat2 = cat
cat3 = cat

print("---马上 删除cat对象")
del cat
print("---马上 删除cat2对象")
del cat2
print("---马上 删除cat3对象")
del cat3

print("程序2秒钟后结束")
time.sleep(2)
```
![image description](Image/7.3.1.png)

**总结**

- 当有1个变量保存了对象的引用时，此对象的引用计数就会加1
- 当使用del删除变量指向的对象时，如果对象的引用计数不会1，比如3，那么此时只会让这个引用计数减1，即变为2，当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除

## 7.4.单继承
## 7.5.多继承
## 7.6.重写父类方法与调用父类方法
## 7.7.多态
## 7.9.静态方法和类方法