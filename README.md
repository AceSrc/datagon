# Datagon -- The combination of Doragon and DataGenerator O(∩_∩)o~

Datagon是一个通用型数据生成器. ~~极其不靠谱~~

~~目前极多bug以及错误提示不清不楚~~

## 安装说明

请预装python和setuptools库

使用
```
python setup.py install
```
即可安装

## 命令使用说明

```
datagon <input-file> [outpu-file]
```

若未指定输出文件, 则结果输出至控制台.

## 描述文件说明

命令中的input-file是对数据输出格式的描述文件. 

目前以支持的语法有:

### 整数

可使用直接使用数字来代表一个整数
```
123 -123 233
```

也可以使用区间来表示取值范围, 生成数据时会等概率生成区间内的整数
```
(1, 10) (1, 10] [1, 10) [1, 10]
```
其中()和[]表示区间的开闭

注意整数并不会直接输出到生成结果中, 必须使用print函数才能将其输出, 比如
```
print((0, 233])
```
将随机输出一个1到233的整数

### 变量
变量可以为任意小写字母组成的字符串, 可以进行赋值和引用
```
set(num, [1, 100])
print(num)
```

### 函数
函数必须后接(), 其中放置参数. 

目前支持的函数有:
* permutation(n): 输出一个长度n的随机排列
* weight(n, interval): 输出一个长度为n的权值数组, 其取值区间为interval
* add(a, b), sub(a, b), mul(a, b): 进行整数间的加减乘
* repeat(n, param1, param2...): 重复输出n行 每行的格式由param1 param2..

### 格式控制
默认描述文件中遇到'\n', 输出结果就会进行换行, 但若在行末添加字符#, 可以取消当前的换行.

主要作用于仅有变量赋值的行中, 使其不会输出空行. 比如
```
num = 233
print(num)
```
会输出成
```

233
```

而
```
num = 233#
print(num)
```
会输出成
```
233
```

## 使用例子

```
set(num, (0, 100])#
permutation(num)
```
会输出一个长度在1到100的排列

```
set(numa, (0, 100])#
set(numb, add(numa, (0, 100]))#
print(numa)
print(numb)
```
会输出两个整数, 其中num2一定大于num1

```
set(n, (0, 20)) set(m, (0, 20))#
print(n) print(m)
repeat(m, print([1, n]), print([1, n]), print((0, 100))
```
可以生成一个图(可能有重边, 也可能不连通)


## TO-DO List

* 实数支持
* 字符串支持
* 图的生成: 树, DAG, 无向图, 有向图, 正权图....
* 逻辑控制: 自定义函数
* 能够生成特殊数据和极端数据
* 提供对拍功能
...

