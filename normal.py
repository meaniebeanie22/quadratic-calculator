import cmath

#inputs
a = float(input('enter a: '))
b = float(input('enter b: '))
c = float(input('enter c: '))

#dealing with discriminant
disc = b**2 - 4*a*c
discsqrt = cmath.sqrt(disc)
if disc != 0:
    #two imaginary roots
    print('r1:', (-b - discsqrt)/(2*a))
    print('r2:', (-b + discsqrt)/(2*a))
else:
    #one real root
    print('r:', -b/(2*a))