#program Iteration
L = [32,15,343,-1]
tup = ()
def findMaxAndMin(L):
	curMin = 999999
	curMax = -99999
	for v in L:
		if v < curMin:
			curMin = v
		if v > curMax : 
			curMax = v
	print(curMin)
	print(curMax)
	tup = (curMin,curMax)
	return tup
tup = findMaxAndMin(L)
print(tup)
print(type(tup))

#program List
L = ['Hello','Test',18,'word','TE',None]
L2 = [s.lower() for s in L if isinstance(s, str)]
print(L2)


#program yanghui triangles
def triangles():
    initList = [1]
    while True:
        yield initList
        initList = [1 if n == 0 or n == len(initList) else initList[n-1] + initList[n] for n in range(len(initList) + 1)]
        #initList = [1] + [initList[n] + initList[n+1] for n in range(len(initList)-1)] + [1]

ge = triangles()

print (type(ge))
for i in range(6):
    print(next(ge))
