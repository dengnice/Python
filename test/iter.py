index = 0
d = {'a':1, 'b':'test','c':3}
for key in d.items():
    print(key)
for k,v in d.items():
    print(v)
    print(k)
index+=1            #python不能用++自增
print('--------------------------%d'% index)
for k in d.items():
    print(k)
    print(k)

index+=1
print('--------------------------%d'% index)
#generator的作用，如果list过大，而只需要前几个元素，可以一边循环一边计算的机制，可以节省大量空间。

#generator和List的区别，在于一个是[ ]一个是( )，有些list表达不了的，可以用generator，比如斐波那契数列，list无法表达，可以用generator边计算边打印
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b #变为generator的重要一步,相当于把b加入到generator中
        a,b = b, a + b
        n += 1
    return 'done'


f = fib(10)
for i in f:
    print(i)
print (type(f))
index+=1
print('--------------------------%d'% index)

def odd():
    yield(1)
    yield(3)
    yield(5)
    yield(7)
    yield(8)

o = odd()
for i in o:
    print(i)
    
