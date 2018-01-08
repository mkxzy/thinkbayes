from thinkbayes import Pmf

pmf = Pmf()
pmf.Set('Bow1', 0.5)
pmf.Set('Bow2', 0.5)
pmf.Mult('Bow1', 0.75)
pmf.Mult('Bow2', 0.5)
pmf.Normalize()
t = pmf.Prob('Bow1')
print(t)
