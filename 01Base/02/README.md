# 2.判断语句和循环语句

## 2.1 if-else

if-else的使用格式

```
    if 条件:
        满足条件时要做的事情1
        满足条件时要做的事情2
        满足条件时要做的事情3
        ...(省略)...
    else:
        不满足条件时要做的事情1
        不满足条件时要做的事情2
        不满足条件时要做的事情3
        ...(省略)...
```
demo1

```
    chePiao = 1 # 用1代表有车票，0代表没有车票
    if chePiao == 1:
        print("有车票，可以上火车")
        print("终于可以见到Ta了，美滋滋~~~")
    else:
        print("没有车票，不能上车")
        print("亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~")
```
结果1：有车票的情况

```
    有车票，可以上火车
    终于可以见到Ta了，美滋滋~~~
```
结果2：没有车票的情况

```
    没有车票，不能上课
    亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~
```


## 2.2 elif

- elif的功能

elif的使用格式如下:
```
    if xxx1:
        事情1
    elif xxx2:
        事情2
    elif xxx3:
        事情3

```

说明:

```
- 当xxx1满足时，执行事情1，然后整个if结束
- 当xxx1不满足时，那么判断xxx2，如果xxx2满足，则执行事情2，然后整个if结束
- 当xxx1不满足时，xxx2也不满足，如果xxx3满足，则执行事情3，然后整个if结束
```
demo:

```
    score = 77

    if score>=90 and score<=100:
        print('本次考试，等级为A')
    elif score>=80 and score<90:
        print('本次考试，等级为B')
    elif score>=70 and score<80:
        print('本次考试，等级为C')
    elif score>=60 and score<70:
        print('本次考试，等级为D')
    elif score>=0 and score<60:
        print('本次考试，等级为E')
```


- 注意点
    - elif必须和if一起使用，否则出错
    - 可以和else一起使用
```
   if 性别为男性:
       输出男性的特征
       ...
   elif 性别为女性:
       输出女性的特征
       ...
   else:
       第三种性别的特征
       ...
```
    说明:
        - 当 “性别为男性” 满足时，执行 “输出男性的特征”的相关代码
        - 当 “性别为男性” 不满足时，如果 “性别为女性”满足，则执行 “输出女性的特征”的相关代码
        - 当 “性别为男性” 不满足，“性别为女性”也不满足，那么久默认执行else后面的代码，即 “第三种性别的特征”相关代码

## 2.3 if嵌套

- if嵌套的格式
```
    if 条件1:

        满足条件1 做的事情1
        满足条件1 做的事情2
        ...(省略)...

        if 条件2:
            满足条件2 做的事情1
            满足条件2 做的事情2
            ...(省略)...
```
说明
    
    - 外层的if判断，也可以是if-else
    - 内层的if判断，也可以是if-else
    - 根据实际开发的情况，进行选择
    
- if嵌套的应用

demo：
```
    chePiao = 1     # 用1代表有车票，0代表没有车票
    daoLenght = 9     # 刀子的长度，单位为cm

    if chePiao == 1:
        print("有车票，可以进站")
        if daoLenght < 10:
            print("通过安检")
            print("终于可以见到Ta了，美滋滋~~~")
        else:
            print("没有通过安检")
            print("刀子的长度超过规定，等待警察处理...")
    else:
        print("没有车票，不能进站")
        print("亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~")
```
结果1：chePiao = 1;daoLenght = 9
```
    有车票，可以进站
    通过安检
    终于可以见到Ta了，美滋滋~~~
```
结果2：chePiao = 1;daoLenght = 20
```
    有车票，可以进站
    没有通过安检
    刀子的长度超过规定，等待警察处理...
```
结果3：chePiao = 0;daoLenght = 9
```
    没有车票，不能进站
    亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~
```
结果4：chePiao = 0;daoLenght = 20
```
    没有车票，不能进站
    亲爱的，那就下次见了，一票难求啊~~~~(>_<)~~~~
```

## 2.4 if应用:猜拳游戏

参考代码

```
    import random

    player = input('请输入：剪刀(0)  石头(1)  布(2):')

    player = int(player)

    computer = random.randint(0,2)

    # 用来进行测试
    #print('player=%d,computer=%d',(player,computer))

    if ((player == 0) and (computer == 2)) or ((player ==1) and (computer == 0)) or ((player == 2) and (computer == 1)):
        print('获胜，哈哈，你太厉害了')
    elif player == computer:
        print('平局，要不再来一局')
    else:
        print('输了，不要走，洗洗手接着来，决战到天亮')
```


## 2.5 循环语句介绍

- 软件开发中循环的使用场景

    跟媳妇承认错误，说一万遍"媳妇儿，我错了"
```
    print("媳妇儿，我错了")
    print("媳妇儿，我错了")
    print("媳妇儿，我错了")
    ...(还有99997遍)...
```
使用循环语句一句话搞定

```
i = 0
   while i<10000:
    print("媳妇儿，我错了")
    i+=1
```

