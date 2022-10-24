import cmath
from fractions import Fraction
import math

def gcd(a, b):
  """
  Returns the Greatest Common Divisor between `a` and `b`.
  """
  while b:
    a, b = b, a % b
  return a

def squarefactors(x):
    return [i for i in range(1,int(x)+1) if x%i==0 and math.sqrt(i)%1==0]

class surdob:
    def __init__(self, surd, mult=1):
        self.surd = surd
        self.mult = Fraction('1/1')

    def simplify(self):
        fac = squarefactors(self.surd)
        if fac != [1,self.surd]:
            self.surd = self.surd/fac[1]
            self.mult = self.mult*math.sqrt(fac[1])
        return self
    
    def __str__(self):
        if self.mult == 1 and self.surd == 1:
            return '1'
        elif self.mult == 1:
            return ('√'+str(self.surd))
        elif self.surd == 1:
            return str(self.mult)
        else:
            return str(self.mult) + '√' + str(self.surd)
    
    def __truediv__(self, other):
        surd = self.surd
        mult = self.mult

        return surdob(surd, mult/other)
    

#inputs
a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

#get disc
disc = b**2 - 4*a*c

if disc < 0:
    #imaginary numbers
    print('you goofed up - imaginary numbers not supported yet')
elif disc > 0:
    #real and needs surdification
    discsurd = surdob(b**2 - 4*a*c).simplify()
    print('Root A =', Fraction(-b/2*a), '+', discsurd/(2*a))
    print('Root B =', Fraction(-b/2*a), '-', discsurd/(2*a))

else:
    #disc = 0
    g = gcd(-b, 2*a)
    print('Root is:', Fraction(-b/(2*a)))

