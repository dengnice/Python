print("hello")
#name =input()
#print (name)

a  = 100
if a >= 0:
    print (a)
    print (-a)

#tuple和list区别：
#tuple不能变，list可变，tuple小括号，但是tuple里面包含list的话，list可变，只是指向不可变

t = ('a', 'b', ['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'

print (t)


#字典
d = {'test':1, 'hello':2, 'ppp':3}
if('test' in d): #判断dict中是否存在test
    print (d['test']) #1
    
#如果key不存在，返回-2（自定义值）
print (d.get('te1st', -2)) # -2

#和list比较，dict有以下几个特点：

#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。

#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。

#集合，以list为参数，元素不会重复
print ("集合:")
s = set([1,1,1,1,2,3])
print (s) #{1,2,3}
s.add(4)
s.remove(1)

#集合的并和交
print ("集合交和并:")
s1 = set([1,2,3])
s2 = set([2,3,4])
print (s1 & s2) #{2,3}
print (s1 | s2) #{1,2,3,4}

t1 = set([1,1,2,2,(1,2),(1,2),(1,2,3)])
print (t1) #{(1, 2), 1, 2, (1, 2, 3)}

#强制类型转换
print (int(12.34)) #12

#函数 - 定义
print ("函数：")
def my_abx(x):
    if x>=0:
        return x
    else:
        return -x;

print (my_abx(-9))


def add_end(L=[]):#有个等号
    L.append("ed");
    return L

print (add_end([1,2]))

#可变参数:
    #1.list作为参数
    #2.*val
#1
def calc(num):
    sum = 0;
    for n in num:
        sum += n 
    return sum
print (calc([1,2,3]))

#2
def calc_sec(*num):
    sum = 0;
    for n in num:
        sum += n
    return sum
print (calc_sec(1,2,3))

#test
