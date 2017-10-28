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
1. find

检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1

```
mystr.find(str, start=0, end=len(mystr))
```

2. index

跟find()方法一样，只不过如果str不在 mystr中会报一个异常.

```
mystr.index(str, start=0, end=len(mystr)) 
```

3. count

返回 str在start和end之间 在 mystr里面出现的次数

```
mystr.count(str, start=0, end=len(mystr))
```

4. replace

把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

```
mystr.replace(str1, str2,  mystr.count(str1))
```
5. split

以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串

```
mystr.split(str=" ", 2) 
```

6. capitalize
7. title
8. startswith
9. endswith
10. lower
11. upper
12. ljust
13. rjust
14. center

## 3.6.列表介绍
## 3.7.列表的循环遍历
## 3.8.列表的常见操作
## 3.9.列表的嵌套
## 3.10.元组
## 3.11.字典介绍
## 3.12.字典的常见操作1
## 3.13.字典的常见操作2
## 3.14.字典的遍历
## 3.15.公共方法
## 3.16.引用

