def f(x):
    return x**2

@profile
def integrate(f, a, b, N):
    s = 0
    dx = (b-a)/N
    for i in xrange(N):
        s += f(a+i*dx)
    return s * dx

def integrate_f_with_functional_tools(a, b, N):
    dx = (float(b)-a)/N
    return sum(map(f, ((a+y*dx) for y in xrange(N))))*dx
