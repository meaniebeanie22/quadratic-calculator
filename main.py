import math
#import surd

#inputs
a = float(input('enter a'))
b = float(input('enter b'))
c = float(input('enter c'))

#dealing with discriminant
disc = b**2 - 4*a*c
if disc < 0:
    #two imaginary roots
    disc = complex(0, )
elif disc > 0:
    #two real roots
    #surd
    pass
else:
    #one real root
    #surd
    pass