- 小总结
    - 一般情况下，需要多次重复执行的代码，都可以用循环的方式来完成
    - 循环不是必须要使用的，但是为了提高代码的重复使用率，所以有经验的开发者都会采用循环


## 2.6 while循环

while循环的格式

```
    while 条件:
        条件满足时，做的事情1
        条件满足时，做的事情2
        条件满足时，做的事情3
        ...(省略)...
```
demo

```
  i = 0
    while i<5:
        print("当前是第%d次执行循环"%(i+1))
        print("i=%d"%i)
        i+=1
```
结果:

```
    当前是第1次执行循环
    i=0
    当前是第2次执行循环
    i=1
    当前是第3次执行循环
    i=2
    当前是第4次执行循环
    i=3
    当前是第5次执行循环
    i=4
```

## 2.7 while循环应用
- 计算1~100的累积和（包含1和100）
    
参考代码如下:
    
```
#encoding=utf-8

i = 1
sum = 0
while i<=100:
    sum = sum + i
    i += 1

print("1~100的累积和为:%d"%sum)
```

- 计算1~100之间偶数的累积和（包含1和100）

参考代码如下:

```
#encoding=utf-8

i = 1
sum = 0
while i<=100:
    if i%2 == 0:
        sum = sum + i
    i+=1

print("1~100的累积和为:%d"%sum)
```


## 2.8 while循环的嵌套以及应用

- while嵌套的格式

```
    while 条件1:

        条件1满足时，做的事情1
        条件1满足时，做的事情2
        条件1满足时，做的事情3
        ...(省略)...

        while 条件2:
            条件2满足时，做的事情1
            条件2满足时，做的事情2
            条件2满足时，做的事情3
            ...(省略)...

```

- while嵌套应用一

要求：打印如下图形：

```
    *
    * *
    * * *
    * * * *
    * * * * *

```
参考代码：

```
    i = 1
    while i<=5:

        j = 1
        while j<=i:
            print("* ",end='')
            j+=1

        print("\n")
        i+=1
```


- while嵌套应用二：九九乘法表

参考代码：

```
    i = 1
    while i<=9:
        j=1
        while j<=i:
            print("%d*%d=%-2d "%(j,i,i*j),end='')
            j+=1
        print('\n')
        i+=1
```

## 2.9 for循环

- for循环的格式

```
    for 临时变量 in 列表或者字符串等:
        循环满足条件时执行的代码
    else:
        循环不满足条件时执行的代码
```

- demo1

```
    name = 'dongGe'

    for x in name:
        print(x)
```

- demo2

```
    name = ''

    for x in name:
        print(x)
    else:
        print("没有数据")
```

## 2.10 break和continue
1.break

- 1)for循环

普通的循环示例如下：
```
  name = 'dongGe'

  for x in name:
      print('----')
      print(x)
``` 
带有break的循环示例如下:
```
  name = 'dongGe'

  for x in name:
      print('----')
      if x == 'g': 
          break
      print(x)
```

- 2)while循环
 
普通的循环示例如下：
```
  i = 0

  while i<10:
      i = i+1
      print('----')
      print(i)
```

带有break的循环示例如下:
```
  i = 0

  while i<10:
      i = i+1
      print('----')
      if i==5:
          break
      print(i)
```
**小总结:**
break的作用：用来结束整个循环

2.continue

- 1)for循环

带有continue的循环示例如下:

```
  name = 'dongGe'

  for x in name:
      print('----')
      if x == 'g': 
          continue
      print(x)
```

- 2)while循环

带有continue的循环示例如下:
```
  i = 0

  while i<10:
      i = i+1
      print('----')
      if i==5:
          continue
      print(i)

```
**小总结:**
continue的作用：用来结束本次循环，紧接着执行下一次的循环

3.注意点

    - break/continue只能用在循环中，除此以外不能单独使用
    - break/continue在嵌套循环中，只对最近的一层循环起作用

## 2.11 总结
- if往往用来对条件是否满足进行判断
- if有4中基本的使用方法：
    - 1.基本方法
        ```
            if 条件:
             满足时做的事情
        ```
    - 2.满足与否执行不同的事情
        ```
            if 条件:
                满足时做的事情
            else:
                不满足时做的事情
        ```
    - 3.多个条件的判断
```
    if 条件:
        满足时做的事情
    elif 条件2:
        满足条件2时做的事情
    elif 条件3:
        满足条件3时做的事情
    else:
        条件都不满足时做的事情
```
    - 4.嵌套
```
    if 条件:
        满足时做的事情

        这里还可以放入其他任何形式的if判断语句
```

- while循环一般通过数值是否满足来确定循环的条件

```
      i = 0
      while i<10:
          print("hello")
          i+=1
```

- for循环一般是对能保存多个数据的变量，进行便利
```
      name = 'dongGe'

      for x in name:
          print(x)
```
    
- if、while、for等其他语句可以随意组合，这样往往就完成了复杂的功能