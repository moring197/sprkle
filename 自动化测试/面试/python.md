1.字符串拼接  ，字典拼接

```python
#字符串拼接方法
str='python'
print(list(str))
#1.变量,用逗号
s='test'
print(str,s)
#2.format
print('{},{}'.format('python','list'))
#3.join(seq)方法  将序列中的元素以指定的字符连接生成一个新的字符串
a=''
b=['py','thon']
print(a.join(b))

print('str %s' % 'shanghai')
#4.f-string方法
print('f-string拼接：' f'{str}{s}')
#5.+
#6.*
```

字典合并



2.字符串转为列表

```python
str='python'
l=list(str)
```

3.列表去重

4.self的含义

self指的是类示例对象本身（不是类本身），self只有在类的方法中才会有，python中self不是关键字，约定成俗为self

5.break,continue,pass区别

break跳出本层循环，不再执行

continue跳出本次循环，执行下次循环

pass：不做任何事情，只起到占位的作用

6.单引号、双引号、三引号的区别

7.*，**传参时的区别

*，表示接受的参数作为元组来处理

**，表示接收的参数作为字典处理

8.装饰器顺序