#本程序用于3D或者2D空间中光线的遮挡情况

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 点是否在边同一边
def isPointinSameSide(pa, pb, pc, p0):
    ab = [pb[0] - pa[0], pb[1] - pa[1], pb[2] - pa[2]]
    ac = [pc[0] - pa[0], pc[1] - pa[1], pc[2] - pa[2]]
    a0 = [p0[0] - pa[0], p0[1] - pa[1], p0[2] - pa[2]]

    vabac = [ab[1] * ac[2] - ab[2] * ac[1], ab[2] * ac[0] -
             ab[0] * ac[2], ab[0] * ac[1] - ab[1] * ac[0]]
    vaba0 = [ab[1] * a0[2] - ab[2] * a0[1], ab[2] * a0[0] -
             ab[0] * a0[2], ab[0] * a0[1] - ab[1] * a0[0]]

    return (vabac[0] * vaba0[0] + vabac[1] * vaba0[1] + vabac[2] * vaba0[2]) >= 0

#单元体类
class element:
    def __init__(self,plight,pobject,paobstacle,pbobstacle,pcobstacle):
        self.pl=plight
        self.po=pobject
        self.pa=paobstacle
        self.pb=pbobstacle
        self.pc=pcobstacle

    #已知平面上三个点求平面法向量，返回值格式为[x,y,z]
    def calVerticalVector(self):
        A=np.array([[(self.pb[0]-self.pa[0]),(self.pb[1]-self.pa[1]),(self.pb[2]-self.pa[2])],
                    [(self.pc[0]-self.pa[0]),(self.pc[1]-self.pa[1]),(self.pc[2]-self.pa[2])],
                    [(self.pc[0]-self.pb[0]),(self.pc[1]-self.pb[1]),(self.pc[2]-self.pb[2])]])
        s, v, d = np.linalg.svd(A)
        return np.compress(v < 1e-10, d, axis=0)

    #连线是否和有限平面相交,True相交，False不相交
    def isIntersect(self, mode='3D'):

        if mode=='3D':#三维空间
            #平面法向量
            planevec=self.calVerticalVector()[0]
            #直线向量
            linevec=[(self.pl[0] - self.po[0]), (self.pl[1] - self.po[1]), (self.pl[2] - self.po[2])]

            if (linevec[0]*planevec[0]+linevec[1]*planevec[1]+linevec[2]*planevec[2])==0:
                return False
            else:
                #直线与无限平面的交点坐标
                #中间参数
                t= ((self.pa[0] - self.pl[0]) * planevec[0] + (self.pa[1] - self.pl[1]) * planevec[1] +
                    (self.pa[2] - self.pl[2]) * planevec[2]) / \
                   (linevec[0]*planevec[0]+linevec[1]*planevec[1]+linevec[2]*planevec[2])

                x0= self.pl[0] + linevec[0] * t
                y0= self.pl[1] + linevec[1] * t
                z0= self.pl[2] + linevec[2] * t
                p0=[x0,y0,z0]

                if (isPointinSameSide(self.pa, self.pb, self.pc, p0)) \
                        and (isPointinSameSide(self.pb, self.pc, self.pa, p0)) \
                        and (isPointinSameSide(self.pc, self.pa, self.pb, p0)):
                    return True
                else:
                    return False
        elif mode=='2D':#二维空间
            pass
        else:
            print('This mode can not be supported...')

#输出结果，输入[[x],[y],[z],[strength]]数据集
def resultPlot(dataset):
    X=dataset[0]
    Y=dataset[1]
    Z=dataset[2]
    # Strength=dataset[3]

    fig = plt.figure()
    ax = Axes3D(fig)
    # X = np.arange(-4, 4, 0.25)
    # Y = np.arange(-4, 4, 0.25)
    # X, Y = np.meshgrid(X, Y)
    # Z = np.sin(np.sqrt(X**2 + Y**2))

    # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1)

    plt.show()

#计算一个数据点集中在某一个垂直向量方向上点最大截面，返回组成这个截面点几个点
def calMaxCrossover(dataset,vector):
    pass


#拟化一个3D图形，得到离散点坐标，输出[[x],[y],[z]]数据集
def examSolid():
    X = np.arange(0,1,0.02)
    Y = np.arange(0,1,0.02)
    Z = 1-X-Y

    return [X,Y,Z]

#主程序
def mainRun():
    #定义光源
    lightPoint=[4,4,4]

    print('step1')

    #定义物体3维坐标
    pa=[3,0,0]
    pb=[0,3,0]
    pc=[0,0,3]

    print('step2')

    #遍历目标点
    X=[]
    Y=[]
    Z=[]
    lightstrength=[]

    print('step3')

    for x in np.arange(-10,10,1):
        for y in np.arange(-10,10,1):
            #获取此地坐标
            X.append(x)
            Y.append(y)
            Z.append(0)

            print('X=')
            print(X)
            print('Y=')
            print(Y)
            print('Z=')
            print(Z)

            #获取此地光强
            singleelement=element(lightPoint,[x,y,0],pa,pb,pc)
            if singleelement.isIntersect():
                lightstrength.append(0)
            else:
                lightstrength.append(100)
            print('strengh=')
            print(lightstrength)

    dataset=[X,Y,lightstrength]

    resultPlot(dataset)

mainRun()
