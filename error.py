# -*- coding: utf-8 -*-
"""error_prop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gh6PhqS-5SGRNk1M1egNaenJ6vmpiLRA
"""

import sympy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sigfig as sf
from scipy.optimize import curve_fit
sympy.init_printing()
from IPython.display import display


def value_and_error(expr, **kwargs):
    variables = tuple(kwargs.keys())
    expr = sympy.parse_expr(expr)
    display(expr)
    print(sympy.latex(expr))
    x = tuple(v[0] for v in kwargs.values())
    c = tuple(v[1] for v in kwargs.values())
    index = [ np.any(c != 0) for c in c  ]
    symbols = sympy.symbols(variables)
    cov_symbols = sympy.symbols(tuple("\delta_" + k for k in variables), positive = True )
    symbols_np = np.asarray(symbols)
    cov_symbols_np = np.asarray(cov_symbols)
    
    expr2 =  sum((expr.diff(s)*c)** 2 for s, c in zip(symbols_np[index], cov_symbols_np[index])) 
    expr2 = expr2.simplify() # recommended for speed and accuracy
    stdev = sympy.simplify(sympy.sqrt(expr2))
    display(stdev)
    print(sympy.latex(stdev))
    
    fval = sympy.lambdify(symbols, expr)
    fcov = sympy.lambdify(symbols + cov_symbols, expr2)

   
    val = fval(*x)
    err = np.sqrt(fcov(*x, *c))
    #print(sf.round(val,err, notation = 'scientific'))
    return val, err


from scipy import odr

def least_squares_y(x,y,sy):
    def func(x,a,b):
      return a*x + b
    fit = curve_fit(func,x,y,sigma=sy, absolute_sigma= True)
    return (fit[0],np.sqrt(np.diag(fit[1])))
def least_squares_xy(x,y,dx,dy):
    def f(B, x):
      return B[0]*x + B[1]
    linear = odr.odrpack.Model(f)
    mydata = odr.odrpack.RealData(x, y, sx=dx, sy=dy)

    myodr = odr.odrpack.ODR(mydata, linear, beta0=[1., 2.])
    myoutput = myodr.run()
    return myoutput.beta,np.sqrt(np.diag(myoutput.cov_beta))



def round(x,dx):
  if dx == 0:
    return x
  else:
    return sf.round(x,dx)

def maketable(*args, transpose = False):
  
  args = np.asarray(args,dtype = tuple)
  data = args[:,1:3]
  #data = np.array([ [str(x) +" \pm "+ str(dx) for x,dx in zip( round_to_error(x,r1sd(dx)),r1sd(dx))] for x,dx in args[:,1:3] ]).T
  data = np.array([ [ round(x, dx) for x,dx in zip(x,dx)] for x,dx in args[:,1:3] ]).T
  if transpose: data = data.T
  df = pd.DataFrame(data, columns= [args[:,0]])
  return df, df.to_latex(index = False, escape = False, position = "h")



#print(maketable( ('(x \pm dx)cm',x,dx), ('(y \pm dy)cm',y,dy))[1])
