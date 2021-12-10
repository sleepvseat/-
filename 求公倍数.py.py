'''
求最大公约数和公倍数
'''
'''
def gongYueshu(a,b):
    if a<b:
        (a, b) = (b, a)
    else:
        pass
    for x in range(b,0,-1):
        if a%x==0 and b%x==0:
            return x

d=gongYueshu(6,9)
print(d)
'''
'''
求公倍数
'''
#公倍数 列表赋值大于0的整数
l=[]
def zuixiaogonebeishu(l):
    sum = 1

    bigsum=None
    #找出最大值
    for x in range(0,len(l)):
        if l[0]>l[x]:
            pass
        else:
            c=l[0]
            l[0]=l[x]
            l[x]=c
    print('最大值%d'%l[0])

    for y in range(0,len(l)):

        sum*=l[y]
    print('直接公倍数%d'%sum)
    #找出最大数与直接公倍数之间适合的公倍数
    for z in range(l[0],sum+1):
        bb=None
        #公倍数测试值除以各个单项
        for g in range(0,len(l)):
            if z%l[g]!=0:
                bb=False
                break
            #测试值不通过跳出测试
            else:
                bb=True
                continue
            #测试值通过这一次，继续测试下一个值

        if bb==True:
            bigsum=z
            break
        #测试值测完了全部通过，这个值就是需要的

    return bigsum
#求列表中最小公倍数
kk=[1,1,1]
print(zuixiaogonebeishu(kk))


