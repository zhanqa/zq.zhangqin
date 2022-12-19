from random import randint
# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength  #生命值

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength



# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')

# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
******************************************************************
*******************           游戏开始             ****************
******************************************************************

'''
)

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification,end='')
# time.sleep(10)
for i in range(20):
    print('\n')

#判断战士是否阵亡
def save(warrior):
    if (warrior.strength<0):
        return True
    else:
        return False

#修养函数
def hel(w_name):
    while (True):
        selects = eval(input("请选择是否要补养" + w_name + "(1为补养2为不补养)："))
        if (selects > 2):
            print("您输入有误，请重新输入！")
        else:
            if (selects == 1):
                s_num = eval(input("请输入您要补养的生命值（1灵石1个生命值）："))
                player.warriors[w_name].healing(s_num)
                player.stoneNumber -= s_num
                break
            else:
                break

#创一个游戏玩家
player=Player(1000)

# 开始雇佣战士
while(True):
    ar_num=list(input("请输入你要雇佣的战士数量(弓箭兵):"))
    if ' ' in ar_num:
        print("您的输入有误，请重新输入！")
    else:

        archer_num=int(ar_num[0])
        for i in range(archer_num):
            name=input("请输入您的第"+str(i+1)+"个弓箭兵的名字:")
            Ar=Archer(name)
            player.stoneNumber-=Ar.price
            player.warriors[str(i+1)+"号弓箭手"]=Ar
        break

while(True):
    ax_num=list(input("请输入你要雇佣的战士数量(斧头兵):"))
    if ' ' in ax_num:
        print("您的输入有误，请重新输入！")
    else:
        axeman_num = int(ax_num[0])
        for i in range(axeman_num):
            name = input("请输入您的第" + str(i+1) + "个斧头兵的名字:")
            Ax = Axeman(name)
            player.stoneNumber -= Ax.price
            player.warriors[str(i+1) + "号斧头手"] = Ax
        break


for i in range(len(forestList)):
    print("==============开始通过第",str(i+1),"座森林！=================")
    while (True):
        if (len(player.warriors)==0):
            print("您没有战士了，游戏失败！")
            break
        w_name = input("请派出您的第{0}个战士(战士名字)：".format(str(i + 1)))
        if w_name not in player.warriors:
            print("您没有该战士，请重新输入！")
        else:
            wr=player.warriors[w_name]
            # 开始战斗
            wr.fightWithMonster(forestList[i].monster)
            print("==========这座森林的妖怪是", forestList[i].monster.typeName, "您的战士派对了吗？=========")
            while(save(wr)):
                print(w_name, "已经阵亡！")
                del player.warriors[w_name]
                w2_name = input("请重新派出一个战士打败妖怪:")
                if w2_name not in player.warriors:
                    print("您没有该战士，请重新输入！")
                else:
                    wr2 = player.warriors[w2_name]
                    # 开始战斗
                    wr2.fightWithMonster(forestList[i].monster)
                    if(wr2.strength<0):
                        print(w2_name, "已经阵亡！")
                        del player.warriors[w2_name]
                    else:
                        hel(w2_name)
                    break
            else:
                hel(w_name)
            break

print("您最后剩余{0}个灵石".format(player.stoneNumber))





