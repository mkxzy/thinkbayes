# _*_ coding: utf-8 _*_

from thinkbayes import Pmf

pmf = Pmf()
pmf.Set('Bow1', 0.5) #碗1的概率
pmf.Set('Bow2', 0.5) #碗2的概率
pmf.Mult('Bow1', 0.75) #碗1香草曲奇概率
pmf.Mult('Bow2', 0.5) #碗2香草曲奇概率
pmf.Normalize() #归一化
t = pmf.Prob('Bow1') #后验概率
print(t)
