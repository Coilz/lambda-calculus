I = lambda x: x
K = lambda x: lambda y: x
KI = K(I)

M = lambda f: f(f)
C = lambda f: lambda x: lambda y: f(y)(x)

T = K
F = KI
