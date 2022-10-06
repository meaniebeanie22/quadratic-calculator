import cmath
import math

def gcd(a, b):
  """
  Returns the Greatest Common Divisor between `a` and `b`.
  """
  while b:
    a, b = b, a % b
  return a

def squarefactors(x):
    return [i for i in range(1,x+1) if x%i==0 and math.sqrt(i)%1==0]

class surdob:
    def __init__(self, surd, mult=1):
        self.surd = surd
        self.mult = mult

    def simplify(self):
        fac = squarefactors(self.surd).sort()
        if fac != [1,self.surd]:
            self.surd = self.surd/squarefactors[1]
            self.mult = self.mult*math.sqrt(squarefactors[1])
        return self
    
    def __str__(self):
        if self.mult == 1 and self.surd == 1:
            return '1'
        elif self.mult == 1:
            return '√'+str(self.surd)
        elif self.surd == 1:
            return str(self.mult)

    

#inputs
a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

#get disc
disc = b**2 - 4*a*c

if disc < 0:
    #imaginary numbers
    pass
if disc > 0:
    #real and needs surdification
    pass
else:
    #disc = 0
    g = gcd(-b, 2*a)
    print('Root is:', (-b/g), '/', (2*a)/g)

