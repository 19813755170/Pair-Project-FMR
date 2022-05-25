from random import randint
class polynomial:
    x=y=z=0
    num=0
    def getresult(self):
        numcount=0
        all =["+","-","*","/"]
        while numcount<num:
            x=randint(0,100)
            y=randint(0,100)
            z=randint(0,100)
            result=str(x)+all[randint(0,3)]+str(y)+all[randint(0,3)]+str(z)
            if(eval(result)>0):
                print(result,"=",eval(result))
            else:
                continue
            numcount+=1
#曾龙王子编写部分
    def __init__(self,num):
        self.num=num
print("请输入需要生成的题目数量")
num=input()
num=int(num)
x=polynomial(num)
x.getresult()
#冯梦然编写部分