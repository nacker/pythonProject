# 8.面向对象3、异常、模块

## 8.1.练习:设计类
1.设计一个卖车的4S店，该怎样做呢？

```
# 定义车类
class Car(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")

# 定义一个销售车的店类
class CarStore(object):

    def order(self):
        self.car = Car() #找一辆车
        self.car.move()
        self.car.stop()
```
说明

> 上面的4s店，只能销售那一种类型的车
> 
> 如果这个是个销售北京现代品牌的车，比如伊兰特、索纳塔等，该怎样做呢？

2.设计一个卖北京现代车的4S店

```
# 定义伊兰特车类
class YilanteCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")

# 定义索纳塔车类
class SuonataCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")

# 定义一个销售北京现代车的店类
class CarStore(object):

    def order(self, typeName):
        #根据客户的不同要求，生成不同的类型的车
        if typeName == "伊兰特":
            car = YilanteCar()
        elif typeName == "索纳塔":
            car = SuonataCar()
        return car
```

## 8.2.工厂模式
- 1.简单工厂模式
    - 1.使用函数实现
        ```
            # 定义伊兰特车类
            class YilanteCar(object):

            # 定义车的方法
            def move(self):
                print("---车在移动---")

            def stop(self):
                print("---停车---")

            # 定义索纳塔车类
            class SuonataCar(object):

             # 定义车的方法
            def move(self):
                print("---车在移动---")

            def stop(self):
                 print("---停车---")

            # 用来生成具体的对象
                def createCar(typeName):
                    if typeName == "伊兰特":
                         car = YilanteCar()
                    elif typeName == "索纳塔":
                        car = SuonataCar()
                        return car

            # 定义一个销售北京现代车的店类
                class CarStore(object):

            def order(self, typeName):
            # 让工厂根据类型，生产一辆汽车
                car = createCar(typeName)
                return car
        ```
    - 2.使用类来实现
    
```
# 定义伊兰特车类
class YilanteCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")

# 定义索纳塔车类
class SuonataCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")

# 定义一个生产汽车的工厂，让其根据具体的订单生产车
class CarFactory(object):

    def createCar(self,typeName):
        if typeName == "伊兰特":
            car = YilanteCar()
        elif typeName == "索纳塔":
            car = SuonataCar()

        return car

# 定义一个销售北京现代车的店类
class CarStore(object):

    def __init__(self):
        #设置4s店的指定生产汽车的工厂
        self.carFactory = CarFactory()

    def order(self, typeName):
        # 让工厂根据类型，生产一辆汽车
        car = self.carFactory.createCar(typeName)
        return car
```

> 咋一看来，好像只是把生产环节重新创建了一个类，这确实比较像是一种编程习惯，此种解决方式被称作简单工厂模式
> 
> 工厂函数、工厂类对具体的生成环节进行了封装，这样有利于代码的后需扩展，即把功能划分的更具体，4s店只负责销售，汽车厂只负责制造

2.工厂方法模式

多种品牌的汽车4S店

当买车时，有很多种品牌可以选择，比如北京现代、别克、凯迪拉克、特斯拉等，那么此时该怎样进行设计呢？

```
# 定义一个基本的4S店类
class CarStore(object):

    #仅仅是定义了有这个方法，并没有实现，具体功能，这个需要在子类中实现
    def createCar(self, typeName):
        pass

    def order(self, typeName):
        # 让工厂根据类型，生产一辆汽车
        self.car = self.createCar(typeName)
        self.car.move()
        self.car.stop()

# 定义一个北京现代4S店类
class XiandaiCarStore(CarStore):

    def createCar(self, typeName):
        self.carFactory = CarFactory()
        return self.carFactory.createCar(typeName)


# 定义伊兰特车类
class YilanteCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")

# 定义索纳塔车类
class SuonataCar(object):

    # 定义车的方法
    def move(self):
        print("---车在移动---")

    def stop(self):
        print("---停车---")

# 定义一个生产汽车的工厂，让其根据具体得订单生产车
class CarFactory(object):

    def createCar(self,typeName):
        self.typeName = typeName
        if self.typeName == "伊兰特":
            self.car = YilanteCar()
        elif self.typeName == "索纳塔":
            self.car = SuonataCar()

        return self.car

suonata = XiandaiCarStore()
suonata.order("索纳塔")
```

最后来看看工厂方法模式的定义

> 定义了一个创建对象的接口(可以理解为函数)，但由子类决定要实例化的类是哪一个，工厂方法模式让类的实例化推迟到子类，抽象的CarStore提供了一个创建对象的方法createCar，也叫作工厂方法。
> 
> 子类真正实现这个createCar方法创建出具体产品。 创建者类不需要直到实际创建的产品是哪一个，选择了使用了哪个子类，自然也就决定了实际创建的产品是什么。
> 
    
## 8.3.__new__方法
__new__和__init__的作用

```
class A(object):
    def __init__(self):
        print("这是 init 方法")

    def __new__(cls):
        print("这是 new 方法")
        return object.__new__(cls)

A()
```
总结

- __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供

- __new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例

- __init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

- 我们可以将类比作制造商，__new__方法就是前期的原材料购买环节，__init__方法就是在有原材料的基础上，加工，初始化商品环节

注意点

![image description](Image/8.3.1.png)

## 8.4.单利模式
## 8.5.异常介绍
## 8.6.捕获异常
## 8.7.异常的传递
## 8.8.抛出自定义的异常
## 8.9.异常处理中抛出异常
## 8.10.模块介绍
## 8.11.模块制作
## 8.12.模块中的__all__
## 8.13.python中的包
## 8.14.模块发布
## 9.15.模块安装、使用