# char to num
from functools import reduce
def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]
def cal(x, y):
    return x * 10 + y

print(reduce(cal, map(char2num, '13579')))

DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x,y: x * 10 + y, map(char2num, s))

print (str2int('4987654'))

#get all prime
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for i in primes():
    if i < 10:
        print(i)
    else :
        break


#如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure).
#用途1，当闭包执行完后，仍然能够保持住当前的运行环境。
#比如说，如果你希望函数的每次执行结果，都是基于这个函数上次的运行结果。
#用途2，闭包可以根据外部作用域的局部变量来得到不同的结果，这有点像一种类似配置功能的作用，我们可以修改外部的变量，
#闭包根据这个变量展现出不同的功能。比如有时我们需要对某些文件的特殊行进行分析，先要提取出这些特殊行。
def count():
    fs = []
    for i in range(1,4):
        def f():
            print('f func')
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1)
print(f1())
#print(f1(),f2(),f3())
