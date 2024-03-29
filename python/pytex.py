# -*- coding: utf-8 -*-
# from __future__ import division # Deprecated
###############
##           ##
##   SYMPY   ##
##           ##
###############
# Functions
from sympy import exp, ln, log, sin, cos, tan, asin, acos, atan, sinh, cosh, tanh, asinh, acosh, atanh, sqrt, root, erf, gamma, Function, FunctionClass
from sympy.core.function import ArgumentIndexError
# Statistics
from sympy import factorial, binomial
# Symbols
from sympy import var, symbols, Symbol, Dummy
# Numbers
from sympy import N, Integer, Float, Rational, Number, Poly
from sympy.core.numbers import Zero, One, NegativeOne, Half
# Matrices
from sympy import Matrix, trace, transpose, det
# Complex Numbers
from sympy import conjugate
# Constants
from sympy import I, nan, pi, oo, zoo
from sympy import E as e
# Functions involving integers
from sympy import factorint, primefactors, gcd, lcm
# Functions involving decimals
from sympy import floor, ceiling, sign, Mod, Max, Min, Abs
# Equations
from sympy import solve, Eq, Equality
# Expressions
from sympy import collect, srepr, sympify, expand, factor
# Simplification
from sympy import simplify, radsimp, ratsimp, trigsimp, powsimp, combsimp, nsimplify, cancel, refine, Q, S
# Operations
from sympy import Add, Mul, Pow, prod
# Operators
from sympy import diff, integrate, limit, Derivative, Integral
# Numeric tools
from sympy.mpmath import polar
from sympy.polys.specialpolys import interpolating_poly
# Physics units
import sympy.physics.units as un
#######################
##                   ##
##   Other modules   ##
##                   ##
#######################
from latex import LatexPrinter, translate, latex
from random import randrange, randint, uniform, shuffle, choice, seed
import sys, copy, inspect
from os import devnull
FNULL = open(devnull, 'w')
from subprocess import call, Popen, PIPE
import re as regexp
import time as tm
import numpy as np
from scipy.integrate import ode


# Symbols
#  ____                  _           _     
# / ___| _   _ _ __ ___ | |__   ___ | |___ 
# \___ \| | | | '_ ` _ \| '_ \ / _ \| / __|
#  ___) | |_| | | | | | | |_) | (_) | \__ \
# |____/ \__, |_| |_| |_|_.__/ \___/|_|___/
#        |___/
#
__digits__ = 5
__physics__ = False
dt = symbols('dt')
# Mathematical variables
var('r:z')
var('i:n', integer=True)
var('f:g', cls=Function)
var('alpha beta gamma delta epsilon phi iota kappa rho theta')
# Physical variables
var('t:10 x:10 y:10 z:10')
var('v_x v_y v_z')
var('v_x:10 v_y:10 v_z:10')
var('a_x a_y a_z')
var('a_x:10 a_y:10 a_z:10')
var('phi:10 rho:10 theta:10 mu:10 xi:10 upsilon:10')
var('v_phi v_rho v_theta v_mu v_xi v_upsilon')
var('v_phi:10 v_rho:10 v_theta:10 v_mu:10 v_xi:10 v_upsilon:10')
var('a_phi a_rho a_theta a_mu a_xi a_upsilon')
var('a_phi:10 a_rho:10 a_theta:10 a_mu:10 a_xi:10 a_upsilon:10')
# Electronic variables
var('U:10')
var('i:10')
var('R:10')
var('C:10')
var('q:10')
# Physical equations
ec = {
'xru'   : Eq(x1 - x0 , v_x0*t),
'yru'   : Eq(y1 - y0 , v_y0*t),
'zru'   : Eq(z1 - z0 , v_z0*t),
'xra'   : Eq(x1 - x0 , v_x0*t + Rational(1,2)*a_x*t**2),
'yra'   : Eq(y1 - y0 , v_y0*t + Rational(1,2)*a_y*t**2),
'zra'   : Eq(z1 - z0 , v_z0*t + Rational(1,2)*a_z*t**2),
'vxra'  : Eq(v_x1 - v_x0 , a_x*t),
'vyra'  : Eq(v_y1 - v_y0 , a_y*t),
'vzra'  : Eq(v_z1 - v_z0 , a_z*t),
'axra'  : Eq(v_x1**2 - v_x0**2 , Rational(2)*a_x*(x1 - x0)),
'ayra'  : Eq(v_y1**2 - v_y0**2 , Rational(2)*a_y*(y1 - y0)),
'azra'  : Eq(v_z1**2 - v_z0**2 , Rational(2)*a_z*(z1 - z0))
}
__variable_names__ = {}
def setvn(dicti = {}):
    """
    Assigns variable names.
    """
    global __variable_names__
    if dicti == {}:
        __variable_names__ = {}
    else:
        __variable_names__.update(dicti)
# Units
#  _   _       _ _       
# | | | |_ __ (_) |_ ___ 
# | | | | '_ \| | __/ __|
# | |_| | | | | | |_\__ \
#  \___/|_| |_|_|\__|___/
#
uN     = un.Unit("Newtons", r"N")
ukg    = un.kg#Unit("Kilogramos", r"kg")
um     = un.m#Unit("metros", r"m")
umin   = un.Unit("minutos", r"min")
us     = un.s#Unit("segundos", r"s")
uHz    = un.Unit("Hertzios", r"Hz")
ukm    = un.Unit("kilometros", r"km")
uh     = un.Unit("horas", r"h")
urad   = un.Unit("radianes", r"rad")
uo     = un.Unit("grados", r"^\circ")
uomin  = un.Unit("grados", r"'")
uos    = un.Unit("grados", r"''")
urpm   = un.Unit("revoluciones por minuto", r"r.p.m.")
uA     = un.A#Unit("Amperios", r"A")
uV     = un.Unit("Voltios", r"V")
uOhm   = un.Unit("Ohmnios", r"\Omega")
uC     = un.Unit("Coulombios", r"C")
uF     = un.Unit("Faradios", r"F")
uJ     = un.Unit("Julios", r"J")
uW     = un.Unit("Watios", r"W")
umol   = un.mol#Unit("moles", r"mol")
uK     = un.K#Unit("Kelvin", r"K")
uT     = un.Unit("Teslas", r"T")
uH     = un.Unit("Henrios", r"H")
uPa    = un.Unit("Pascales", r"Pa")
#
# Simplifying expressions with units
#
units_format = [
{
# Primary units. Although they are ordered not matter what order.
# therefore they appear in the same directory.
# Circuits
uF            : un.F,
uOhm          : un.ohm,
uV            : un.V,
uH            : un.H,
uT            : un.T,
uC            : un.C,
#uA            : un.A, # primary
# Dynamics
uW            : un.W,
uJ            : un.J,
uN            : un.N,
uPa           : un.Pa,
uHz           : un.s**-1#,
#ukg           : un.kg, # primary
#um            : un.m, # primary
#us            : un.s, # primary
# Thermodynamics
#umol          : un.mol, # primary
#uK            : un.K # primary
},
# Derived units. Essential order, so several directories are defined.
{
un.F            : uF
},
{
un.ohm          : uOhm
},
{
un.V            : uV
},
{
un.H            : uH
},
{
un.J/urad       : un.Unit("Newtons*metro", r"N\cdot m")
},
{
un.W            : uW
},
{
un.J            : uJ
},
{
un.T            : uT
},
{
un.N            : uN,
un.Pa           : uPa
},
{
un.kg/un.s**2   : un.Unit("Newtons/metro", r"\ufrac{N}{m}")
},
{
un.C            : uC
}
]
# Unit conversion
#  _   _       _ _                                       _             
# | | | |_ __ (_) |_    ___ ___  _ ____   _____ _ __ ___(_) ___  _ __  
# | | | | '_ \| | __|  / __/ _ \| '_ \ \ / / _ \ '__/ __| |/ _ \| '_ \ 
# | |_| | | | | | |_  | (_| (_) | | | \ V /  __/ |  \__ \ | (_) | | | |
#  \___/|_| |_|_|\__|  \___\___/|_| |_|\_/ \___|_|  |___/_|\___/|_| |_|
#

# International System
cSI = {
ukm        : 1000*um,
uh         : 3600*us,
urpm       : pi/30*urad/us,
uo         : pi/180*urad
}
# Another System
cNSI = {
um         : ukm/1000,
us         : uh/3600,
urad/us    : 30/pi*urpm,
urad       : 180/pi*uo
}
# Functions involving units
#  _____                 _   _                 
# |  ___|   _ _ __   ___| |_(_) ___  _ __  ___ 
# | |_ | | | | '_ \ / __| __| |/ _ \| '_ \/ __|
# |  _|| |_| | | | | (__| |_| | (_) | | | \__ \
# |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#  _                 _       _                           _ _       
# (_)_ ____   _____ | |_   _(_)_ __   __ _    _   _ _ __ (_) |_ ___ 
# | | '_ \ \ / / _ \| \ \ / / | '_ \ / _` |  | | | | '_ \| | __/ __|
# | | | | \ V / (_) | |\ V /| | | | | (_| |  | |_| | | | | | |_\__ \
# |_|_| |_|\_/ \___/|_| \_/ |_|_| |_|\__, |   \__,_|_| |_|_|\__|___/
#                                    |___/
#
def erase_units(expr):
    """
    Remove units from expression.
    """
    if isinstance(expr, list):
        return [ erase_units(i) for i in expr ]
    elif isinstance(expr, tuple):
        return tuple([ erase_units(i) for i in expr ])
    elif isinstance(expr, dict):
        return { key: erase_units(expr[key]) for key in list(expr.keys())}
    elif isinstance(expr, Add):
        result = 0
        for arg in expr.args:
            result += erase_units(arg)
        return result
    elif isinstance(expr, Mul):
        result = 1
        for arg in expr.args:
            result *= erase_units(arg)
        return result
    elif isinstance(expr, Pow):
        return erase_units(expr.base)**expr.exp
    elif isinstance(expr, Equality):
        return Eq(erase_units(expr.lhs), erase_units(expr.rhs))
    elif isinstance(expr, Matrix):
        return Matrix([ [ erase_units(expr[i,j]) for j in range(expr.cols) ] for i in range(expr.rows) ])
    elif isinstance(expr, un.Unit):
        return 1
    # Remove units inside functions
    elif isinstance(expr, Function):
        return type(expr)(*( erase_units(i) for i in expr.args ))
    else:
        return expr
def freeze_units(expr):
    """
    Convert products and divisions of units in a block
    """
    if isinstance(expr, list):
        return [ freeze_units(i) for i in expr ]
    elif isinstance(expr, tuple):
        return tuple([ freeze_units(i) for i in expr ])
    elif isinstance(expr, dict):
        return { key: freeze_units(value) for key, value in list(expr.items())}
    elif isinstance(expr, Add):
        result = 0
        for arg in expr.args:
            result += freeze_units(arg)
        return result
    elif isinstance(expr, Mul):
        contain_add = False
        for arg in expr.args:
            if isinstance(arg, Add):
                contain_add = True
                break
        if contain_add:
            result = 1
            for arg in expr.args:
                result *= freeze_units(arg)
        else:
            result = expr
            if hasattr(expr, "atoms"):
                if len(expr.atoms(un.Unit)) != 0:
                    units = 1
                    value = 1
                    for arg in expr.args:
                        if len(arg.atoms(un.Unit)) != 0:
                            units *= arg
                        else:
                            value *= arg
                    if units == 1/un.s:
                        units = uHz
                    result = Mul(value, un.Unit("Bloque de unidades",r"\;"+latex(units).replace(r"\frac",r"\ufrac")))
        return result
    elif isinstance(expr, Equality):
        return Eq(freeze_units(expr.lhs), freeze_units(expr.rhs))
    elif isinstance(expr, Matrix):
        return Matrix([ [ freeze_units(expr[i,j]) for j in range(expr.cols) ] for i in range(expr.rows) ])
    # Freeze inside functions
    elif isinstance(expr, Function):
        return type(expr)(*( freeze_units(i) for i in expr.args ))
    else:
        return expr
# Physical constants
#  ____  _               _           _ 
# |  _ \| |__  _   _ ___(_) ___ __ _| |
# | |_) | '_ \| | | / __| |/ __/ _` | |
# |  __/| | | | |_| \__ \ | (_| (_| | |
# |_|   |_| |_|\__, |___/_|\___\__,_|_|
#              |___/                   
#                      _              _       
#   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
#  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
# | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
#  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
#
co = {
########################### UNIVERSAL
'c'      : 2.99792458e8*um/us,
'h'      : 6.62e-34*uJ*us,
########################### THERMODYNAMIC
'Na'     : 6.022e23,
'R'      : 8.314*uJ/umol/uK,
'cvO2'   : 648.*uJ/ukg/uK,
'cpO2'   : 911.2*uJ/ukg/uK,
########################### ELECTROMAGNETIC
'Ke'     : 9.e9*uN*um**2/uC**2,
'Km'     : 1.e-7*uT*um/uA,
'mu0'    : pi*4.e-7*uT*um/uA,
'ep0'    : 8.85e-12*uF/um,
########################### PARTICLE
'me'     : 9.1e-31*ukg,
'e'      : 1.6E-19*uC,
########################### NUCLEAR
'Ry'     : 1.097e7/um,
########################### ASTRONOMIC
'G'      : 6.67e-11*uN*um**2/ukg**2,
'g'      : 9.81*um/us**2,
'MT'     : 5.98e24*ukg,
'RT'     : 6.37e6*um,
'MS'     : 1.99e30*ukg,
'RS'     : 6.96e8*um,
########################### MATERIAL
'dH2O'   : 1000.*ukg/um**3,
'dHg'    : 13600.*ukg/um**3,
}
# Linear Systems
#  _     _                         ____            _                     
# | |   (_)_ __   ___  __ _ _ __  / ___| _   _ ___| |_ ___ _ __ ___  ___ 
# | |   | | '_ \ / _ \/ _` | '__| \___ \| | | / __| __/ _ \ '_ ` _ \/ __|
# | |___| | | | |  __/ (_| | |     ___) | |_| \__ \ ||  __/ | | | | \__ \
# |_____|_|_| |_|\___|\__,_|_|    |____/ \__, |___/\__\___|_| |_| |_|___/
#                                        |___/
#
def factordet(Mat):
    """
    Extract common factors of the determinant of the matrix.

    Examples
    ========

    >>> from sympy import *
    >>> x, y, z = symbols('x y z')
    >>> A = Matrix([[x,x*y],[y*z,z]])
    >>> factordet(A)
    x*z
    """
    fact = 1
    ncols = Mat.cols
    for i in range(ncols):
        col = Mat.col(i)
        common = gcd(list(col))
        if (common != 0)&(common != 1):
            fact *= common
            Mat[i] = Matrix(list(map(cancel, col/common)))
    for j in range(Mat.rows):
        row = Mat.row(j)
        common = gcd(list(row))
        if (common != 0)&(common != 1):
            fact *= common
            Mat[j*ncols] = Matrix([list(map(cancel, row/common))])
    return fact

def solveswc(ecu_list, res_list):
    """
    Solves simplifying big linear systems.
    """
    A, B = syst2matrix(ecu_list, res_list)
    Den = Matrix(A)
    den = simplify(factordet(Den))
    Num, num = [], []
    for i in range(A.cols):
        Num.append(Matrix(A))
        Num[i][i] = B
        num.append(factordet(Num[i]))
    Den = Den.det_bareis()
    return {res_list[i]: cancel(num[i]/den)*Num[i].det_bareis()/Den for i in range(len(res_list))}

def syst_subs(system, equations, *params):
    """
    Solve 'system' for variables in 'variables' using 'equations'
    """
    variables = []
    arrange = False
    for param in params:
        if isinstance(param, bool):
            arrange = param
        else:
            variables = param
    variables = set(variables)
    system_vars = []
    for equation in system:
        system_vars += list(equation.atoms(Symbol))
    system_vars = set(system_vars)
    equations_vars = []
    for equation in equations:
        equations_vars += list(equation.atoms(Symbol))
    equations_vars = set(equations_vars)
    # Solve for variables listed
    substitution = solve(equations, (system_vars|equations_vars)-variables)
    if arrange:
        vars_to_zero = {variable: 0 for variable in system_vars}
    result = []
    for equation in system:
        if isinstance(equation, Equality):
            if arrange:
                replaced = collect((equation.lhs - equation.rhs).subs(substitution).expand(), variables)
                varless = replaced.subs(vars_to_zero)
                result.append(Eq(replaced - varless, -varless))
            else:
                equation = equation.subs(substitution)
                result.append(Eq(collect(equation.lhs.expand(), variables), collect(equation.rhs.expand(), variables)))
        else:
            replaced = collect(equation.subs(substitution).expand(), variables)
            if arrange:
                varless = replaced.subs(vars_to_zero)
                result.append(Eq(replaced - varless, -varless))
            else:
                result.append(replaced)
    return result
def syst2matrix(system, variables=None):
    """
    Returns A, B matrices of the system A·X = B.

    Examples
    ========

    >>> from sympy import *
    >>> x, y, z = symbols('x y z')
    >>> syst = [ 2*x + 3*y - 10, - 3*x + 5*y - 7 ]
    >>> syst2matrix(syst)
    ⎛⎡2   3⎤, ⎡10⎤⎞
    ⎜⎢     ⎥  ⎢  ⎥⎟
    ⎝⎣-3  5⎦  ⎣7 ⎦⎠

    >>> syst = [ Eq(2*x + 3*y, 10), Eq(- 3*x + 5*y, 7) ]
    >>> syst2matrix(syst)
    ⎛⎡3  2 ⎤, ⎡10⎤⎞
    ⎜⎢     ⎥  ⎢  ⎥⎟
    ⎝⎣5  -3⎦  ⎣7 ⎦⎠

    >>> syst = [ Eq(2*x + 3*y, 10), - 3*x + 5*y - 7 ]
    >>> syst2matrix(syst)
    ⎛⎡3  2 ⎤, ⎡10⎤⎞
    ⎜⎢     ⎥  ⎢  ⎥⎟
    ⎝⎣5  -3⎦  ⎣7 ⎦⎠
    """
    if variables == None:
        variables = []
        for equation in system:
            variables += list(equation.atoms(Symbol))
        variables = list(set(variables))
    else:
        variables = list(set(variables))
    vars_to_zero = { k: 0 for k in variables }
    matrix_of_the_system = []
    const_of_the_system = []
    for equation in system:
        matrix_of_the_system.append([])
        if isinstance(equation, Equality):
            equation = (equation.lhs - equation.rhs)
        const_of_the_system.append(-equation.subs(vars_to_zero))
        for variable in variables:
            matrix_of_the_system[-1].append(equation.expand().collect(variable).coeff(variable))
    return Matrix(matrix_of_the_system), Matrix(const_of_the_system)
# classical Mechanics
#   ____ _               _           _ 
#  / ___| | __ _ ___ ___(_) ___ __ _| |
# | |   | |/ _` / __/ __| |/ __/ _` | |
# | |___| | (_| \__ \__ \ | (_| (_| | |
#  \____|_|\__,_|___/___/_|\___\__,_|_|
#  __  __           _                 _          
# |  \/  | ___  ___| |__   __ _ _ __ (_) ___ ___ 
# | |\/| |/ _ \/ __| '_ \ / _` | '_ \| |/ __/ __|
# | |  | |  __/ (__| | | | (_| | | | | | (__\__ \
# |_|  |_|\___|\___|_| |_|\__,_|_| |_|_|\___|___/
#
def eleq(Lagrangian, Friction = 0, t = Symbol('t')):
    """
    Returns Euler-Lagrange equations of the lagrangian system.

    Examples
    ========

    >>> from sympy import *
    >>> t, k = symbols('t k')
    >>> x = symbols('x', cls=Function)
    >>> eleq(diff(x(t),t)**2/2 - k*x(t)**2/2)
    {a_x: -k*x}

    >>> a = symbols('a')
    >>> eleq(diff(x(t),t)**2/2 - k*x(t)**2/2, a*diff(x(t),t)**2/2)
    {a_x: -*a*v_x - k*x}
    """
    Lagrangian = simplify(Lagrangian)
    var_list = [list(x.atoms(Function))[0] for x in Lagrangian.atoms(Derivative)]
    nvar = len(var_list)
    ecu_list = [ diff(Lagrangian, variable) - diff(Lagrangian, diff(variable,t), t) -  diff(Friction, diff(variable,t)) for variable in var_list ]
    str_list = [ str(variable).replace("("+str(t)+")","") for variable in var_list ]
    a_subs = {diff(var_list[i],t,2): Symbol('a_' + str_list[i]) for i in range(nvar)}
    v_subs = {diff(var_list[i],t): Symbol('v_' + str_list[i]) for i in range(nvar)}
    x_subs = {var_list[i]: Symbol(str_list[i]) for i in range(nvar)}
    for i in range(nvar):
        if hasattr(ecu_list[i], "subs"):
            ecu_list[i] = ecu_list[i].subs(a_subs).subs(v_subs).subs(x_subs)
    a_list = sorted(list(a_subs.values()), key = str)
    return solveswc(ecu_list, a_list)


def ieleq(Lagrangian, Friction = 0, t = Symbol('t')):
    """
    Returns Euler-Lagrange equations of the lagrangian system
    with first integrals.

    Examples
    ========

    >>> from sympy import *
    >>> t, k = symbols('t k')
    >>> x = symbols('x', cls=Function)
    >>> ieleq(diff(x(t),t)**2/2)
    {v_x: v_x0}

    >>> a = symbols('a')
    >>> ieleq(diff(x(t),t)**2/2, a*diff(x(t),t)**2/2)
    {v_x: -a*x + a*x0 + v_x0}
    """
    Lagrangian = simplify(Lagrangian)
    var_list = [list(x.atoms(Function))[0] for x in Lagrangian.atoms(Derivative)]
    nvar = len(var_list)
    # new variables
    str_list = [ str(variable).replace("("+str(t)+")","") for variable in var_list ]
    a_list = [ Symbol('a_' + str_list[i]) for i in range(nvar) ]
    v_list = [ Symbol('v_' + str_list[i]) for i in range(nvar) ]
    a_subs = {diff(var_list[i],t,2): a_list[i] for i in range(nvar)}
    v_subs = {diff(var_list[i],t): v_list[i] for i in range(nvar)}
    x_subs = {var_list[i]: Symbol(str_list[i]) for i in range(nvar)}
    v0_subs = {diff(var_list[i],t): Symbol('v_' + str_list[i] + "0") for i in range(nvar)}
    x0_subs = {var_list[i]: Symbol(str_list[i] + "0") for i in range(nvar)}
    # First integrals equations
    a_ecu = []
    v_ecu = []
    a_var = []
    v_var = []
    for i, variable in enumerate(var_list):
        dLx = diff(Lagrangian, variable)
        dLv = diff(Lagrangian, diff(variable,t))
        dFv = diff(Friction, diff(variable,t))
        IdFv = integrate(dFv,t)
        if (dLx == 0)&(not isinstance(IdFv, Integral)):
            v_var.append(v_list[i])
            v_ecu.append(dLv.subs(v_subs).subs(x_subs) - dLv.subs(v0_subs).subs(x0_subs))
            v_ecu[-1] += IdFv.subs(v_subs).subs(x_subs) - IdFv.subs(v0_subs).subs(x0_subs)
        else:
            a_var.append(a_list[i])
            a_ecu.append((diff(dLv, t) - dLx).subs(a_subs).subs(v_subs).subs(x_subs))
            a_ecu[-1] += dFv.subs(a_subs).subs(v_subs).subs(x_subs)
    # Solve system
    sol_dict = {}
    if len(v_var) != 0:
        sol_dict.update(solveswc(v_ecu, v_var))
    if len(a_var) != 0:
        sol_dict.update(solveswc(a_ecu, a_var))
    return sol_dict

def hamiltonian(Lagrangian, t = Symbol('t'), delta = False):
    """
    Returns the Hamiltonian of the Lagrangian.

    Examples
    ========

    >>> from sympy import *
    >>> t, k = symbols('t k')
    >>> x = symbols('x', cls=Function)
    >>> hamiltonian(diff(x(t),t)**2/2 - k*x(t)**2/2)
    k*x**2/2 + v_x**2/2
    """
    Lagrangian = simplify(Lagrangian)
    var_list = [list(x.atoms(Function))[0] for x in Lagrangian.atoms(Derivative)]
    nvar = len(var_list)
    # New variables.
    str_list = [ str(variable).replace("("+str(t)+")","") for variable in var_list ]
    v_subs = {diff(var_list[i],t): Symbol('v_' + str_list[i]) for i in range(nvar)}
    x_subs = {var_list[i]: Symbol(str_list[i]) for i in range(nvar)}
    # Hamiltonian calculus.
    dxdLv = 0
    for variable in var_list:
        dxdLv += diff(variable,t)*diff(Lagrangian, diff(variable,t))
    result = simplify((dxdLv - Lagrangian).subs(v_subs).subs(x_subs))
    if delta:
        v0_subs = {Symbol('v_' + str_list[i]): Symbol('v_' + str_list[i] + "0") for i in range(nvar)}
        x0_subs = {Symbol(str_list[i]): Symbol(str_list[i] + "0") for i in range(nvar)}
        return result - result.subs(v0_subs).subs(x0_subs)
    else:
        return result

def B(particleA, particleB):
    """
    Returns magnetic field expression between 'particleA' and 'particleB'.

    Examples
    ========

    >>> B(1,2)
    Matrix([
    [ 9000000000.0*q1*(v_y1*(-z1 + z2) - v_z1*(-y1 + y2))/((-x1 + x2)**2 + (-y1 + y2)**2 + (-z1 + z2)**2)**(3/2)],
    [9000000000.0*q1*(-v_x1*(-z1 + z2) + v_z1*(-x1 + x2))/((-x1 + x2)**2 + (-y1 + y2)**2 + (-z1 + z2)**2)**(3/2)],
    [ 9000000000.0*q1*(v_x1*(-y1 + y2) - v_y1*(-x1 + x2))/((-x1 + x2)**2 + (-y1 + y2)**2 + (-z1 + z2)**2)**(3/2)]])

    >>> B(7,3)
    Matrix([
    [ 9000000000.0*q7*(v_y7*(z3 - z7) - v_z7*(y3 - y7))/((x3 - x7)**2 + (y3 - y7)**2 + (z3 - z7)**2)**(3/2)],
    [9000000000.0*q7*(-v_x7*(z3 - z7) + v_z7*(x3 - x7))/((x3 - x7)**2 + (y3 - y7)**2 + (z3 - z7)**2)**(3/2)],
    [ 9000000000.0*q7*(v_x7*(y3 - y7) - v_y7*(x3 - x7))/((x3 - x7)**2 + (y3 - y7)**2 + (z3 - z7)**2)**(3/2)]])
    """
    rAB = Matrix([eval("x"+str(particleB))-eval("x"+str(particleA)), eval("y"+str(particleB))-eval("y"+str(particleA)), eval("z"+str(particleB))-eval("z"+str(particleA))])
    vA = Matrix([eval("v_x"+str(particleA)), eval("v_y"+str(particleA)), eval("v_z"+str(particleA))])
    return 9.e9*eval("q"+str(particleA))/sqrt(rAB.dot(rAB))**3*vA.cross(rAB)
def E(particleA, particleB):
    rAB = Matrix([eval("x"+str(particleB))-eval("x"+str(particleA)), eval("y"+str(particleB))-eval("y"+str(particleA)), eval("z"+str(particleB))-eval("z"+str(particleA))])
    return 9.e9*eval("q"+str(particleA))/sqrt(rAB.dot(rAB))**3*rAB
def G(particleA, particleB):
    rAB = Matrix([eval("x"+str(particleB))-eval("x"+str(particleA)), eval("y"+str(particleB))-eval("y"+str(particleA)), eval("z"+str(particleB))-eval("z"+str(particleA))])
    return -6.67e-11*eval("m"+str(particleA))/sqrt(rAB.dot(rAB))**3*rAB
def FB(particleA, particleB):
    vB = Matrix([eval("v_x"+str(particleB)), eval("v_y"+str(particleB)), eval("v_z"+str(particleB))])
    return eval("q"+str(particleB))*vB.cross(B(particleA, particleB))
def FE(particleA, particleB):
    return eval("q"+str(particleB))*E(particleA, particleB)
def FG(particleA, particleB):
    return eval("m"+str(particleB))*G(particleA, particleB)
def VE(particleA, particleB):
    rAB = Matrix([eval("x"+str(particleB))-eval("x"+str(particleA)), eval("y"+str(particleB))-eval("y"+str(particleA)), eval("z"+str(particleB))-eval("z"+str(particleA))])
    return 9.e9*eval("q"+str(particleA))/sqrt(rAB.dot(rAB))*eval("q"+str(particleB))
def VG(particleA, particleB):
    rAB = Matrix([eval("x"+str(particleB))-eval("x"+str(particleA)), eval("y"+str(particleB))-eval("y"+str(particleA)), eval("z"+str(particleB))-eval("z"+str(particleA))])
    return -6.67e-11*eval("m"+str(particleA))/sqrt(rAB.dot(rAB))*eval("m"+str(particleB))
# Output Formatting
#   ___        _               _   
#  / _ \ _   _| |_ _ __  _   _| |_ 
# | | | | | | | __| '_ \| | | | __|
# | |_| | |_| | |_| |_) | |_| | |_ 
#  \___/ \__,_|\__| .__/ \__,_|\__|
#                 |_|              
#  _____                          _   _   _             
# |  ___|__  _ __ _ __ ___   __ _| |_| |_(_)_ __   __ _ 
# | |_ / _ \| '__| '_ ` _ \ / _` | __| __| | '_ \ / _` |
# |  _| (_) | |  | | | | | | (_| | |_| |_| | | | | (_| |
# |_|  \___/|_|  |_| |_| |_|\__,_|\__|\__|_|_| |_|\__, |
#                                                 |___/
#
def ifactor(x):
    """
    Factor integers. Formatting result in exponential form.
    """
    if isinstance(x, (Rational, Half)):
        result = ifactor(x.p)/ifactor(x.q)
    elif isinstance(x, list):
        result = list(map(ifactor, x))
    elif isinstance(x, dict):
        result = {k: ifactor(v) for k, v in list(x.items())}
    elif isinstance(x, Add):
        result = 0
        for arg in x.args:
            result += ifactor(arg)
    elif isinstance(x, Mul):
        result = 1
        for arg in x.args:
            result *= ifactor(arg)
    elif isinstance(x, Pow):
        result = ifactor(x.base)**x.exp
    elif isinstance(x, Symbol):
        result = tryto(x.name, int)
        if result == None:
            result = x
        else:
            result = ifactor(result)
    elif isinstance(x, (Integer, int)):
        sig = sign(x)
        x = abs(x)
        if (x == 1)|(x == 0):
            result = sig * Symbol(str(x))
        else:
            prim = primefactors(x)
            expo = factorint(x)
            result = sig * Symbol(str(prim[0])) ** expo[prim[0]]
            for i in range(1, len(prim)):
                result = result * Symbol(str(prim[i])) ** expo[prim[i]]
    else:
        x = nsimplify(x)
        if not isinstance(x, Rational):
            raise ValueError("Not Factorizable object.")
        result = ifactor(x)
    return result
def lfactor(_x):
    """
    Factor integers. Latex output.
    """
    if isinstance(_x, (int, Integer, Zero, One, NegativeOne)):
        if sign(_x) == -1:
            _sign = "-"
        else:
            _sign = ""
        _x = abs(_x)
        if (_x == 1)|(_x == 0):
            _lfactor = _sign + str(_x)
        else:
            _primes = primefactors(_x)
            _exponents = factorint(_x)
            _lfactor = _sign + "{" + str(_primes[0]) + "}^{" + str(_exponents[_primes[0]]) + "}"
            for _i in range(1, len(_primes)):
                _lfactor = _lfactor + "\cdot {" + str(_primes[_i]) + "}^{" + str(_exponents[_primes[_i]]) + "}"
    elif isinstance(_x, (Rational, Half)):
        _lfactor = "\\frac{" + lfactor(_x.p) + "}{" + lfactor(_x.q) + "}"
    elif isinstance(_x, list):
        _lfactor = list(map(lfactor, _x))
    elif isinstance(_x, dict):
        _lfactor = {}
        for _k in list(_x.keys()):
            _lfactor[_k] = lfactor(_x[_k])
    return _lfactor
def polar_deg(x):
    """
    Subscript polar notation for complex numbers. Latex output.
    Degrees units.
    """
    x = polar(complex(x))
    result = str(Float(x[0]).evalf(__digits__)) + "_{"
    result += str((Float(x[1])*180/pi).evalf(__digits__)) + "^\\circ}"
    return result
def polar_rad(x):
    """
    Subscript polar notation for complex numbers. Latex output.
    Radians units.
    """
    x = polar(complex(x))
    result = str(Float(x[0]).evalf(__digits__)) + "_{"
    result += str((Float(x[1])/pi).evalf(__digits__)) + "\\pi\\;rad}"
    return result
def latexsy(_x, dicti = {}):
    dicti.update(__variable_names__)
    _latexsy = latex(_x, symbol_names = dicti)
    _latexsy = regexp.sub("([^_a-zA-Z])i([^_a-zA-Z]|$)", "\\1\\\\I\\2", _latexsy)
    _latexsy = regexp.sub("\.0([^0-9]|$)", "\\1", _latexsy)
    return _latexsy
def split_mat(_s, _n):
    """
    Split output matrix '_s' if has more than '_n' columns
    """
    _start = regexp.search("\\\\begin\{(.?|small)matrix\}", _s).end()
    _end   = regexp.search("\\\\end\{(.?|small)matrix\} *$", _s).start()
    _first = _s.find("\\\\", _start, _end)
    _colum = _s.count("&", _start, _first) + 1
    _split_mat = _s
    if _start >= _end:
        sys.exit("Error: split_mat: No se encuentra matriz. Línea: " + str(_nline_)
        + " Pos:" + str(_start) + ", " + str(_end) + " \n" + _s)
    _i = 0
    _pos_list = []
    _typ_list = []
    for _iter in regexp.finditer("&|\\\\\\\\", _split_mat):
        _pos = _iter.start()
        if (_start < _pos)&(_pos < _end):
            _i += 1
        else:
            break
        _i %= _colum
        if (_i % _n == 0):
            _pos_list.append(_pos)
            _typ_list.append(_i)
    if len(_pos_list) !=0:
        _pos_list.append(_end)
        _typ_list.append(0)
        _pos_list.reverse()
        _typ_list.reverse()
        _complete = _n - _colum % _n
        for _i in range(len(_pos_list)):
            if _typ_list[_i] == 0:
                _subst = " " + "& "*_complete
            else:
                if _typ_list[_i] == _n:
                    _subst = " & \\backslash \\\\\n ...  "
                else:
                    _subst = "  \\\\\n ...  "
            _split_mat = _split_mat[:_pos_list[_i]] + _subst + _split_mat[_pos_list[_i]:]
    return _split_mat
def physics_format(expr, dicti = {}):
    """
    Process physical units.
    """
    # Simplify units
    if atoms(expr, un.Unit):
        for subst in units_format:
            expr = subs(expr, subst)
    # Round '__digits__' significant figures
    import __main__
    if "__digits__" in dir(__main__):
        __digits__ = __main__.__digits__
    if isinstance(__digits__, (int, Integer)):
        return cevalf(expr, __digits__) #significant_digits(expr)
    else:
        return expr
# Diophantine equations
#  ____  _             _                 _   _            
# |  _ \(_) ___  _ __ | |__   __ _ _ __ | |_(_)_ __   ___ 
# | | | | |/ _ \| '_ \| '_ \ / _` | '_ \| __| | '_ \ / _ \
# | |_| | | (_) | |_) | | | | (_| | | | | |_| | | | |  __/
# |____/|_|\___/| .__/|_| |_|\__,_|_| |_|\__|_|_| |_|\___|
#               |_|                                       
#                         _   _                 
#   ___  __ _ _   _  __ _| |_(_) ___  _ __  ___ 
#  / _ \/ _` | | | |/ _` | __| |/ _ \| '_ \/ __|
# |  __/ (_| | |_| | (_| | |_| | (_) | | | \__ \
#  \___|\__, |\__,_|\__,_|\__|_|\___/|_| |_|___/
#          |_|
#
def c_sol2lin(sols, layer = [1,20], equation = True, nonzero = [], nonneg = [], linears = -1):
    """
    Find linear equations with 'sols' solutions and coefficients in 'layer'.
    Using c to improve speed.
    """
    nvars = len(sols) + 1
    if linears == -1:
        linears = nvars - 1
    if not isinstance(layer, list):
        layer = [1, layer]
    if nonzero == []:
        nonzero = [ True for i in range(1, nvars) ] + [ False ]
    elif nonzero == True:
        nonzero = [ True for i in range(nvars)]
    elif nonzero == False:
        nonzero = [ False for i in range(nvars)]
    if nonneg == []:
        nonneg = [ False for i in range(nvars)]
    elif nonneg == True:
        nonneg = [ True for i in range(nvars)]
    elif nonneg == False:
        nonneg = [ False for i in range(nvars)]
    sols = list(map(nsimplify,sols))
    z = lcm(list(map(lambda x: x.q, sols)))
    sols = list(map(lambda x, lz=z: x*lz, sols)) + [z]
    ## Needed to call c code
    import ctypes
    # c library
    c_lib = ctypes.cdll.LoadLibrary('./cpppytex.so')
    # parameters
    c_coef = (ctypes.c_int * nvars)(*sols)
    c_ncoef = ctypes.c_uint(nvars)
    c_layer = (ctypes.c_int * 2)(*layer)
    c_nonzero = (ctypes.c_bool * nvars)(*nonzero)
    c_nonneg = (ctypes.c_bool * nvars)(*nonneg)
    c_linears = ctypes.c_uint(linears)
    # Format input
    c_lib.dioph_lin.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_uint,
    ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool),
    ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.POINTER(ctypes.c_int)),
    ctypes.c_uint]
    # Output
    c_result = (ctypes.POINTER(ctypes.c_int) * linears)()
    for i in range(linears):
        c_result[i] = (ctypes.c_int * nvars)()
    # Format output
    c_lib.dioph_lin.restype = ctypes.c_uint
    # Call c code
    linears = c_lib.dioph_lin(c_coef, c_ncoef, c_layer, c_nonzero, c_nonneg, c_result, c_linears)
    # Process output
    result = []
    for i in range(linears):
        result.append([])
        for j in range(nvars):
            result[-1].append(c_result[i][j])
    if equation:
        symbvars = [Symbol('x'), Symbol('y'),Symbol('z'),Symbol('t'),Symbol('u'),Symbol('v'),Symbol('w')]
        equations = []
        for res in result:
            equ = 0
            for j in range(nvars-1):
                equ += res[j]*symbvars[j]
            equations.append(Eq(equ,-res[-1]))
        return equations
    else:
        return result
def sol2lin(sols, layer = [1,20], equation = True, nonzero = [], nonneg = [], linears = -1):
    """
    Find linear equations with 'sols' solutions and coefficients in 'layer'.
    """
    nvars = len(sols) + 1
    if linears == -1:
        linears = nvars - 1
    if not isinstance(layer, list):
        layer = [1, layer]
    if nonzero == []:
        nonzero = [ True for i in range(1, nvars) ] + [ False ]
    elif nonzero == True:
        nonzero = [ True for i in range(nvars)]
    elif nonzero == False:
        nonzero = [ False for i in range(nvars)]
    if nonneg == []:
        nonneg = [ False for i in range(nvars)]
    elif nonneg == True:
        nonneg = [ True for i in range(nvars)]
    elif nonneg == False:
        nonneg = [ False for i in range(nvars)]
    sols = list(map(nsimplify,sols))
    z = lcm(list(map(lambda x: x.q, sols)))
    sols = list(map(lambda x, lz=z: x*lz, sols)) + [z]
    def cadd(coefs,systems):
        all_independent = True
        for system in systems:
            fact = system[0]/coefs[0]
            independent = False
            for i in range(1,len(coefs)):
                if fact*coefs[i] != system[i]:
                    independent = True
                    break
            if not independent:
                all_independent = False
                break
        if all_independent:
            systems.append(coefs[:])
    systems = []
    n_syst = 0
    coefs = [0 for j in range(nvars)]
    for ilayer in range(layer[0],layer[1]):
        n_range = []
        varsrange = []
        for j in range(nvars):
            if nonzero[j]:
                if nonneg[j]:
                    n_range.append(ilayer)
                    varsrange.append(list(range(1,ilayer+1)))
                else:
                    n_range.append(2*ilayer)
                    varsrange.append(list(range(-ilayer,0))+list(range(1,ilayer+1)))
            else:
                if nonneg[j]:
                    n_range.append(ilayer+1)
                    varsrange.append(list(range(ilayer+1)))
                else:
                    n_range.append(2*ilayer+1)
                    varsrange.append(list(range(-ilayer,ilayer+1)))
        for i in range(nvars):
            if i != 0:
                if nonzero[i-1]:
                    if nonneg[i-1]:
                        varsrange[i-1] = list(range(1,ilayer))
                        n_range[i-1] = ilayer-1
                    else:
                        varsrange[i-1] = list(range(-ilayer+1,0)) + list(range(1,ilayer))
                        n_range[i-1] = 2*(ilayer-1)
                else:
                    if nonneg[i-1]:
                        varsrange[i-1] = list(range(ilayer))
                        n_range[i-1] = ilayer
                    else:
                        varsrange[i-1] = list(range(-ilayer+1,ilayer))
                        n_range[i-1] = 2*ilayer-1
            if nonneg[i]:
                varsrange[i] = [ilayer]
                n_range[i] = 1
            else:
                varsrange[i] = [-ilayer, ilayer]
                n_range[i] = 2
            for integer in range(prod(n_range)):
                scalar = 0
                for j in range(nvars):
                    coefs[j] = varsrange[j][integer % n_range[j]]
                    integer //= n_range[j]
                    scalar += coefs[j]*sols[j]
                if scalar == 0:
                    cadd(coefs, systems)
                    n_syst = len(systems)
                    if n_syst == linears:
                        break
            if n_syst == linears:
                break
        if n_syst == linears:
            break
    if equation:
        symbvars = [Symbol('x'), Symbol('y'),Symbol('z'),Symbol('t'),Symbol('u'),Symbol('v'),Symbol('w')]
        equations = []
        for system in systems:
            equ = 0
            for j in range(nvars-1):
                equ += system[j]*symbvars[j]
            equations.append(Eq(equ,-system[-1]))
        return equations
    else:
        return systems
def isolve(equations, layer = [1,10], nonzero = [], nonneg = [], nsols = -1):
    """
    Returns a list of integer solutions that satisfy all equations.

    'equations' - Equation or list of equations to be solved.
    'layer'     - Layer or layers to be searched solutions.
    'nonzero'   - Boolean or boolean list. Boolean means a Boolean
                      list with the same value. nth Boolean 'True'
                      means nth variable has non zero value.
    'nonneg'    - Boolean or boolean list. Boolean means a Boolean
                      list with the same value. nth Boolean 'True'
                      means nth variable has non negative value.
    'nsols'     - Looking 'nsols' solutions. -1 finds all solutions.
    """
    if not isinstance(equations, list):
        equations = [ equations ]
    n_equ = len(equations)
    if not isinstance(layer, list):
        layer = [1, layer]
    variables = set([])
    for i in range(n_equ):
        if isinstance(equations[i], Equality):
            equations[i] = equations[i].lhs - equations[i].rhs
        variables |= equations[i].atoms(Symbol)
    variables = sorted(list(variables),key=str)
    nvars = len(variables)
    if nonzero == []:
        nonzero = [ False for i in range(nvars)]
    elif nonzero == True:
        nonzero = [ True for i in range(nvars)]
    elif nonzero == False:
        nonzero = [ False for i in range(nvars)]
    if nonneg == []:
        nonneg = [ False for i in range(nvars)]
    elif nonneg == True:
        nonneg = [ True for i in range(nvars)]
    elif nonneg == False:
        nonneg = [ False for i in range(nvars)]
    solutions = []
    n_sols = 0
    coefs = [0 for j in range(nvars)]
    for ilayer in range(layer[0],layer[1]):
        n_range = []
        varsrange = []
        for j in range(nvars):
            if nonzero[j]:
                if nonneg[j]:
                    n_range.append(ilayer)
                    varsrange.append(list(range(1,ilayer+1)))
                else:
                    n_range.append(2*ilayer)
                    varsrange.append(list(range(-ilayer,0))+list(range(1,ilayer+1)))
            else:
                if nonneg[j]:
                    n_range.append(ilayer+1)
                    varsrange.append(list(range(ilayer+1)))
                else:
                    n_range.append(2*ilayer+1)
                    varsrange.append(list(range(-ilayer,ilayer+1)))
        for i in range(nvars):
            if i != 0:
                if nonzero[i-1]:
                    if nonneg[i-1]:
                        varsrange[i-1] = list(range(1,ilayer))
                        n_range[i-1] = ilayer-1
                    else:
                        varsrange[i-1] = list(range(-ilayer+1,0)) + list(range(1,ilayer))
                        n_range[i-1] = 2*(ilayer-1)
                else:
                    if nonneg[i-1]:
                        varsrange[i-1] = list(range(ilayer))
                        n_range[i-1] = ilayer
                    else:
                        varsrange[i-1] = list(range(-ilayer+1,ilayer))
                        n_range[i-1] = 2*ilayer-1
            if nonneg[i]:
                varsrange[i] = [ilayer]
                n_range[i] = 1
            else:
                varsrange[i] = [-ilayer, ilayer]
                n_range[i] = 2
            for integer in range(prod(n_range)):
                checking = equations[:]
                for j in range(nvars):
                    coefs[j] = varsrange[j][integer % n_range[j]]
                    integer //= n_range[j]
                    for k in range(n_equ):
                        checking[k] = checking[k].subs(variables[j],coefs[j])
                check = True
                for j in range(n_equ):
                    if checking[j] != 0:
                        check = False
                        break
                if check:
                    solutions.append(coefs[:])
                    n_sols = len(solutions)
                    if n_sols == nsols:
                        break
            if n_sols == nsols:
                break
        if n_sols == nsols:
            break
    return solutions
# Trigonometry
#  _____     _                                        _              
# |_   _| __(_) __ _  ___  _ __   ___  _ __ ___   ___| |_ _ __ _   _ 
#   | || '__| |/ _` |/ _ \| '_ \ / _ \| '_ ` _ \ / _ \ __| '__| | | |
#   | || |  | | (_| | (_) | | | | (_) | | | | | |  __/ |_| |  | |_| |
#   |_||_|  |_|\__, |\___/|_| |_|\___/|_| |_| |_|\___|\__|_|   \__, |
#              |___/                                           |___/
#
def arctan(x,y,semi=False):
    """
    Arctan between -pi/2 and pi/2, semi = True;
           between -pi   and pi,   semi = False;
    """
    if x == 0:
        if sign(y) == -1:
            return -pi/2
        else:
            return pi/2
    else:
        if semi:
            return atan(y/x)
        if sign(x) == -1:
            return atan(y/x) + pi
        else:
            return atan(y/x)
# Statistics
#  ____  _        _   _     _   _          
# / ___|| |_ __ _| |_(_)___| |_(_) ___ ___ 
# \___ \| __/ _` | __| / __| __| |/ __/ __|
#  ___) | || (_| | |_| \__ \ |_| | (__\__ \
# |____/ \__\__,_|\__|_|___/\__|_|\___|___/
#
def mode_cont_pure(X):
    n = len(X)
    difs = []
    for i in range(n):
        difs.append(0)
        for j in range(n):
            difs[-1] += abs(X[j] - X[i])
    return X[difs.index(min(difs))]
def mode_cont(X):
    max_value = max(X)
    min_value = min(X)
    if max_value == min_value:
        return max_value
    dif_value = (max_value - min_value)/100
    frec_list = [ 0 for i in range(101)]
    for i in range(len(X)):
        frec_list[int(float(X[i]-min_value)//float(dif_value))] += 1
    return frec_list.index(max(frec_list))*dif_value + min_value
# Strings
#  ____  _        _                 
# / ___|| |_ _ __(_)_ __   __ _ ___ 
# \___ \| __| '__| | '_ \ / _` / __|
#  ___) | |_| |  | | | | | (_| \__ \
# |____/ \__|_|  |_|_| |_|\__, |___/
#                         |___/
#
def numbersstr(_x):
    _numbersstr = []
    _x = regexp.sub("(\-?[0-9]*\.?[0-9]+)", "\",\"\\1\",\"", _x)
    _x = "[\"" + _x + "\"]"
    _x = eval(_x)
    for _i in _x:
        _tmp = tryto(_i, float)
        if _tmp != None:
            _numbersstr.append(_tmp)
    return _numbersstr
def delim(_s, begin = None, paren = [ "([{$", ")]}$" ], step = 1):
    _m = [len(_s) - 1, 0]
    _find = True
    if step >= 0:
        _inc = 1
        _d = 0
    else:
        _inc = -1
        _d = 1
    if begin == None:
        begin = _m[1-_d]
    else:
        if begin > _m[0]:
            return None, None
    while not _s[begin] in paren[_d]:
        begin += _inc
        if _inc*begin > _inc*_m[_d]:
            _find = False
            break
    if not _find:
        return None, None
    end = begin
    _de = ["", ""]
    _de[_d] = _s[end]
    if isinstance(paren, list):
        _tmp = paren[_d].find(_de[_d])
        _de[1-_d] = paren[1-_d][_tmp]
    else:
        _de[1-_d] = paren[1-_d]
    _p = 1
    while _p != 0:
        end += _inc
        if _inc*begin > _inc*_m[_d]:
            _find = False
            break
        if _s[end] == _de[1-_d]:
            _p -= 1
        elif _s[end] == _de[_d]:
            _p += 1
    if _find:
        if _inc == 1:
            return begin, end
        else:
            return end, begin
    else:
        return None, None
def arguments(s, begin = None, paren = [ "([{", ")]}" ], step = 1):
    begin, end = delim(s, begin, paren, step)
    if end == None:
        return []
    result = [ begin ]
    pos = begin + 1
    while pos < end:
        if s[pos] in "([{$":
            _, pos = delim(s, pos)
        elif s[pos] == ",":
            result.append(pos)
        pos += 1
    if pos != end:
        raise NameError('Bloque sin cierre.')
    result.append(end)
    params = []
    for index in range(len(result)-1):
        params.append(s[result[index]+1:result[index+1]])
    return params
def iarguments(s, begin = None, paren = [ "([{", ")]}" ], step = 1):
    begin, end = delim(s, begin, paren, step)
    if end == None:
        return [ -1 ]
    result = [ begin ]
    pos = begin + 1
    while pos < end:
        if s[pos] in "([{$":
            _, pos = delim(s, pos)
        elif s[pos] == ",":
            result.append(pos)
        pos += 1
    if pos != end:
        raise NameError('Bloque sin cierre.')
    result.append(end)
    return result
def delim_fun(_s, _i, step = 1):
    _v = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789."
    _m = len(_s) - 1
    _del = [ "([{$", ")]}$" ]
    _lst = [ "([{+-*/ ,:=", ")]}+-*/ ,:=" ]
    if step >= 0:
        _inc = 1
        _d = 0
    else:
        _inc = -1
        _d = 1
    while _s[_i] == " ":
        _i += _inc
    _j = _i
    if _inc == 1:
        while (_s[_j] in _v)&(_j != _m):
            _j += _inc
        while (_s[_j] == " ")&(_j != _m):
            _j += _inc
    if _s[_j] in _del[_d]:
        _de = ["", ""]
        _de[_d] = _s[_j]
        _tmp = _del[_d].find(_de[_d])
        _de[1-_d] = _del[1-_d][_tmp]
        _p = 1
        while _p != 0:
            _j += _inc
            if _s[_j] == _de[1-_d]:
                _p -= 1
            elif _s[_j] == _de[_d]:
                _p += 1
        if _inc == -1:
            if _j != 0:
                _j += _inc
                while (_s[_j] in _v)&(_j != 0):
                    _j += _inc
                _j -= _inc
    else:
        while (not _s[_j] in _lst[1-_d])&(_j != _m)&(_j != 0):
            _j += _inc
        if _s[_j] in _lst[1-_d]:
            _j -= _inc
    if _inc == 1:
        return _i, _j
    else:
        return _j, _i
# Random
#  ____                 _                 
# |  _ \ __ _ _ __   __| | ___  _ __ ___  
# | |_) / _` | '_ \ / _` |/ _ \| '_ ` _ \ 
# |  _ < (_| | | | | (_| | (_) | | | | | |
# |_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|
#
def indexes(length, amount = 1):
    result = []
    indexes_list = list(range(length))
    for i in range(amount):
        tmp = randrange(length)
        result.append(indexes_list[tmp])
        del indexes_list[tmp]
        length -= 1
    return result
def jumble(_x, items = 0):
    shuffle(_x)
    if items == 0:
        _jumble = _x
    else:
        _jumble = tuple(_x[0:items])
    return _jumble
def randmags(start, end, amount, unit = 1):
    result = indexes(end - start + 1, amount)
    result = list(map(lambda x, s=start, u=unit: float(x + s)*u, result))
    if amount == 1:
        return result[0]
    else:
        return tuple(result)
def randfrac(num, den):
    """
    Rational Fraction = randfrac(num, den)

    Returns random fraction with numerator in 'num' list and
    denominator in 'den' list. If 'num' or 'den' are numbers
    then numerator is at most 'num' and denominator is at
    most 'den'.
    """
    if not isinstance(num, list):
        num = range(1, num + 1)
    if not isinstance(den, list):
        den = range(2, den + 1)
    den = choice(den)
    num = choice([ i for i in num if gcd(i, den) == 1 ])
    return Rational(num, den)
def coprimes(_x, _y, _num = 2):
    """
    list two coprimes = coprime(int start, int stop)

    Random coprimes.
    """
    if _y - _x < 1:
        sys.exit("Error: coprimes: '_x' < '_y'")
    _ini = list(range(_x, _y + 1))
    _find = 0
    while (_find < _num)&(len(_ini) != 0):
        _i = randrange(len(_ini))
        _coprimes = [ _ini[_i] ]
        _find = 1
        del _ini[_i]
        _list = list(range(_x, _y + 1))
        _list.remove(_coprimes[0])
        while (_find < _num)&(len(_list) !=0):
            _coprimes.append(choice(_list))
            _list.remove(_coprimes[-1])
            _find += 1
            for _i in range(len(_coprimes) - 1):
                if gcd(_coprimes[_i], _coprimes[-1]) != 1:
                    _coprimes.pop()
                    _find -= 1
                    break
    if _find < _num:
        sys.exit("Error: coprimes: Insuficientes coprimos en el intervalo. Línea: " + str(_nline_))
    return _coprimes
def genexpr(_opers, _elems, maxim = 0, factor = False, evaluate = False, cover = None, tostr = str):
    """
    [ symb expr, expr eval(expr), str latex(expr) ]
    = genexpr(str operator list, expr elements list, int maxim, str frac)
    
    Random expression generator.
    """
    global __rand__
    if len(_elems) < 2:
        sys.exit("Error: genexpr: more elements required")
    if len(_opers) + 1 < len(_elems):
        sys.exit("Error: genexpr: more operators required")
    _results = []
    if cover == None:
        __rand__ = Cover()
    else:
        __rand__ = cover
    functions = ["randrange", "randint", "indexes", "jumble"]
    _finding = True
    while _finding:
        _elements = list(_elems)
        _operators = list(_opers)
        if evaluate:
            _elements = [isinstance(x, str) and regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,])", _repl_val_, evalfun(x, functions, "__rand__.")) or tostr(x) for x in _elements]
            _elements = [isinstance(x, str) and tostr(eval(x)) or tostr(x) for x in _elements]
        else:
            _elements = [isinstance(x, str) and regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,])", _repl_val_, evalfun(x, functions, "__rand__.")) or tostr(x) for x in _elements]
        while len(_elements) != 1:
            _iel = __rand__.indexes(len(_elements),2)
            _iop = __rand__.randrange(len(_operators))
            _tmp_ele0 = S(_elements[_iel[0]])
            _tmp_ele1 = S(_elements[_iel[1]])
            if (_operators[_iop] == "/")&(_tmp_ele1 == 0):
                _element = "("+_elements[_iel[0]]+")" + _operators[_iop] + "("+_elements[_iel[1]]+"+1)"
            elif (_operators[_iop] == "**")&(eval("sign("+tostr(_tmp_ele0)+")") == -1)&(eval("("+tostr(_tmp_ele1)+") % 1") != 0):
                _element = "(-("+_elements[_iel[0]]+"))" + _operators[_iop] + "("+_elements[_iel[1]]+")"
            else:
                _element = "("+_elements[_iel[0]]+")" + _operators[_iop] + "("+_elements[_iel[1]]+")"
            _elements[_iel[0]] = _element
            del _elements[_iel[1]]
            del _operators[_iop]
        _solution = S(_elements[0])
        if factor:
            _solution = ifactor(_solution)
        if maxim == 0:
            _finding = False
        else:
            _results.append(_elements[0])
            _results.sort()
            _maxim = max(list(map(abs, numbersstr(str(_solution)))))
            if not next(__rand__):
                sys.exit("Error: genexpr: no se encuentra expresión. Línea: " + str(_nline_))
            if _maxim <= maxim:
                _finding = False
    return _elements[0]
# Arithmetic
#     _         _ _   _                    _   _      
#    / \   _ __(_) |_| |__  _ __ ___   ___| |_(_) ___ 
#   / _ \ | '__| | __| '_ \| '_ ` _ \ / _ \ __| |/ __|
#  / ___ \| |  | | |_| | | | | | | | |  __/ |_| | (__ 
# /_/   \_\_|  |_|\__|_| |_|_| |_| |_|\___|\__|_|\___|
#
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
def divisors(number):
    result = []
    for i in range(1,number):
        if (number % i == 0):
            result.append(i)
    return result
# Improved Sympy
#  ___                                        _ 
# |_ _|_ __ ___  _ __  _ __ _____   _____  __| |
#  | || '_ ` _ \| '_ \| '__/ _ \ \ / / _ \/ _` |
#  | || | | | | | |_) | | | (_) \ V /  __/ (_| |
# |___|_| |_| |_| .__/|_|  \___/ \_/ \___|\__,_|
#               |_|                             
#  ____                              
# / ___| _   _ _ __ ___  _ __  _   _ 
# \___ \| | | | '_ ` _ \| '_ \| | | |
#  ___) | |_| | | | | | | |_) | |_| |
# |____/ \__, |_| |_| |_| .__/ \__, |
#        |___/          |_|    |___/
#
def tryto(x, constructor):
    try:
        result = constructor(x)
        return result
    except ValueError:
        return None
def mapi(list_fun, list_param):
    """
    Scalar product of functions list and parameters list.
    """
    return [ list_fun[i](param) for i, param in enumerate(list_param) ]
def remove(_list, _elem):
    """
    Remove second list elements from the first list and return result.
    """
    _tmp = copy.deepcopy(_list)
    for item_to_remove in _elem:
        _tmp.remove(item_to_remove)
    return _tmp
def subs(expression, *params):
    """
    Generalized substitution where possible
    """
    if isinstance(expression, list):
        return [ subs(item, *params) for item in expression ]
    elif isinstance(expression, dict):
        return { key: subs(value, *params)  for key, value in list(expression.items()) }
    else:
        if hasattr(expression, "subs"):
            if (len(params) == 1)|(not isinstance(params[0], dict)):
                return expression.subs(*params)
            else:
                result = expression
                for i in params:
                    result = result.subs(i)
                return result
        else:
            return expression
def atoms(expression, *params):
    """
    Generalized atoms where possible
    """
    if isinstance(expression, list):
        result = set([])
        for item in expression:
            result |= atoms(item, *params)
        return result
    elif isinstance(expression, dict):
        result = set([])
        for item in list(expression.values()):
            result |= atoms(item, *params)
        return result
    else:
        if hasattr(expression, "atoms"):
            return expression.atoms(*params)
        else:
            return set([])
def roundn(number, __digits__):
    number = float(number)
    if __digits__ > 0:
        if number == 0:
            return 0
        else:
            return round(number, -int(np.floor(np.log10(np.abs(number))) - __digits__ + 1))
    else:
        return round(number, -__digits__)
def rounds(expr, *params):
    return recursive_rounds(N(expr), *params)
def recursive_rounds(expr, *params):
    if isinstance(expr, (Float, float, int, Integer, Zero, One, NegativeOne, Rational, Half)):
        return round(expr, *params)
    elif sympify(expr).atoms(Symbol,un.Unit) == set([]):
        return round(expr, *params)
    elif isinstance(expr, list):
        return [ recursive_rounds(i, *params) for i in expr ]
    elif isinstance(expr, tuple):
        return tuple([ recursive_rounds(i, *params) for i in expr ])
    elif isinstance(expr, dict):
        return { key: recursive_rounds(expr[key], *params) for key in list(expr.keys())}
    elif isinstance(expr, Add):
        result = 0
        for arg in expr.args:
            result += recursive_rounds(arg, *params)
        return result
    elif isinstance(expr, Mul):
        result = 1
        for arg in expr.args:
            result *= recursive_rounds(arg, *params)
        return result
    elif isinstance(expr, Pow):
        return recursive_rounds(expr.base, *params)**recursive_rounds(expr.exp, *params)
    elif isinstance(expr, Equality):
        return Eq(recursive_rounds(expr.lhs, *params), recursive_rounds(expr.rhs, *params))
    elif isinstance(expr, Matrix):
        return Matrix([ [ recursive_rounds(expr[i,j], *params) for j in range(expr.cols) ] for i in range(expr.rows) ])
    # Comienzo de funciones.
    elif isinstance(expr, Function):
        return type(expr)(*( recursive_rounds(i, *params) for i in expr.args ))
    else:
        return expr
def evalf(expression, *params):
    if isinstance(expression, list):
        return [ evalf(item, *params) for item in expression ]
    elif isinstance(expression, dict):
        return { key: evalf(value, *params)  for key, value in list(expression.items()) }
    elif isinstance(expression, str):
        return expression
    else:
        if len(params) == 0:
            return N(expression)
        if params[0] > 0:
            return N(expression,*params)
        else:
            return recursive_rounds(N(expression,*params[1:]),-params[0])
def cevalf(expression, *params):
    if isinstance(expression, float):
        return evalf(expression, *params)
    elif isinstance(expression, list):
        return [ cevalf(item, *params) for item in expression ]
    elif isinstance(expression, dict):
        return { key: cevalf(value, *params)  for key, value in list(expression.items()) }
    elif isinstance(expression, str):
        return expression
    else:
        if hasattr(expression, "atoms"):
            if expression.atoms(Float, float) != set([]):
                return evalf(expression, *params)
            else:
                return expression
        else:
            return expression
# Numerical approximations
#  _   _                           _           _ 
# | \ | |_   _ _ __ ___   ___ _ __(_) ___ __ _| |
# |  \| | | | | '_ ` _ \ / _ \ '__| |/ __/ _` | |
# | |\  | |_| | | | | | |  __/ |  | | (_| (_| | |
# |_| \_|\__,_|_| |_| |_|\___|_|  |_|\___\__,_|_|
#                                  _                 _   _                 
#   __ _ _ __  _ __  _ __ _____  _(_)_ __ ___   __ _| |_(_) ___  _ __  ___ 
#  / _` | '_ \| '_ \| '__/ _ \ \/ / | '_ ` _ \ / _` | __| |/ _ \| '_ \/ __|
# | (_| | |_) | |_) | | | (_) >  <| | | | | | | (_| | |_| | (_) | | | \__ \
#  \__,_| .__/| .__/|_|  \___/_/\_\_|_| |_| |_|\__,_|\__|_|\___/|_| |_|___/
#       |_|   |_|
#
def integrate_rectangle(expr, variable = Symbol('x'), interval = [0,1], steps = 1):
    """
    Maximum and minimum Riemann summations. Approximation using rectangles.
    """
    interval = list(map(Float, interval))
    if len(interval) == 2:
        points = [ (interval[1] - interval[0])/steps*i + interval[0] for i in range(steps+1) ]
    elif len(interval) > 2:
        points = interval
        steps = len(interval) - 1
    else:
        sys.exit("integrate_rectangle: El intervalo debe contener al menos dos puntos.")
    values = list(map(lambda x: expr.subs(variable, x), points))
    max_value = 0
    min_value = 0
    for i in range(steps):
        if values[i] > values[i+1]:
            max_value += values[i]*(points[i+1] - points[i])
            min_value += values[i+1]*(points[i+1] - points[i])
        else:
            max_value += values[i+1]*(points[i+1] - points[i])
            min_value += values[i]*(points[i+1] - points[i])
    return [ min_value, max_value ]
# Graph functions
#   ____                 _         __                  _   _                 
#  / ___|_ __ __ _ _ __ | |__     / _|_   _ _ __   ___| |_(_) ___  _ __  ___ 
# | |  _| '__/ _` | '_ \| '_ \   | |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
# | |_| | | | (_| | |_) | | | |  |  _| |_| | | | | (__| |_| | (_) | | | \__ \
#  \____|_|  \__,_| .__/|_| |_|  |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#                 |_|
#
def getRoots(aNeigh):
    def findRoot(aNode,aRoot):
        while aNode != aRoot[aNode][0]:
            aNode = aRoot[aNode][0]
        return (aNode,aRoot[aNode][1])
    myRoot = {}
    for myNode in list(aNeigh.keys()):
        myRoot[myNode] = (myNode,0)
    for myI in aNeigh:
        for myJ in aNeigh[myI]:
            (myRoot_myI,myDepthMyI) = findRoot(myI,myRoot)
            (myRoot_myJ,myDepthMyJ) = findRoot(myJ,myRoot)
            if myRoot_myI != myRoot_myJ:
                myMin = myRoot_myI
                myMax = myRoot_myJ
                if  myDepthMyI > myDepthMyJ:
                    myMin = myRoot_myJ
                    myMax = myRoot_myI
                myRoot[myMax] = (myMax,max(myRoot[myMin][1]+1,myRoot[myMax][1]))
                myRoot[myMin] = (myRoot[myMax][0],-1)
    myToRet = {}
    for myI in aNeigh:
        if myRoot[myI][0] == myI:
            myToRet[myI] = []
    for myI in aNeigh:
        myToRet[findRoot(myI,myRoot)[0]].append(myI)
    return myToRet
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
def find_all_paths(graph, start, end, path=[]):
    #http://www.python.org/doc/essays/graphs/
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
def find_paths(graph):
    #http://www.ieor.berkeley.edu/~faridani/python.htm
    cycles=[]
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path)==len(graph)):
                    cycles.append(path)
    return cycles
def find_cycles(graph):
    #http://www.ieor.berkeley.edu/~faridani/python.htm
    cycles=[]
    for startnode in graph:
        for endnode in graph:
            newpaths = find_all_paths(graph, startnode, endnode)
            for path in newpaths:
                if (len(path)==len(graph)):
                    if path[0] in graph[path[len(graph)-1]]:
                        path.append(path[0])
                        cycles.append(path)
    return cycles
def find_cycles_from(graph, startnode):
    #http://www.ieor.berkeley.edu/~faridani/python.htm
    cycles=[]
    for endnode in graph:
        newpaths = find_all_paths(graph, startnode, endnode)
        for path in newpaths:
            if (len(path)==len(graph)):
                if path[0] in graph[path[len(graph)-1]]:
                    path.append(path[0])
                    cycles.append(path)
    return cycles
def find_all_cycles_of(graph, start, current = None, path = []):
    if current == None:
        current = start
        path = path + [current]
    else:
        path = path + [current]
        if start == current:
            return [path]
    if graph[current] == []:
        return []
    paths = []
    for node in graph[current]:
        if node not in path[1:]:
            index = graph[node].index(current)
            graph[node].remove(current)
            paths_to_add = find_all_cycles_of(graph, start, node, path)
            graph[node].insert(index, current)
            for path_to_add in paths_to_add:
                paths.append(path_to_add)
    return paths
def find_all_wires(graph):
    wires = []
    for i in list(graph.keys()):
        for j in graph[i]:
            wires.append([j, i])
    first = True
    i = 0
    while i < len(wires):
        line = wires[i]
        if first:
            wires.remove([line[1],line[0]])
            first = False
        if len(graph[line[-1]]) == 2:
            for wire in wires:
                if wire[0] == line[-1]:
                    break
            wires[i].append(wire[1])
            wires.remove(wire)
            wire.reverse()
            wires.remove(wire)
        elif len(graph[line[0]]) == 2:
            for wire in wires:
                if wire[-1] == line[0]:
                    break
            wires[i].insert(0,wire[0])
            wires.remove(wire)
            wire.reverse()
            wires.remove(wire)
        else:
            first = True
            i += 1
    return wires
def complete_graph(p_graph):
    graph = dict(p_graph)
    traduction = []
    for i in list(graph.keys()):
        for j in graph[i]:
            traduction.append([j, i])
    ends = list(set([ i for j in list(graph.keys()) for i in graph[j] ]))
    for i in ends:
        begins = []
        for j in traduction:
            if j[0] == i:
                begins.append(j[1])
        if i in list(graph.keys()):
            graph.update({i: graph[i] + begins})
        else:
            graph.update({i: begins})
    return graph
# Circuits
#   ____ _                _ _       
#  / ___(_)_ __ ___ _   _(_) |_ ___ 
# | |   | | '__/ __| | | | | __/ __|
# | |___| | | | (__| |_| | | |_\__ \
#  \____|_|_|  \___|\__,_|_|\__|___/
#
class Circuit:
    def __init__(self, *params):
        style = ""
        self.def_omega = False
        for param in params:
            if isinstance(param, dict):
                first_key = list(param.keys())[0]
                if isinstance(first_key, str):
                    data = param
                elif isinstance(first_key, int):
                    graph = param
                else:
                    sys.exit("Error: incompatible dictionary key type. Dict = " + str(param))
            elif isinstance(param, str):
                style = param
            elif isinstance(param, (float, Float, un.Unit, Mul, Number)):
                self.omega = param
                self.def_omega = True
        s_omega = Symbol('omega',real=True)
        self.graph = graph
        self.organize_data(data)
        self.complete = complete_graph(self.graph)
        self._abc_ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.nodes = list(set([ k for l in list(graph.keys()) for k in graph[l] ] + list(graph.keys())))
        self.max_node = max(self.nodes)
        self.nnodes = len(self.nodes)
        self.edges = 0
        max_tmp = 0
        for k in list(graph.keys()):
            len_tmp = len(graph[k])
            self.edges += len_tmp
            if max_tmp < len_tmp:
                self.vertex = k
                max_tmp = len_tmp
        self.short_cycles = self.edges - self.nnodes + 1
        self.points = []
        self.IntensityEq = {}
        self.Edges = [ [ 0 for l in self.graph[k] ] for k in list(self.graph.keys()) ]
        self.pstcirc = "\\begin{pspicture}"
        # Choose spatial node distribution
        if style == "":
            if self.edges/self.nnodes*1.2 < max_tmp:
                style = "regpol"
            else:
                style = "grid"
        if style == "regpol":
            self.pstcirc += self.repocirc(len(self.nodes)-1, 3)
        elif style == "grid":
            base = sqrt(self.max_node)
            if isinstance(base, (Integer, Float)):
                high = self.max_node/base
            else:
                base = floor(base)
                high = ceiling(self.max_node/base)
            self.pstcirc += self.gridcirc(base, high, 3)
        else:
            sys.exit("Error: style of circuit must be in [\"regpol\", \"grid\"]")
        # Gets shorter cycles
        all_cycles = []
        all_sets = []
        for k in self.nodes:
            cycles = find_all_cycles_of(self.complete, k)
            for l in cycles:
                l_set = set(l)
                if not l_set in all_sets:
                    all_cycles.append(l)
                    all_sets.append(l_set)
        all_cycles = sorted(all_cycles, key=len)
        complete_set = []
        self.sorted_cycles = []
        for k in all_cycles:
            new_edges = False
            for l in range(len(k)-1):
                new_set = set([k[l],k[l+1]])
                if not new_set in complete_set:
                    complete_set.append(new_set)
                    new_edges = True
            if new_edges:
                self.sorted_cycles.append(k)
        sys.stderr.write("Ciclos independientes teóricos: "+str(self.short_cycles)+" reales: "+str(len(self.sorted_cycles))+"\n")
        # Gets wires ------------------------
        self.wires = find_all_wires(self.complete)
        # Incluye los comando en latex para dibujar el gráfico.
        # Monta el circuito y prepara sus ecuaciones.
        self.pstcirc_incomplete = self.pstcirc
        self.equations = True
        nodes_to_disk = []
        self.NodeEq = [ 0 for k in range(self.nnodes) ]
        for k in range(len(self.wires)):
            nodes_to_disk.append(self.wires[k][0])
            nodes_to_disk.append(self.wires[k][-1])
            # Construimos las ecuaciones de los nodos.
            self.NodeEq[self.nodes.index(self.wires[k][0])] += -Symbol('i'+str(k+1))
            self.NodeEq[self.nodes.index(self.wires[k][-1])] += Symbol('i'+str(k+1))
            for l in range(len(self.wires[k])-1):
                self.pstcirc += self.multidipole(k, self.wires[k][l], self.wires[k][l+1])
        nodes_to_remove = list(set(nodes_to_disk))
        for k in nodes_to_remove:
            nodes_to_disk.remove(k)
        nodes_to_disk = list(set(nodes_to_disk))
        for k in nodes_to_disk:
            self.pstcirc += "\n\\qdisk("+self._abc_[self.nodes.index(k)]+"){2pt}"
        self.pstcirc += "\n\\end{pspicture}"
        for k in range(self.nnodes-1,-1,-1):
            if self.NodeEq[k] == 0:
                del self.NodeEq[k]
        self.equations = False
        # Obtenemos las ecuaciones del circuito.
          # Ecuacionse de las mayas.
        self.CycleEq = []
        for k in self.sorted_cycles:
            self.CycleEq.append(0)
            for l in range(len(k)-1):
                begin = k[l]
                end = k[l+1]
                if begin in list(self.graph.keys()):
                    if end in self.graph[begin]:
                        end = self.graph[begin].index(end)
                        begin = list(self.graph.keys()).index(begin)
                        sig = 1
                    else:
                        tmp = end
                        end = self.graph[end].index(begin)
                        begin = list(self.graph.keys()).index(tmp)
                        sig = -1
                else:
                    tmp = end
                    end = self.graph[end].index(begin)
                    begin = list(self.graph.keys()).index(tmp)
                    sig = -1
                self.CycleEq[-1] += sig*self.Edges[begin][end]
        # Resolvemos las ecuaciones del circuito.
        self.NodeEq = [hasattr(x, "subs") and x.subs(self.IntensityEq) or x for x in self.NodeEq[:-1]] + list(self.IntensityEq.keys())
        for k in range(len(self.NodeEq)-1,0,-1):
            for l in range(k-1,-1,-1):
                if (self.NodeEq[k] == self.NodeEq[l])|(self.NodeEq[k] == -self.NodeEq[l]):
                    del self.NodeEq[k]
                    break
        i_vars = []
        for equation in self.NodeEq:
            i_vars += list(equation.atoms(Symbol))
        i_vars = set(i_vars)
        self.ReducedEq = syst_subs(self.CycleEq, self.NodeEq)
        U_vars = []
        for equation in self.ReducedEq:
            U_vars += list(equation.atoms(Symbol))
        U_vars = set(U_vars)-set([s_omega])
        system_vars = list(i_vars|U_vars)
        A, B = syst2matrix(self.ReducedEq + self.NodeEq, system_vars)
        A, B = erase_units(A), erase_units(B)
        X = (A**-1*B).evalf(__digits__)
        self.Solved = {system_vars[k]: X[k]*uA for k in range(len(system_vars))}
        self.UEdges = {"U_{"+self._abc_[self.nodes.index(k)]+self._abc_[self.nodes.index(l)]+"}": evalf(subs(erase_units(self.Edges[list(self.graph.keys()).index(l)][self.graph[l].index(k)]), erase_units(self.Solved)), __digits__)*uV for l in list(self.graph.keys()) for k in self.graph[l] }
    ## Guarda las magnitudes del circuito en el formato adecuado
    def organize_data(self, data):
        self.i = data['i']
        self.q = data['q']
        def plain_list(data):
            result = True
            for dat in data:
                if isinstance(dat, list):
                    result = False
            return result
        if plain_list(data['U']):
            self.U = []
            for k in self.graph.keys():
                self.U.append([])
                for l in self.graph[k]:
                    self.U[-1].append(data['U'].pop())
        else:
            self.U = data['U']
        if plain_list(data['C']):
            self.C = []
            for k in self.graph.keys():
                self.C.append([])
                for l in self.graph[k]:
                    self.C[-1].append(data['C'].pop())
        else:
            self.C = data['C']
        if plain_list(data['L']):
            self.L = []
            for k in self.graph.keys():
                self.L.append([])
                for l in self.graph[k]:
                    self.L[-1].append(data['L'].pop())
        else:
            self.L = data['L']
        if plain_list(data['R']):
            self.R = []
            for k in self.graph.keys():
                self.R.append([])
                for l in self.graph[k]:
                    self.R[-1].append(data['R'].pop())
        else:
            self.R = data['R']
    ## Devuelve el gráfico del circuito en latex
    def as_str(self, *params):
        cycle = -1
        scale = 0.75
        show_labels = False
        for k in params:
            if isinstance(k, bool):
                show_labels = k
            elif isinstance(k, (int, Integer)):
                cycle = k
            elif isinstance(k, (float, Float)):
                scale *= k
        if cycle == -1:
            result = self.pstcirc
        else:
            result = self.pstcirc_incomplete
            for k in range(len(self.wires)):
                for l in range(len(self.wires[k])-1):
                    if (self.wires[k][l] in self.sorted_cycles[cycle])&(self.wires[k][l+1] in self.sorted_cycles[cycle]):
                        if abs(self.sorted_cycles[cycle].index(self.wires[k][l]) - self.sorted_cycles[cycle].index(self.wires[k][l+1])) == 1:
                            result += self.multidipole(k, self.wires[k][l], self.wires[k][l+1])
                        if (self.wires[k][l] == self.sorted_cycles[cycle][-1])|(self.wires[k][l+1] == self.sorted_cycles[cycle][-1]):
                            if abs(self.sorted_cycles[cycle].index(self.wires[k][l],1) - self.sorted_cycles[cycle].index(self.wires[k][l+1],1)) == 1:
                                result += self.multidipole(k, self.wires[k][l], self.wires[k][l+1])
            result += "\n\\end{pspicture}"
        if not show_labels:
            result = regexp.sub("wire\[intensitylabel=\$[^$]*\$\]", "wire", result)
            result = regexp.sub(",intensitylabel=\$[^$]*\$", "", result)
            result = regexp.sub("\\\\uput\[\-45\][^}]+\}", "", result)
        if scale != 1.:
            result = "\\scalebox{" + str(scale) + "}{" + result + "}"
        return result
    ## Define una malla de puntos para empezar a poner componentes.
    def gridcirc(self, _circ_x_, _circ_y_, factor = 1):
        factor *= 2.2
        _circ_x_ = int(_circ_x_)
        _circ_y_ = int(_circ_y_)
        result = "(-1,-1)(" + str(factor*(_circ_x_-1) + 1) + "," + str(factor*(_circ_y_-1) + 1) + ")"
        result += "\n\\psset{intensitylabeloffset=.25,intensitywidth=2pt}"
        label = 0
        for _y_ in range(_circ_y_):
            for _x_ in range(_circ_x_):
                if _x_ + _circ_x_*_y_ + 1 in self.nodes:
                    result += "\n\\pnode(" + str(factor*_x_) + "," + str(factor*_y_) + "){" + self._abc_[label] + "}"
                    result += "\n\\uput[-45](" + self._abc_[label] + "){" + self._abc_[label] + "}"
                    #result += "\\qdisk("+self._abc_[label]+"){2pt}"
                    label += 1
        return result
    ## Define un polígono regular de puntos para empezar a poner componentes.
    def repocirc(self, lados, radio, angulo = 0):
        radio *= 2.3
        result = "(-" + str((radio) + 1) + ",-" + str((radio) + 1) + ")"
        result += "(" + str((radio) + 1) + "," + str((radio) + 1) + ")"
        result += "\n\\psset{intensitylabeloffset=.25,intensitywidth=2pt}"
        for _i_ in range(lados):
            if _i_ + 1 in self.nodes:
                result += "\n\\pnode("+str((radio*cos(2*pi/lados*(_i_-1)-pi*(1/2+1/lados))).evalf())+","+str((radio*sin(2*pi/lados*(_i_-1)-pi*(1/2+1/lados))).evalf())+"){"+self._abc_[self.nodes.index(_i_+1)]+"}"
                result += "\n\\uput[-45](" + self._abc_[self.nodes.index(_i_+1)] + "){" + self._abc_[self.nodes.index(_i_+1)] + "}"
                #result += "\\qdisk("+self._abc_[label]+"){2pt}"
        result += "\n\\pnode(0,0){"+self._abc_[self.nnodes-1]+"}"
        result += "\n\\uput[-45](" + self._abc_[self.nnodes-1] + "){" + self._abc_[self.nnodes-1] + "}"
        #result += "\\qdisk("+self._abc_[label]+"){2pt}"
        return result
    ## Devuelve el código latex de un cable con componentes aleatorios.
    ## str latex = multidipole(i)
    def multidipole(self, index, begin, end, components = ["U","i","R","C","L"]):
        if isinstance(components, list):
            shuffle(components)
        result = "\n\\multidipole("+self._abc_[self.nodes.index(begin)]+")("+self._abc_[self.nodes.index(end)]+")"
        result += "\n\\wire[intensitylabel=$i_{"+str(index+1)+"}$]"
        if begin in list(self.graph.keys()):
            if end in self.graph[begin]:
                end = self.graph[begin].index(end)
                begin = list(self.graph.keys()).index(begin)
                sig = 1
            else:
                tmp = end
                end = self.graph[end].index(begin)
                begin = list(self.graph.keys()).index(tmp)
                sig = -1
        else:
            tmp = end
            end = self.graph[end].index(begin)
            begin = list(self.graph.keys()).index(tmp)
            sig = -1
        for k in range(len(components)):
            if components[k] == "U":
                if self.U[begin][end] != 0:
                    result += "\n\\Ucc[labelangle=:U,labelInside=2]{$\\color{palatinateblue}"+latex(physics_format(self.U[begin][end]))+"$}"
                    if self.equations:
                        self.Edges[begin][end] += sig*self.U[begin][end]
            if components[k] == "i":
                if (not isinstance(self.i[index], Symbol))&(self.i[index] != 0):
                    result += "\n\\Ucc[labelangle=:U,labelInside=3]{$\\color{palatinateblue}"+latex(physics_format(self.i[index]))+"$}"
                    if self.equations:
                        self.Edges[begin][end] += sig*Symbol('U_{i_{'+self._abc_[begin]+","+self._abc_[self.nodes.index(self.graph[list(self.graph.keys())[begin]][end])]+'}}')
            if components[k] == "R":
                if self.R[begin][end] != 0:
                    result += "\n\\resistor[labelangle=:U]{$\color{palatinateblue}"+latex(physics_format(self.R[begin][end]))+"$}"
                    if self.equations:
                        self.Edges[begin][end] += -sig*self.R[begin][end]*self.i[index]
            if components[k] == "L":
                if self.L[begin][end] != 0:
                    result += "\n\\coil[labelangle=:U,dipolestyle=curved]{$\color{palatinateblue}"+latex(physics_format(self.L[begin][end]))+"$}"
                    if self.equations:
                        if self.def_omega:
                                # En continua una inductancia es un cable.
                                # no se hace nada.
                            if not self.omega == 0:
                                self.Edges[begin][end] += sig*I*self.i[index]*self.omega*self.L[begin][end]
                        else:
                            self.Edges[begin][end] += sig*I*self.i[index]*Symbol('omega',real=True)*self.L[begin][end]
            if components[k] == "C":
                if 1/self.C[begin][end] != 0:
                    result += "\n\\capacitor[labelangle=:U,intensitylabel=$"+latex(physics_format(self.q[index]))+"$"
                    capacity = float(erase_units(self.C[begin][end]))
                    if abs(capacity) < 1e-4:
                        capacity *= 1e6*un.Unit("micro Faraday", "\\;\\mu F")
                    elif abs(capacity) < 1e-1:
                        capacity *= 1e3*un.Unit("mili Faraday", "\\;mF")
                    else:
                        capacity *= uF
                    result += "]{$\\color{palatinateblue}"+latex(physics_format(capacity))+"$}"
                    if self.equations:
                        if self.def_omega:
                            if self.omega == 0:
                                self.Edges[begin][end] += -sig*self.q[index]/self.C[begin][end]
                                self.IntensityEq.update({self.i[index]: 0})
                            else:
                                self.Edges[begin][end] += sig*I*self.i[index]/(self.omega*self.C[begin][end])
                        else:
                            self.Edges[begin][end] += sig*I*self.i[index]/(Symbol('omega',real=True)*self.C[begin][end])
        result += "\n\\wire{}"
        return result
#    def iNodeEquations(self):
#        while 0 in self.Vertexes:
#            self.Vertexes.remove(0)
#        if len(self.Vertexes) < self.vertexes:
#            return self.Vertexes
#        else:
#            return self.Vertexes[1:]
#    def qNodeEquations(self):
#        while 0 in self.qVertexes:
#            self.qVertexes.remove(0)
#        if len(self.qVertexes) < self.vertexes:
#            return self.qVertexes
#        else:
#            return self.qVertexes[1:]
#    def UCycleEquations(self):
#    def UEdgeEquations(self):
#        return self.UEdges
#    def erase_labels(self, dipoles):
#        dipoles = list(dipoles)
#        for k in range(len(dipoles)):
#            if dipoles[k][:5] != r"\wire":
#                dipoles[k] = regexp.sub("\[.*\]", "", dipoles[k])
#                dipoles[k] = regexp.sub("\{.*\}", "{}", dipoles[k])
#        return dipoles
# Plotting
#  ____  _       _   _   _             
# |  _ \| | ___ | |_| |_(_)_ __   __ _ 
# | |_) | |/ _ \| __| __| | '_ \ / _` |
# |  __/| | (_) | |_| |_| | | | | (_| |
# |_|   |_|\___/ \__|\__|_|_| |_|\__, |
#                                |___/
#
from sympy import plotting
# Gráfico 3D de la cinta de Moebius.
# void plot_moebius_strip(str file)
def plot_moebius(_file):
    kwargs = {'title':'Cinta de Moebius', 'xlabel':'x', 'ylabel':'y', 'show':False}
    moebius_strip = plotting.plot3d_parametric_surface((2+(v/2)*cos(u/2))*cos(u), (2+(v/2)*cos(u/2))*sin(u), (v/2)*sin(u/2), (u,0,2*pi), (v,-1,1), **kwargs)
    moebius_strip[0].color = cos(u)
    moebius_strip[0].nb_of_points_u = 100
    moebius_strip[0].nb_of_points_v = 20
    moebius_strip.save(_file)
# Función de la botella de Klein
def klein_bottle_surf(u, v):
    r = 4*(1 - cos(u)/2)
    if (0 <= u) & (u < pi):
        x = 6*cos(u)*(1 + sin(u)) + r*cos(v + pi)
        y = 16 * sin(u)
    else:
        x = 6*cos(u)*(1 + sin(u)) + r*cos(u)*cos(v)
        y = 16*sin(u) + r*sin(u)*cos(v)
    z = r * sin(v)
    return x, y, z
# Gráfico 3D de la botella de Klein.
def plot_klein_bottle(_file):
    kwargs = {'title':'Botella de Klein', 'xlabel':'x', 'ylabel':'y', 'show':False}
    klein_bottle = plotting.plot3d_parametric_surface((lambda u, v: (0 <= u) & (u < pi) and 6*cos(u)*(1 + sin(u)) + 4*(1 - cos(u)/2)*cos(v + pi) or 6*cos(u)*(1 + sin(u)) + 4*(1 - cos(u)/2)*cos(u)*cos(v))(u,v), (lambda u, v: (0 <= u) & (u < pi) and 16 * sin(u) or 16*sin(u) + 4*(1 - cos(u)/2)*sin(u)*cos(v))(u,v), 4*(1 - cos(u)/2)* sin(v), (u,0,2*pi), (v,0,2*pi), **kwargs)
    klein_bottle[0].nb_of_points_u = 100
    klein_bottle[0].nb_of_points_v = 20
    klein_bottle.save(_file)
# Gráfico 3D de un puto de silla.
def plot_saddle_point(_file):
    from sympy import plotting
    kwargs = {'title':'Punto de Silla', 'xlabel':'x', 'ylabel':'y', 'show':False}
    saddle_point = plotting.plot3d(x**2-y**2, (x,-1,1), (y,-1,1), **kwargs)
    saddle_point.save(_file)
# Eval functions
#  _____            _     __                  _   _                 
# | ____|_   ____ _| |   / _|_   _ _ __   ___| |_(_) ___  _ __  ___ 
# |  _| \ \ / / _` | |  | |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
# | |___ \ V / (_| | |  |  _| |_| | | | | (__| |_| | (_) | | | \__ \
# |_____| \_/ \__,_|_|  |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
#
# Sustituye el valor de las variables en la cadena.
def _repl_val_(_x):
    _str = _x.group(1)
    if _str in globals():
        _str = "("+str(eval(_str))+")"
    return _str + _x.group(2)
def _repl_val_wtu_(_x):
    _str = _x.group(1)
    if _str in globals():
        _str = "("+str(erase_units(eval(_str)))+")"
    return _str + _x.group(2)
# Sustituye la evaluacion de todo el patrón.
def _repl_eval_(_x):
    return str(eval(_x.group(0)))
def _repl_pow_rat_(_x):
    __repl_pow_rat_ = "\\sqrt"
    _base = latex(eval(_x.group(1)))
    _num_exp = latex(eval(_x.group(2)))
    _den_exp = latex(eval(_x.group(3)))
    if _den_exp != "2":
        __repl_pow_rat_ += "[" + _den_exp + "]"
    if _num_exp != "1":
        __repl_pow_rat_ += "{{" + _base + "}^{" + _num_exp + "}}"
    else:
        __repl_pow_rat_ += "{" + _base + "}"
    return "Dummy('" + __repl_pow_rat_ + "')"
def _repl_pow_pow_(_x):
    __repl_pow_rat_ = "\\sqrt"
    _base = latex(eval(_x.group(1)))
    _exp = latex(eval(_x.group(2)))
    _exp_exp = latex(eval(_x.group(3)))
    __exp_exp = eval(_exp_exp)
    if __exp_exp < 0:
        if __exp_exp == -1:
            __repl_pow_rat_ += "[" + _exp + "]{" + _base + "}"
        else:
            __repl_pow_rat_ += "[{" + _exp + "}^{" + latex(abs(__exp_exp)) + "}]{" + _base + "}"
    else:
        __repl_pow_rat_ = "{{" + _base + "}^{{" + _exp + "}^{" + _exp_exp + "}}}"
    return "Dummy('" + __repl_pow_rat_ + "')"
# Evalua las variables indicadas
# str symbol = evalvar(str string)
def evalvar(_str):
    return regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_, _str)
# Evalua las funcines indicadas
# str symbol = evalfun(str string, list str )
def evalfun(_str, _list_str = [], obj = ""):
    start = []
    end = []
    for instance in regexp.finditer("([a-zA-Z_][a-zA-Z_0-9\.]*) *\(", _str):
        if (instance.group(1) in _list_str)|(_list_str == []):
            start.append(instance.start(0))
            end.append(instance.end(0))
    start.reverse()
    end.reverse()
    for i in range(len(start)):
        s, e = delim_fun(_str, end[i]-1)
        _str = _str[:start[i]] + str(eval(obj + _str[start[i]:e+1])) + _str[e+1:]
    return _str
# Evalua sustituyendo el valor de las variables y transformando todos
# los átomos en símbolos.
# expression symbol = syeval(str string)
def syeval(_x):
    _s = _x.split("'")
    _n = len(_s)
    _i = 0
    while _i < _n:
        if _s[_i] != "":
            _s[_i] = evalvar( _s[_i])
            _s[_i] = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", "Dummy('\\1')\\2", _s[_i])
            _s[_i] = regexp.sub("(^|[\(\[\{\+\-\*/ ,\:=])(\-?[0-9]*\.?[0-9]+)", "\\1Dummy('\\2')", _s[_i])
            #_s[_i] = _s[_i].replace("/", "*Rational(1)/")
        _i += 2
    return S("'".join(_s))
# Evalua un expression symbol operándolo.
# expression = evalsy(expression symbol syevalexpr)
def evalsy(_x):
    _evals = regexp.sub("Dummy\('(\-?[0-9]*\.?[0-9]+)'\)", "\\1", tostr(_x))
    _evals = regexp.sub("Dummy\('([a-zA-Z_][a-zA-Z_0-9]*)'\)", "\\1", srepr(_x))
    return eval(_evals)
# Function classes
#  _____                 _   _                     _                         
# |  ___|   _ _ __   ___| |_(_) ___  _ __      ___| | __ _ ___ ___  ___  ___ 
# | |_ | | | | '_ \ / __| __| |/ _ \| '_ \    / __| |/ _` / __/ __|/ _ \/ __|
# |  _|| |_| | | | | (__| |_| | (_) | | | |  | (__| | (_| \__ \__ \  __/\__ \
# |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|   \___|_|\__,_|___/___/\___||___/
#
# Devuelve la parte decimal del número.
class decimal(Function):
    nargs = 1

    is_real = True

    def fdiff(self, argindex=1):
        if argindex == 1:
            # property number 1
            return 1
        else:
            raise ArgumentIndexError(self, argindex)
    @classmethod
    def eval(cls, arg):
        if arg.is_number:
            return arg % 1
# Devuelve 0 si es negativo y 1 si no.
class isnneg(Function):
    nargs = 1

    is_real = True

    def fdiff(self, argindex=1):
        if argindex == 1:
            # property number 1
            return 0
        else:
            raise ArgumentIndexError(self, argindex)
    @classmethod
    def eval(cls, arg):
        if arg.is_nonnegative:
            return 1
        elif arg.is_negative:
            return 0
# Anula los valores negativos.
class nneg(Function):
    nargs = 1

    is_real = True

    def fdiff(self, argindex=1):
        if argindex == 1:
            # property number 1
            return isnneg(self.args[0])
        else:
            raise ArgumentIndexError(self, argindex)
    @classmethod
    def eval(cls, arg):
        if arg.is_nonnegative:
            return arg
        elif arg.is_negative:
            return 0
# Sexagesimal classes
#  ____                                 _                 _ 
# / ___|  _____  ____ _  __ _  ___  ___(_)_ __ ___   __ _| |
# \___ \ / _ \ \/ / _` |/ _` |/ _ \/ __| | '_ ` _ \ / _` | |
#  ___) |  __/>  < (_| | (_| |  __/\__ \ | | | | | | (_| | |
# |____/ \___/_/\_\__,_|\__, |\___||___/_|_| |_| |_|\__,_|_|
#                       |___/                               
#       _                         
#   ___| | __ _ ___ ___  ___  ___ 
#  / __| |/ _` / __/ __|/ _ \/ __|
# | (__| | (_| \__ \__ \  __/\__ \
#  \___|_|\__,_|___/___/\___||___/
#
# Pasa de decimal a sexagesimal.
class dec2dms(Function):
    @classmethod
    def eval(cls, arg):
        if isinstance(arg, (int, float, complex)):
            mnt,sec = divmod(arg*3600,60)
            deg,mnt = divmod(mnt,60)
            return deg,mnt,sec
# Clase forma compleja de grados, minutos y segundos.
# Necesita: from __future__ import division
class DMS:
    def __init__(self, degree, minute = 0., second = 0.):
        self.degree = degree
        self.minute = minute
        self.second = second
        self.__reduced__()
    def __repr__(self):
        return str(int(self.degree)) + " gra.  " + str(int(self.minute)) + " min.  " \
        + str(float(self.second)).rstrip("0").rstrip(".") + " sec."
    def _latex(self, printer):
        return str(int(self.degree)) + r"^\circ\ " + str(int(self.minute)) + "'\ " \
        + str(float(self.second)).rstrip("0").rstrip(".") + "''"
    def __reduced__(self):
        # De arriba a abajo
        decimal = self.degree % 1
        self.degree //= 1
        self.minute += decimal * 60
        decimal = self.minute % 1
        self.minute //= 1
        self.second += decimal * 60
        # de abajo a arriba
        self.minute += self.second // 60
        self.second = self.second % 60
        self.degree += self.minute // 60
        self.minute = self.minute % 60
        self.degree = self.degree % 360
    def __float__(self):
        return self.degree + self.minute / 60 + self.second / 3600
    def degrees(self):
        return self.__float__()
    def minutes(self):
        return self.__float__() * 60
    def seconds(self):
        return self.__float__() * 3600
    def __add__(self, other):
        if isinstance(other, DMS):
            degree = self.degree + other.degree
            minute = self.minute + other.minute
            second = self.second + other.second
            return DMS(degree, minute, second)
        else:
            return NotImplemented
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if isinstance(other, DMS):
            degree = self.degree - other.degree
            minute = self.minute - other.minute
            second = self.second - other.second
            return DMS(degree, minute, second)
        elif isinstance(other, (int, float)):
            degree = self.degree - other
            return DMS(degree, self.minute, self.second)
        else:
            return NotImplemented
    def __rsub__(self, other):
        if isinstance(other, DMS):
            degree = other.degree - self.degree
            minute = other.minute - self.minute
            second = other.second - self.second
            return DMS(degree, minute, second)
        elif isinstance(other, (int, float)):
            degree = other - self.degree
            return DMS(degree, self.minute, self.second)
        else:
            return NotImplemented
    def __mul__(self, other):
        if isinstance(other, DMS):
            return NotImplemented
        elif isinstance(other, (int, float)):
            degree = self.degree * other
            minute = self.minute * other
            second = self.second * other
            return DMS(degree, minute, second)
        else:
            return NotImplemented
    def __rmul__(self, other):
        return self.__mul__(other)
    def __div__(self, other):
        if isinstance(other, DMS):
            return self.__float__() / other.__float__()
        elif isinstance(other, (int, float)):
            degree = self.degree / other
            minute = self.minute / other
            second = self.second / other
            return DMS(degree, minute, second)
        else:
            return NotImplemented
    def __rdiv__(self, other):
        if isinstance(other, DMS):
            return other.__float__() / self.__float__()
        else:
            return NotImplemented
    def __truediv__(self, other):
        return self.__div__(other)
    def __rtruediv__(self, other):
        return self.__rdiv__(other)
# Clase forma compleja de horas, minutos y segundos.
# Necesita: from __future__ import division
class HMS:
    def __init__(self, *params):
        nparams = len(params)
        if nparams == 0:
            self.day, self.hour, self.minute, self.second = 0., 0., 0., 0.
        elif nparams == 1:
            self.second = params[0]
            self.day, self.hour, self.minute = 0., 0., 0.
        elif nparams == 2:
            self.minute = params[0]
            self.second = params[1]
            self.day, self.hour = 0., 0.
        elif nparams == 3:
            self.hour = params[0]
            self.minute = params[1]
            self.second = params[2]
            self.day = 0.
        elif nparams == 4:
            self.day = params[0]
            self.hour = params[1]
            self.minute = params[2]
            self.second = params[3]
        else:
            raise ValueError("Incorrect number of parameters.")
        self.__reduced__()
    def round(self, decimals):
        self.second = round(self.second, decimals)
        return self
    def __str__(self):
        result = ""
        if self.day != 0:
            result += str(int(self.day)) + "d "
        if self.hour != 0:
            result += str(int(self.hour)) + "h "
        if self.minute != 0:
            result += str(int(self.minute)) + "m "
        if self.second != 0:
            result += str(float(self.second)).rstrip("0").rstrip(".") + "s"
        if result == "":
            result = "0s"
        return result
    def __repr__(self):
        if self.day == 0:
            return str(int(self.hour)) \
            + " h.  " + str(int(self.minute)) + " min.  " \
            + str(float(self.second)).rstrip("0").rstrip(".") + " seg."
        else:
            return str(int(self.day)) + " días  " + str(int(self.hour)) \
            + " h.  " + str(int(self.minute)) + " min.  " \
            + str(float(self.second)).rstrip("0").rstrip(".") + " seg."
    def _latex(self, printer):
        if self.day == 0:
            return str(int(self.hour)) \
            + r"\;h.\ " + str(int(self.minute)) + r"\;min.\ " \
            + str(float(self.second)).rstrip("0").rstrip(".") + r"\;seg."
        else:
            return str(int(self.day)) + r"\;d\acute{\imath}as\ " + str(int(self.hour)) \
            + r"\;h.\ " + str(int(self.minute)) + r"\;min.\ " \
            + str(float(self.second)).rstrip("0").rstrip(".") + r"\;seg."
    def __reduced__(self):
        # De arriba a abajo
        decimal = self.day % 1
        self.day //= 1
        self.hour += decimal * 24
        decimal = self.hour % 1
        self.hour //= 1
        self.minute += decimal * 60
        decimal = self.minute % 1
        self.minute //= 1
        self.second += decimal * 60
        # de abajo a arriba
        self.minute += self.second // 60
        self.second = self.second % 60
        self.hour += self.minute // 60
        self.minute = self.minute % 60
        self.day += self.hour // 24
        self.hour = self.hour % 24
        if self.day < 0:
            raise ValueError("Instancia HMS negativa.")
    def __float__(self):
        return self.day * 24 + self.hour + self.minute / 60 + self.second / 3600
    def days(self):
        return self.__float__() / 24
    def hours(self):
        return self.__float__()
    def minutes(self):
        return self.__float__() * 60
    def seconds(self):
        return self.__float__() * 3600
    def __add__(self, other):
        if isinstance(other, HMS):
            day = self.day + other.day
            hour = self.hour + other.hour
            minute = self.minute + other.minute
            second = self.second + other.second
            return HMS(day, hour, minute, second)
        else:
            return NotImplemented
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        if isinstance(other, HMS):
            day = self.day - other.day
            hour = self.hour - other.hour
            minute = self.minute - other.minute
            second = self.second - other.second
            return HMS(day, hour, minute, second)
        elif isinstance(other, (int, float)):
            hour = self.hour - other
            return HMS(self.day, hour, self.minute, self.second)
        else:
            return NotImplemented
    def __rsub__(self, other):
        if isinstance(other, HMS):
            day = other.day - self.day
            hour = other.hour - self.hour
            minute = other.minute - self.minute
            second = other.second - self.second
            return HMS(day, hour, minute, second)
        elif isinstance(other, (int, float)):
            hour = other - self.hour
            return HMS(self.day, hour, self.minute, self.second)
        else:
            return NotImplemented
    def __mul__(self, other):
        if isinstance(other, HMS):
            return NotImplemented
        elif isinstance(other, (int, float)):
            day = self.day * other
            hour = self.hour * other
            minute = self.minute * other
            second = self.second * other
            return HMS(day, hour, minute, second)
        else:
            return NotImplemented
    def __rmul__(self, other):
        return self.__mul__(other)
    def __div__(self, other):
        if isinstance(other, HMS):
            return self.__float__() / other.__float__()
        elif isinstance(other, (int, float)):
            day = self.day / other
            hour = self.hour / other
            minute = self.minute / other
            second = self.second / other
            return HMS(day, hour, minute, second)
        else:
            return NotImplemented
    def __rdiv__(self, other):
        if isinstance(other, HMS):
            return other.__float__() / self.__float__()
        else:
            return NotImplemented
    def __truediv__(self, other):
        return self.__div__(other)
    def __rtruediv__(self, other):
        return self.__rdiv__(other)
#############################################################
#############################################################
#############################################################
#                 Herramientas
#############################################################
#############################################################
#############################################################
# Freeze tiene problemas con Symbol ya que desaparece al
# hacerlo str
class Freeze:
    def __init__(self, _str, functions = [expand], frac = "dfrac"):
        _functions = ["randrange", "randint", "indexes", "jumble"]
        self.str = evalfun(evalvar( _str), _functions)
        self.eval = S(self.str)
        self.frac = frac
        self.evol(functions)
    def evol(self, functions):
        self.begin = str2tex(self.str)
        _tmp = self.eval
        for _function in functions:
            _tmp = _function(_tmp)
        self.end = latex(_tmp)
        if self.frac != "frac":
            self.begin = self.begin.replace("\\frac","\\" + self.frac)
            self.end = self.end.replace("\\frac","\\" + self.frac)
#############################################################
#            Clases de generación aleatoria
#############################################################
class Cover:
    def __init__(self, *params):
        name = ""
        self.__first_round__ = True
        self.__space__ = 1
        self.__space_factors__ = []
        for i in params:
            if isinstance(i, (int, float, complex)):
                self.__space__ = int(i)
            elif isinstance(i, str):
                name = i
        if name != "":
            __from__ = inspect.stack()[1]
            __modu__ = inspect.getmodule(__from__[0])
            if __modu__ == None:
                import __main__
                if name in dir(__main__):
                    if isinstance(eval("__main__." + name), Cover):
                        eval("__main__." + name + ".next()")
                    else:
                        exec ("__main__." + name + " = Cover(" + str(self.__space__) + ")")
                else:
                    exec ("__main__." + name + " = Cover(" + str(self.__space__) + ")")
            else:
                exec("import " + __modu__.__name__)
                if name in dir(__modu__):
                    if isinstance(eval(__modu__.__name__ + "." + name), Cover):
                        eval("__modu__." + name + ".next()")
                    else:
                        exec ("__modu__." + name + " = Cover(" + str(self.__space__) + ")")
                else:
                    exec ("__modu__." + name + " = Cover(" + str(self.__space__) + ")")
        else:
            self.__set_space__(self.__space__)
    def __set_space__(self, space):
        self.__space__ = space
        self.__tmp_space__ = 1
        if not hasattr(self, "start"):
            self.__start__ = randrange(self.__space__)
        if self.__space__ != 1:
            self.__randomness__ = self.__start__
            self.__current__ = self.__randomness__
    def next(self):
        if self.__space__ == 1:
            if self.__tmp_space__ == 1:
                sys.exit("Error: Cover.next: no se puede ejecutar next() sin semilla.")
            self.__set_space__(self.__tmp_space__)
        if self.__first_round__:
        # Calcula el generador sólo la primera vez
        # de otro modo podría no recorrer todos los
        # valores puesto que la suma de dos generadores
        # no tiene porqué ser un generador.
            self.generator = 1
            factors_len = len(self.__space_factors__)
            # El contador recorre los números con todas
            # sus cifras distintas de cero.
            def randsafe(x):
                if x == 1:
                    return 0
                else:
                    return randrange(x - 1) + 1
            counter = [ randsafe(self.__space_factors__[i]) for i in range(factors_len) ]
            positio = []
            for i in range(factors_len-1):
                positio.append(self.__space_factors__[i])
                for j in range(i):
                    positio[i] *= self.__space_factors__[j]
            for k in range(self.__space__):
                generator = counter[0] + 1
                for i in range(factors_len-1):
                    generator += counter[i+1]*positio[i]
                if gcd(generator, self.__space__) == 1:
                    self.generator = generator
                    # Sale del bucle sobre k.
                    break
                counter[0] += 1
                for j in range(factors_len):
                    if counter[j] == self.__space_factors__[j] - 1:
                        counter[j] = 0
                        if j == factors_len - 1:
                            counter[0] += 1
                        else:
                            counter[j+1] += 1
                    else:
                        # Sale del bucle sobre j.
                        break
            self.__first_round__ = False
        self.__randomness__ += self.generator
        self.__randomness__ %= self.__space__
        self.__current__ = self.__randomness__
        # Si ha recorrido todas las combinaciones
        # establece state = False
        if self.__randomness__ == self.__start__:
            self.__state__ =  False
        else:
            self.__state__ = True
        return self.__state__
    def covered():
        return self.__state__
    # Función a la que tienen que llamar todas las
    # funciones aleatorias, ya sea directamente o
    # a través de otras.
    def randrange(self, start, stop = None, step = 1):
        if stop == None:
            a, b = 0, start
        else:
            a, b = start, stop
        if self.__space__ == 1:
            result = randrange(start, stop, step)
            self.__start__ += self.__tmp_space__*(result-a)//step
            self.__tmp_space__ *= (b - a)//step
            if self.__first_round__:
                self.__space_factors__.append((b - a)//step)
        else:
            result = self.__current__ % ((b - a)//step)
            result *= step
            result += a
            self.__current__ //= ((b - a)//step)
            if self.__first_round__:
                self.__space_factors__.append((b - a)//step)
        return int(result)
    def randint(self, a, b):
        return self.randrange(a, b + 1)
    def indexes(self, length, amount = 1):
        result = []
        indexes_list = list(range(length))
        for i in range(amount):
            tmp = self.randrange(length)
            result.append(indexes_list[tmp])
            del indexes_list[tmp]
            length -= 1
        return result
    def jumble(self, subject, items = 0):
        result = []
        length = len(subject)
        if items == 0:
            items = length
            return_tuple = True
        else:
            return_tuple = False
        shuffle_list = self.indexes(length, items)
        for i in shuffle_list:
            result.append(subject[i])
        if (items == 1)&(not return_tuple):
            return result[0]
        else:
            return tuple(result)
#############################################################
#############################################################
#############################################################
#           Clases para latex
#############################################################
#############################################################
#############################################################
# Thanks to: http://stackoverflow.com/questions/3867028/converting-a-python-numeric-expression-to-latex
import ast

class LatexVisitor(ast.NodeVisitor):

    def prec(self, n):
        return getattr(self, 'prec_'+n.__class__.__name__, getattr(self, 'generic_prec'))(n)

    def visit_Call(self, n):
        func = self.visit(n.func)
        args = ', '.join(map(self.visit, n.args))
        if func == 'sqrt':
            return '\sqrt{%s}' % args
        else:
            return r'\operatorname{%s}\left(%s\right)' % (func, args)

    def prec_Call(self, n):
        return 1000

    def visit_Name(self, n):
        return n.id

    def prec_Name(self, n):
        return 1000

    def visit_UnaryOp(self, n):
        if self.prec(n.op) > self.prec(n.operand):
            return r'%s \left(%s\right)' % (self.visit(n.op), self.visit(n.operand))
        else:
            return r'%s %s' % (self.visit(n.op), self.visit(n.operand))

    def prec_UnaryOp(self, n):
        return self.prec(n.op)

    def visit_BinOp(self, n):
        if isinstance(n.op, ast.Div):
            return r'\frac{%s}{%s}' % (self.visit(n.left), self.visit(n.right))
        elif isinstance(n.op, ast.FloorDiv):
            return r'\left\lfloor\frac{%s}{%s}\right\rfloor' % (self.visit(n.left), self.visit(n.right))

        if self.prec(n.op) > self.prec(n.left):
            left = r'\left(%s\right)' % self.visit(n.left)
        else:
            left = self.visit(n.left)
        if self.prec(n.op) > self.prec(n.right):
            right = r'\left(%s\right)' % self.visit(n.right)
        # Added becuase 3 - ( 1 + 2 ) fails
        elif self.prec(n.op) == self.prec(n.right) and isinstance(n.op, ast.Sub):
            right = r'\left(%s\right)' % self.visit(n.right)
        else:
            right = self.visit(n.right)


        if isinstance(n.op, ast.Pow):
            return r'%s^{%s}' % (left, self.visit(n.right))
        else:
            return r'%s %s %s' % (left, self.visit(n.op), right)

    def prec_BinOp(self, n):
        return self.prec(n.op)

    def visit_Sub(self, n):
        return '-'

    def prec_Sub(self, n):
        return 300

    def visit_Add(self, n):
        return '+'

    def prec_Add(self, n):
        return 300

    def visit_Mult(self, n):
        return '\\cdot'

    def prec_Mult(self, n):
        return 400

    def visit_Mod(self, n):
        return '\\bmod'

    def prec_Mod(self, n):
        return 500

    def prec_Pow(self, n):
        return 700

    def prec_Div(self, n):
        return 400

    def prec_FloorDiv(self, n):
        return 400

    def visit_LShift(self, n):
        return '\\operatorname{shiftLeft}'

    def visit_RShift(self, n):
        return '\\operatorname{shiftRight}'

    def visit_BitOr(self, n):
        return '\\operatorname{or}'

    def visit_BitXor(self, n):
        return '\\operatorname{xor}'

    def visit_BitAnd(self, n):
        return '\\operatorname{and}'

    def visit_Invert(self, n):
        return '\\operatorname{invert}'

    def prec_Invert(self, n):
        return 800

    def visit_Not(self, n):
        return '\\neg'

    def prec_Not(self, n):
        return 800

    def visit_UAdd(self, n):
        return '+'

    def prec_UAdd(self, n):
        return 800

    def visit_USub(self, n):
        return '-'

    def prec_USub(self, n):
        return 800
    def visit_Num(self, n):
        return str(n.n)

    def prec_Num(self, n):
        return 1000

    def generic_visit(self, n):
        if isinstance(n, ast.AST):
            return r'' % (n.__class__.__name__, ', '.join(map(self.visit, [getattr(n, f) for f in n._fields])))
        else:
            return str(n)

    def generic_prec(self, n):
        return 0
# Usa la clase anterior como función
def str2tex(expr):
    pt = ast.parse(expr)
    return LatexVisitor().visit(pt.body[0].value)
# Compila latex
class ani2eps:
    def __init__(self, name = ""):
        if name == "":
            name = str(self)
            self.name = "__delme__" + name[name.find("0x"):-1] + "___"
        else:
            self.name = "__delme__" + name + "___"
        if not os.path.exists("tmp_ltx"):
            os.makedirs("tmp_ltx")
        self.pic = open("tmp_ltx/" + self.name + ".ltx", "w")
        self.pic.write( "% 'minimal' no permite tamaños de letra como \\Large. Para usarlos cambiar 'minimal' a 'article' u otros.\n" )
        self.pic.write( "\\documentclass[9pt,spanish]{minimal}\n" )
        self.pic.write( "\\usepackage[utf8]{inputenc}\n" )
        self.pic.write( "\\usepackage{babel}\n" )
        self.pic.write( "\\usepackage[T1]{fontenc}\n" )
        self.pic.write( "\\usepackage{amsmath}\n" )
        self.pic.write( "\\usepackage{amssymb}\n" )
        self.pic.write( "\\usepackage{amsxtra}\n" )
        self.pic.write( "\\usepackage{latexsym}\n" )
        self.pic.write( "\\usepackage{bbm}\n" )
        self.pic.write( "\\usepackage{extarrows}\n" )
        self.pic.write( "\\usepackage{braket}\n" )
        self.pic.write( "\\usepackage{units}\n" )
        self.pic.write( "\\usepackage{cancel}\n" )
        self.pic.write( "\\usepackage{eurosym}\n" )
        self.pic.write( "\\usepackage{color}\n" )
        self.pic.write( "\\usepackage{pstricks}\n" )
        self.pic.write( "\\usepackage{pst-fractal}\n" )
        self.pic.write( "\\usepackage{pst-circ}\n" )
        self.pic.write( "\\usepackage{pst-coil}\n" )
        self.pic.write( "\\usepackage{pst-plot}\n" )
        self.pic.write( "\\usepackage{pst-solides3d}\n" )
        self.pic.write( "\\usepackage{pst-eps}\n" )
        self.pic.write( "\\usepackage{pstricks-add}\n" )
        self.pic.write( "\\usepackage{multido}\n" )
        self.pic.write( r"\definecolor{ashgrey}{rgb}{0.7, 0.75, 0.71}" + "\n" )
        self.pic.write( r"\definecolor{earthyellow}{rgb}{0.88, 0.66, 0.37}" + "\n" )
        self.pic.write( r"\definecolor{ferrarired}{rgb}{1.0, 0.11, 0.0}" + "\n" )
        self.pic.write( r"\definecolor{indigo}{rgb}{0.0, 0.25, 0.42}" + "\n" )
        self.pic.write( r"\definecolor{palatinateblue}{rgb}{0.15, 0.23, 0.89}" + "\n" )
        self.pic.write( r"\definecolor{electricblue}{rgb}{0.49, 0.98, 1.0}" + "\n" )
        self.pic.write( r"\definecolor{blue(pigment)}{rgb}{0.2, 0.2, 0.6}" + "\n" )
        self.pic.write( r"\definecolor{green(pigment)}{rgb}{0.0, 0.65, 0.31}" + "\n" )
        self.pic.write( r"\definecolor{red(pigment)}{rgb}{0.93, 0.11, 0.14}" + "\n" )
        self.pic.write( r"\definecolor{burgundy}{rgb}{0.5, 0.0, 0.13}" + "\n" )
        self.pic.write( r"\definecolor{melon}{rgb}{0.99, 0.74, 0.71}" + "\n" )
        self.pic.write( r"\definecolor{peach}{rgb}{1.0, 0.9, 0.71}" + "\n" )
        self.pic.write( r"\definecolor{apricot}{rgb}{0.98, 0.81, 0.69}" + "\n" )
        self.pic.write( r"\definecolor{aqua}{rgb}{0.0, 1.0, 1.0}" + "\n" )
        self.pic.write( r"\definecolor{aquamarine}{rgb}{0.5, 1.0, 0.83}" + "\n" )
        self.pic.write( r"\definecolor{orangered}{rgb}{1.0, 0.27, 0.0}" + "\n" )
        self.pic.write( r"\definecolor{persianrose}{rgb}{1.0, 0.16, 0.64}" + "\n" )
        self.pic.write( r"\definecolor{persianred}{rgb}{0.8, 0.2, 0.2}" + "\n" )
        self.pic.write( r"\definecolor{radicalred}{rgb}{1.0, 0.21, 0.37}" + "\n" )
        self.pic.write( r"\definecolor{uared}{rgb}{0.85, 0.0, 0.3}" + "\n" )
        self.pic.write( r"\definecolor{fluorescentyellow}{rgb}{0.8, 1.0, 0.0}" + "\n" )
        self.pic.write( r"\definecolor{cadetblue}{rgb}{0.37, 0.62, 0.63}" + "\n" )
        self.pic.write( r"\definecolor{burlywood}{rgb}{0.87, 0.72, 0.53}" + "\n" )
        self.pic.write( r"\definecolor{columbiablue}{rgb}{0.61, 0.87, 1.0}" + "\n" )
        self.pic.write( r"\newcommand{\ufrac}[3][.6ex]{\left.\raisebox{#1}{$#2$}\negmedspace{\bigm/}\negmedspace\raisebox{-#1}{$#3$}\right.}" + "\n" )
        self.pic.write( r"\newcommand{\ifrac}[3][.6ex]{\left.\raisebox{#1}{$#2$}\negmedspace\middle/\negmedspace\raisebox{-#1}{$#3$}\right.}" + "\n" )
        self.pic.write( r"\begin{document}" + "\n" )
        self.number = 0
    def append(self, content):
        if content != "":
            if content.find(r"\begin{pspicture}") != -1:
                self.pic.write(r"\begin{TeXtoEPS}" + "\n")
            self.pic.write(content + "\n")
            if content.find(r"\end{pspicture}") != -1:
                self.pic.write(r"\end{TeXtoEPS}" + "\n")
                self.pic.write(r"\clearpage" + "\n")
                self.number += 1
    def make(self):
        self.pic.write(r"\end{document}")
        self.pic.close()
        #call(["latex", "-interaction=nonstopmode", self.name + ".ltx"], stdout=FNULL, stderr=FNULL)
        proc = Popen(["latex", "-output-directory=tmp_ltx", "-interaction=nonstopmode", "-file-line-error", "tmp_ltx/" + self.name + ".ltx"], stdout=PIPE, stderr=FNULL)
        show = 0
        page = 0
        line = proc.stdout.readline()
        while line != b"":
            #sys.stderr.write(line)
            if regexp.search(b"\[1\]$", line) != None:
                page += 1
                sys.stderr.write("\r" + "latex procesó la página " + str(page))
            if regexp.match(b".*:[0-9]*:.*$", line) != None:
                show = 1
            if show == 1:
                sys.stderr.write(line.decode(encoding='UTF-8') + "\n")
            if regexp.match(b"l\\.[0-9]* .*$", line) != None:
                show = 0
            line = proc.stdout.readline()
        sys.stderr.write("\n")
        #call(["dvips", self.name + ".dvi", "-i", "-E", "-o", self.name], stdout=FNULL, stderr=FNULL)
        proc = Popen(["dvips", "tmp_ltx/" + self.name + ".dvi", "-i", "-E", "-o", "tmp_ltx/" + self.name], stdout=FNULL, stderr=PIPE)
        page = 0
        line = proc.stderr.readline()
        while line != b"":
            if regexp.search(b"\[1\] $", line) != None:
                page += 1
                sys.stderr.write("\r" + "dvips procesó la página " + str(page))
            line = proc.stderr.readline()
        sys.stderr.write("\n")
        call(["fnf", "tmp_ltx/" + self.name + "*[0-9]", "-e", "eps", "-n", "6"], stdout=FNULL, stderr=FNULL)
        self.content = ""
#############################################################
#############################################################
#############################################################
#           Clases para física
#############################################################
#############################################################
#############################################################
def n2t(x, ndigits=-3):
    return str(roundn(x, ndigits)).rstrip("0").rstrip(".")
def axesN(x):
    a = str(N(x))
    b = " "
    first = True
    decimal = False
    for i in range(len(a)):
        if first:
            if a[i] in "125":
                b += a[i]
                first = False
            elif a[i] in "34":
                b += "2"
                first = False
            elif a[i] in "67":
                b += "5"
                first = False
            elif a[i] in "89":
                if b[-1] == ".":
                    b = b[:-1] + "1"
                else:
                    b = b[:-1] + "10"
                first = False
            elif a[i] == ".":
                b += "."
                decimal = True
        else:
            if a[i] == "." or decimal:
                break
            else:
                b += "0"
    if b[0] == " ":
        return b[1:]
    else:
        return b
class Animation:
    # k partículas.
    # l vectores de cada partícula.
    # i iteración.
    # j dimensiones.
    # m, n otros...
    def __init__(self, *parameters):
        #self.cine = []
        self.evoled = False
        self.cine = list(erase_units(parameters))
        #for m in parameters:
            #self.cine.append({eval(regexp.sub("(Symbol\('[a-zA-Z][a-zA-Z_]*)[0-9]+('\))", "\\1\\2", srepr(key))) : eval(regexp.sub("(Symbol\('[a-zA-Z][a-zA-Z_]*)[0-9]+('\))", "\\1\\2", srepr(erase_units(value)))) for key, value in m.items() })
        self.k = -1
        self.i = -1
        self.vars = []
        self.v_vars = []
        self.a_vars = []
        self.dim = []
        self.F = []
        self.scale = 1
        self.Fname = []
        self.Falig = []
        self.Funit = []
        self.Fscal = []
        self.particles = len(parameters)
        self.static = [""]
        self.objects = [""]
        self.radius = []
        self.shadows = [""]
        self.sshadows = [""]
        self.interobjs = {}
        self.sinterobjs = {}
        self.interobjslist = []
        self.sinterobjslist = []
        numeric_list = []
        vars_list = []
        vars_dict = {}
        self.numeric = []
        self.explicit_particle = []
        self.numeric_Curve = []
        self.draw_v = []
        self.draw_a = []
        self.draw_track = False
        self.tracks = {}
        self.mov = []
        self.coils = 0
        self.curves = 0
        self.pendulums = 0
        self.puts = 0
        self.bgputs = ""
        self.bgputsmov = False
        for k in range(self.particles):
            self.vars.append([])
            self.v_vars.append([])
            self.a_vars.append([])
            vars_list.append([])
            for key in list(self.cine[k].keys()):
                if isinstance(key, Symbol):
                    vars_list[k].append(key)
                    vars_dict.update({key: k})
                    if str(key).find("_") == -1:
                        self.vars[k].append(key)
            self.vars[k] = sorted(self.vars[k], key=str)
            self.v_vars[k] = { j: eval("Symbol('v_"+str(j)+"')") for j in self.vars[k] }
            self.a_vars[k] = { j: eval("Symbol('a_"+str(j)+"')") for j in self.vars[k] }
            self.dim.append(len(self.vars[k]))
            self.F.append([])
            self.Fname.append([])
            self.Falig.append([])
            self.Funit.append([])
            self.Fscal.append([])
            self.interobjslist.append(set([]))
            self.sinterobjslist.append(set([]))
            self.objects.append("")
            self.radius.append("0")
            self.static.append("")
            self.shadows.append("")
            self.sshadows.append("")
            self.mov.append(True)
            tmp_symbols = atoms(list(self.cine[k].values()), Symbol)
            if (tmp_symbols != set([Symbol('t')]))&(tmp_symbols != set([])):
                if "param" in list(self.cine[k].keys()):
                    self.numeric_Curve.append(k)
                    self.draw_v.append(False)
                    self.draw_a.append(False)
                    continue
                else:
                    numeric_list.append(k)
            else:
                #self.cine[k].update({self.v_vars[k][j]: diff(self.cine[k][j], Symbol('t')) for j in self.vars[k] if not self.v_vars[k][j] in self.cine[k].keys()})
                #self.cine[k].update({self.a_vars[k][j]: diff(self.cine[k][self.v_vars[k][j]], Symbol('t')) for j in self.vars[k] if not self.a_vars[k][j] in self.cine[k].keys()})
                self.explicit_particle.append(k)
            if 'draw_v' in list(self.cine[k].keys()):
                self.draw_v.append(self.cine[k]['draw_v'])
            else:
                self.draw_v.append(True)
            if 'draw_a' in list(self.cine[k].keys()):
                self.draw_a.append(self.cine[k]['draw_a'])
            else:
                self.draw_a.append(True)
            if 'draw_track' in list(self.cine[k].keys()):
                self.draw_track = True
                self.tracks.update({k: self.cine[k]['draw_track']})
                if 'orig_part' in list(self.cine[k].keys()):
                    if not self.cine[k]['orig_part'] in list(self.tracks.keys()):
                        self.tracks.update({self.cine[k]['orig_part']: ""})
        subs_dict = {}
        for k_True in numeric_list:
            # Substituye explicitas en Numérico.
            for k_False in self.explicit_particle:
                self.cine[k_True] = subs(self.cine[k_True], self.cine[k_False])
            # Obtenemos las expresiones integradas.
            for j in self.vars[k_True]:
                if not self.a_vars[k_True][j] in list(self.cine[k_True].keys()):
                    if not self.v_vars[k_True][j] in list(self.cine[k_True].keys()):
                        subs_dict.update({j: self.cine[k_True][j]})
                    else:
                        subs_dict.update({self.v_vars[k_True][j]: self.cine[k_True][self.v_vars[k_True][j]]})
        # Sustituimos expresiones integradas en las demás
        for k_True in numeric_list:
            self.cine[k_True] = subs(self.cine[k_True], subs_dict)
        self.integrates = subs_dict
        # Encontramos dependencias entre partículas.
        depend_graph = {}
        for k in numeric_list:
            tmp_set = set()
            for j in vars_list[k]:
                tmp_set |= sympify(self.cine[k][j]).atoms(Symbol)
            tmp_set -= set(vars_list[k] + [Symbol('t')])
            tmp_list = list(tmp_set)
            tmp_set = set()
            for variable in tmp_list:
                tmp_set |= set([vars_dict[variable]])
            depend_graph.update({k: list(tmp_set)})
        self.numeric = list(getRoots(depend_graph).values())
        self.dim_max = max(self.dim)
        self.mov.append(False)
    def moderate(self, *x):
        x = list(x)
        norm = sqrt(sum([value**2 for value in x]))
        if abs(norm) < 0.01:
            if norm == 0: #abs(norm) < 0.000001:
                fact = 0
                norm = 1 # evitar la división por cero.
            else:
                fact = 0.01
        else:
            if abs(norm) < 1.5:
                return tuple(x)
            else:
                fact = 1.5
        return tuple([value/norm*fact for value in x])
    def __ev__(self, expression, type_of = "a"):
        directory = {'t': self.start + self.i*self.lap}
        if type_of != "t":
            if type_of != "v":
                directory.update({self.a_vars[self.k][self.vars[self.k][j]]: self.__a__[self.k][j][self.i] for j in range(self.dim[self.k])})
            directory.update({self.v_vars[self.k][self.vars[self.k][j]]: self.__v__[self.k][j][self.i] for j in range(self.dim[self.k])})
            directory.update({self.vars[self.k][j]: self.__r__[self.k][j][self.i] for j in range(self.dim[self.k])})
        result = subs(expression, directory)
        #if hasattr(result, "evalf"):
        #    result = result.evalf()
        return float(result)
    def __diff__(self, r_t, prec=1):
        nr_t = len(r_t)
        simul_v = []
        for i in range(0,2,prec):
            simul_v.append((2*r_t[i+3]-9*r_t[i+2]+18*r_t[i+1]-11*r_t[i])/(6*self.lap/self.prec))
        for i in range(i+prec,nr_t-2,prec):
            simul_v.append((-r_t[i+2]+8*r_t[i+1]-8*r_t[i-1]+r_t[i-2])/(12*self.lap/self.prec))
        for i in range(i+prec,nr_t,prec):
            simul_v.append((-2*r_t[i-3]+9*r_t[i-2]-18*r_t[i-1]+11*r_t[i])/(6*self.lap/self.prec))
        return simul_v
    def evol(self, start, end = None, time = 0, prec = 0, fps = 5, extremes = [], estimate = 1, norm = [3, 3, 5], debug = False, simul = "ode", jac = True, integrator = 'vode', method = 'adams'):
        sys.stderr.write("Animation: Comenzando cálculos...\n")
        if end == None:
            end = start
            start = 0
        self.evoled = True
        start = float(erase_units(start))
        end = float(erase_units(end))
        if time == 0:
            time = end - start
        if prec == 0:
            if self.draw_track:
                prec = 10
            else:
                prec = 1
        points = int(time*fps + 1)
        lap = (end - start)/(points - 1)
        self.start = start
        self.end = end
        self.lap = lap
        self.points = points
        self.fps = fps
        self.prec = prec
        self.__tracks__ = [[ [] for j in range(self.dim[k]) ] for k in range(self.particles) ]
        self.__r__ = [[ [] for j in range(self.dim[k]) ] for k in range(self.particles) ]
        self.__v__ = [[ [] for j in range(self.dim[k]) ] for k in range(self.particles) ]
        self.__a__ = [[ [] for j in range(self.dim[k]) ] for k in range(self.particles) ]
        self.Fnum = [ len(self.F[k]) for k in range(self.particles) ]
        ##### Tratamiento función conservada. #####
        ##### Obtención de trayectorias y curvas. #####
        # Cálculos con ecuaciones explícitas.
        sys.stderr.write("Cálculo explicito partículas:")
        for self.k in self.explicit_particle:
            sys.stderr.write(" " + str(self.k))
            if self.k in list(self.tracks.keys()):
                for j, var in enumerate(self.vars[self.k]):
                    for i in range((points-1)*prec+1):
                        self.__tracks__[self.k][j].append(subs(self.cine[self.k][var], {'t': lap/prec*i+start}))
                    for self.i in range(points):
                        self.__r__[self.k][j].append(self.__tracks__[self.k][j][self.i*prec])
                    simul_v = self.__diff__(self.__tracks__[self.k][j])
                    for self.i in range(points):
                        self.__v__[self.k][j].append(simul_v[self.i*prec])
                    self.__a__[self.k][j] = self.__diff__(simul_v, prec)
            else:
                for j, var in enumerate(self.vars[self.k]):
                    for self.i in range(points):
                        self.__r__[self.k][j].append(self.__ev__(self.cine[self.k][var], "t"))
                    self.__v__[self.k][j] = self.__diff__(self.__r__[self.k][j])
                    self.__a__[self.k][j] = self.__diff__(self.__v__[self.k][j])
        sys.stderr.write(".\n")
        ### Comienzo de los integradores numéricos ###
        # Construye la lista de variables de todas las partículas
        # que necesita el integrador y sus valores iniciales.
        sys.stderr.write("Cálculo Numérico partículas:")
        for partic_grp, partic_list in enumerate(self.numeric):
            sys.stderr.write(" " + str(partic_list))
            variables = [Symbol('t')]
            initials = []
            initials.append(start)
            for self.k in partic_list:
                for j in self.vars[self.k]:
                    if self.a_vars[self.k][j] in list(self.cine[self.k].keys()):
                        initials.append(self.cine[self.k][self.v_vars[self.k][j]])
                        initials.append(self.cine[self.k][j])
                        variables.append(self.v_vars[self.k][j])
                        variables.append(j)
                    elif self.v_vars[self.k][j] in list(self.cine[self.k].keys()):
                        initials.append(self.cine[self.k][j])
                        variables.append(j)
            # Construye las ecuaciones.
            equations = []
            for self.k in partic_list:
                for j in self.vars[self.k]:
                    if self.a_vars[self.k][j] in list(self.cine[self.k].keys()):
                        equations.append(self.cine[self.k][self.a_vars[self.k][j]])
                        equations.append(self.v_vars[self.k][j])
                    elif self.v_vars[self.k][j] in list(self.cine[self.k].keys()):
                        equations.append(self.cine[self.k][self.v_vars[self.k][j]])
            if simul == "ode":
                ode_lambda = "lambda t, y: " #"lambda " + str(variables)[1:-1] + ": "
                ode_subs = {variables[j+1]: Symbol('y['+str(j)+']') for j in range(len(variables)-1)}
                ode_system = ode_lambda + str(subs(equations, ode_subs))
                if jac:
                    ode_jacobi = ode_lambda + str(subs(Matrix(equations).jacobian(variables[1:]), ode_subs))[7:-1]
                # Realización de la simulación numérica
                    simulator = ODE(lap/prec, eval(ode_system), initials, jac = eval(ode_jacobi), integrator = integrator, method = method)
                else:
                    simulator = ODE(lap/prec, eval(ode_system), initials, integrator = integrator, method = method)
            elif simul == "rk4":
                ode_lambda = "lambda " + ",".join(map(str, variables)) + ": "
                ode_system = [ eval(ode_lambda + str(equation)) for equation in equations ]
                simulator = RK4(lap/prec, ode_system, initials)
            if debug:
                sys.stderr.write("\n")
                sys.stderr.write(str(variables))
                for iteration in range((points-1)*prec):
                    sys.stderr.write("\n")
                    __tic__ = tm.time()
                    simulator.iterate(1)
                    __toc__ = tm.time()
                    sys.stderr.write(str(iteration + 1) + ": " + str(HMS(__toc__-__tic__).round(4)) + "  ")
                    tmp_x = [ simulator.x[i_last][-1] for i_last in range(simulator.dim) ]

                    sys.stderr.write(str(tmp_x))
            else:
                __tic__ = tm.time()
                simulator.iterate(estimate)
                __toc__ = tm.time()
                sys.stderr.write(" " + str(HMS((__toc__-__tic__)*((points-1)*prec+1)/estimate).round(0)) + " ")
                simulator.iterate((points-1)*prec  -estimate)
            index = 0 # Índice de la variable en el integrador numérico.
            # Recupero los valores de la simulación.
            for self.k in partic_list:
                for j in range(self.dim[self.k]):
                    if self.a_vars[self.k][self.vars[self.k][j]] in list(self.cine[self.k].keys()):
                        index += 2
                        for self.i in range(points):
                            self.__v__[self.k][j].append(simulator.x[index-1][self.i*prec])
                            self.__r__[self.k][j].append(simulator.x[index][self.i*prec])
                        if self.k in list(self.tracks.keys()):
                            self.__tracks__[self.k][j] = simulator.x[index]
                        self.__a__[self.k][j] = self.__diff__(simulator.x[index-1], prec)
                    elif self.v_vars[self.k][self.vars[self.k][j]] in list(self.cine[self.k].keys()):
                        index += 1
                        for self.i in range(points):
                            self.__r__[self.k][j].append(simulator.x[index][self.i*prec])
                        if self.k in list(self.tracks.keys()):
                            self.__tracks__[self.k][j] = simulator.x[index]
                        simul_v = self.__diff__(simulator.x[index])
                        for self.i in range(points):
                            self.__v__[self.k][j].append(simul_v[self.i*prec])
                        self.__a__[self.k][j] = self.__diff__(simul_v, prec)
            # Calculo las variables integradas en términos de las demás.
            for self.k in partic_list:
                for j in range(self.dim[self.k]):
                    if (not self.a_vars[self.k][self.vars[self.k][j]] in list(self.cine[self.k].keys()))&(not self.v_vars[self.k][self.vars[self.k][j]] in list(self.cine[self.k].keys())):
                        nt_t = len(simulator.x[0])
                        nvar = len(variables)
                        r_t = []
                        expression = self.cine[self.k][self.vars[self.k][j]]
                        for i in range(nt_t):
                            instant_subs = {variables[n]: simulator.x[n][i] for n in range(nvar)}
                            r_t.append(subs(expression, instant_subs))
                        for self.i in range(points):
                            self.__r__[self.k][j].append(r_t[self.i*prec])
                        if self.k in list(self.tracks.keys()):
                            self.__tracks__[self.k][j] = r_t
                        simul_v = self.__diff__(r_t)
                        for self.i in range(points):
                            self.__v__[self.k][j].append(simul_v[self.i*prec])
                        self.__a__[self.k][j] = self.__diff__(simul_v, prec)
        sys.stderr.write(".\n")
        # Cálculo de curvas. [ EN PROYECTO ]
#        equations = []
#        for self.k in self.numeric_Curve:
#            for j in self.vars[self.k]:
#                if self.a_vars[self.k][j] in self.cine[self.k].keys():
#                    equations.append(eval(lamb + str(self.cine[self.k][self.a_vars[self.k][j]])))
#                    equations.append(eval(lamb + str(self.v_vars[self.k][j])))
#                elif self.v_vars[self.k][j] in self.cine[self.k].keys():
#                    equations.append(eval(lamb + str(self.cine[self.k][self.v_vars[self.k][j]])))
        self.__ao__ = copy.deepcopy(self.__a__)
        self.__vo__ = copy.deepcopy(self.__v__)
        self.__ro__ = copy.deepcopy(self.__r__)
        ##### Cambio de coordenadas. #####
        for self.k in range(self.particles):
            vars_list = eval(regexp.sub("(Symbol\('[a-zA-Z][a-zA-Z_]*)[0-9]+('\))", "\\1\\2", srepr(self.vars[self.k])))
            if ("x" in list(self.cine[self.k].keys()))|("y" in list(self.cine[self.k].keys()))|("z" in list(self.cine[self.k].keys())):
                lambda_r = "lambda " + str(self.vars[self.k])[1:-1] + ": "
                lambda_v = lambda_r[:-2] + "," + str([self.v_vars[self.k][j] for j in self.vars[self.k]])[1:-1] + ": "
                lambda_a = lambda_v[:-2] + "," + str([self.a_vars[self.k][j] for j in self.vars[self.k]])[1:-1] + ": "
                calc_x, calc_y, calc_z = False, False, False
                if "x" in list(self.cine[self.k].keys()):
                    calc_x = True
                    expr_r = self.cine[self.k]["x"]
                    x_fun = eval(lambda_r + str(expr_r))
                    expr_v = 0
                    for j in self.vars[self.k]:
                        expr_v += diff(expr_r, j)*self.v_vars[self.k][j]
                    vx_fun = eval(lambda_v + str(expr_v))
                    expr_a = 0
                    for j in self.vars[self.k]:
                        expr_a += diff(expr_v, j)*self.v_vars[self.k][j]
                        expr_a += diff(expr_v, self.v_vars[self.k][j])*self.a_vars[self.k][j]
                    ax_fun = eval(lambda_a + str(expr_a))
                if "y" in list(self.cine[self.k].keys()):
                    calc_y = True
                    expr_r = self.cine[self.k]["y"]
                    y_fun = eval(lambda_r + str(expr_r))
                    expr_v = 0
                    for j in self.vars[self.k]:
                        expr_v += diff(expr_r, j)*self.v_vars[self.k][j]
                    vy_fun = eval(lambda_v + str(expr_v))
                    expr_a = 0
                    for j in self.vars[self.k]:
                        expr_a += diff(expr_v, j)*self.v_vars[self.k][j]
                        expr_a += diff(expr_v, self.v_vars[self.k][j])*self.a_vars[self.k][j]
                    ay_fun = eval(lambda_a + str(expr_a))
                if "z" in list(self.cine[self.k].keys()):
                    calc_z = True
                    expr_r = self.cine[self.k]["z"]
                    z_fun = eval(lambda_r + str(expr_r))
                    expr_v = 0
                    for j in self.vars[self.k]:
                        expr_v += diff(expr_r, j)*self.v_vars[self.k][j]
                    vz_fun = eval(lambda_v + str(expr_v))
                    expr_a = 0
                    for j in self.vars[self.k]:
                        expr_a += diff(expr_v, j)*self.v_vars[self.k][j]
                        expr_a += diff(expr_v, self.v_vars[self.k][j])*self.a_vars[self.k][j]
                    az_fun = eval(lambda_a + str(expr_a))
                for self.i in range(points):
                    r = [ self.__r__[self.k][j][self.i] for j in range(self.dim[self.k]) ]
                    v = r + [ self.__v__[self.k][j][self.i] for j in range(self.dim[self.k]) ]
                    a = v + [ self.__a__[self.k][j][self.i] for j in range(self.dim[self.k]) ]
                    if calc_x:
                        self.__a__[self.k][0][self.i] = ax_fun(*a)
                        self.__v__[self.k][0][self.i] = vx_fun(*v)
                    if calc_y:
                        self.__a__[self.k][1][self.i] = ay_fun(*a)
                        self.__v__[self.k][1][self.i] = vy_fun(*v)
                    if calc_z:
                        self.__a__[self.k][2][self.i] = az_fun(*a)
                        self.__v__[self.k][2][self.i] = vz_fun(*v)
                if self.k in list(self.tracks.keys()):
                    for i in range((points-1)*prec+1):
                        r = [ self.__tracks__[self.k][j][i] for j in range(self.dim[self.k]) ]
                        if calc_x:
                            self.__tracks__[self.k][0][i] = x_fun(*r)
                        if calc_y:
                            self.__tracks__[self.k][1][i] = y_fun(*r)
                        if calc_z:
                            self.__tracks__[self.k][2][i] = z_fun(*r)
                    for self.i in range(points):
                        for j in range(self.dim[self.k]):
                            self.__r__[self.k][j][self.i] = self.__tracks__[self.k][j][self.i*prec]
                else:
                    for self.i in range(points):
                        r = [ self.__r__[self.k][j][self.i] for j in range(self.dim[self.k]) ]
                        if calc_x:
                            self.__r__[self.k][0][i] = x_fun(*r)
                        if calc_y:
                            self.__r__[self.k][1][i] = y_fun(*r)
                        if calc_z:
                            self.__r__[self.k][2][i] = z_fun(*r)
            elif len( set(vars_list) - set([Symbol('phi'), Symbol('rho'), Symbol('z')]) ) == 0:
                for self.i in range(points):
                    a = [ self.__a__[self.k][j][self.i] for j in range(2) ]
                    v = [ self.__v__[self.k][j][self.i] for j in range(2) ]
                    r = [ self.__r__[self.k][j][self.i] for j in range(2) ]
                    # Aceleración
                    self.__a__[self.k][0][self.i] = a[1]*cos(r[0]) - r[1]*a[0]*sin(r[0]) - r[1]*v[0]**2*cos(r[0]) - 2*v[1]*v[0]*sin(r[0])
                    self.__a__[self.k][1][self.i] = a[1]*sin(r[0]) + r[1]*a[0]*cos(r[0]) - r[1]*v[0]**2*sin(r[0]) + 2*v[1]*v[0]*cos(r[0])
                    # La tercera componente no cambia.
                    # Velocidad
                    self.__v__[self.k][0][self.i] = v[1]*cos(r[0]) - r[1]*v[0]*sin(r[0])
                    self.__v__[self.k][1][self.i] = v[1]*sin(r[0]) + r[1]*v[0]*cos(r[0])
                    # La tercera componente no cambia.
                # Posición
                if self.k in list(self.tracks.keys()):
                    for i in range((points-1)*prec+1):
                        r = [ self.__tracks__[self.k][j][i] for j in range(2) ]
                        self.__tracks__[self.k][0][i] = r[1]*cos(r[0])
                        self.__tracks__[self.k][1][i] = r[1]*sin(r[0])
                    for self.i in range(points):
                        for j in range(2):
                            self.__r__[self.k][j][self.i] = self.__tracks__[self.k][j][self.i*prec]
                else:
                    for self.i in range(points):
                        r = [ self.__r__[self.k][j][self.i] for j in range(2) ]
                        self.__r__[self.k][0][self.i] = r[1]*cos(r[0])
                        self.__r__[self.k][1][self.i] = r[1]*sin(r[0])
                        # La tercera componente no cambia.
            elif vars_list == [Symbol('phi'), Symbol('rho'), Symbol('x')]:
                for self.i in range(points):
                    a = [ self.__a__[self.k][j][self.i] for j in range(3) ]
                    v = [ self.__v__[self.k][j][self.i] for j in range(3) ]
                    r = [ self.__r__[self.k][j][self.i] for j in range(3) ]
                    # Aceleración
                    self.__a__[self.k][0][self.i] = a[2]
                    self.__a__[self.k][1][self.i] = a[1]*cos(r[0]) - r[1]*a[0]*sin(r[0]) - r[1]*v[0]**2*cos(r[0]) - 2*v[1]*v[0]*sin(r[0])
                    self.__a__[self.k][2][self.i] = a[1]*sin(r[0]) + r[1]*a[0]*cos(r[0]) - r[1]*v[0]**2*sin(r[0]) + 2*v[1]*v[0]*cos(r[0])
                    # Velocidad
                    self.__v__[self.k][0][self.i] = v[2]
                    self.__v__[self.k][1][self.i] = v[1]*cos(r[0]) - r[1]*v[0]*sin(r[0])
                    self.__v__[self.k][2][self.i] = v[1]*sin(r[0]) + r[1]*v[0]*cos(r[0])
                # Posición
                if self.k in list(self.tracks.keys()):
                    for i in range((points-1)*prec+1):
                        r = [ self.__tracks__[self.k][j][i] for j in range(3) ]
                        self.__tracks__[self.k][0][i] = r[2]
                        self.__tracks__[self.k][1][i] = r[1]*cos(r[0])
                        self.__tracks__[self.k][2][i] = r[1]*sin(r[0])
                    for self.i in range(points):
                        for j in range(3):
                            self.__r__[self.k][j][self.i] = self.__tracks__[self.k][j][self.i*prec]
                else:
                    for self.i in range(points):
                        r = [ self.__r__[self.k][j][self.i] for j in range(3) ]
                        self.__r__[self.k][0][self.i] = r[2]
                        self.__r__[self.k][1][self.i] = r[1]*cos(r[0])
                        self.__r__[self.k][2][self.i] = r[1]*sin(r[0])
            elif vars_list == [Symbol('phi'), Symbol('rho'), Symbol('theta')]:
                for self.i in range(points):
                    a = [ self.__a__[self.k][j][self.i] for j in range(3) ]
                    v = [ self.__v__[self.k][j][self.i] for j in range(3) ]
                    r = [ self.__r__[self.k][j][self.i] for j in range(3) ]
                    # Aceleración
                    self.__a__[self.k][0][self.i] = -r[1]*sin(r[0])*sin(r[2])*a[0] - 2*r[1]*sin(r[0])*cos(r[2])*v[0]*v[2] - r[1]*sin(r[2])*cos(r[0])*v[0]**2 - r[1]*sin(r[2])*cos(r[0])*v[2]**2 + r[1]*cos(r[0])*cos(r[2])*a[2] - 2*sin(r[0])*sin(r[2])*v[0]*v[1] + sin(r[2])*cos(r[0])*a[1] + 2*cos(r[0])*cos(r[2])*v[1]*v[2]
                    self.__a__[self.k][1][self.i] = -r[1]*sin(r[0])*sin(r[2])*v[0]**2 - r[1]*sin(r[0])*sin(r[2])*v[2]**2 + r[1]*sin(r[0])*cos(r[2])*a[2] + r[1]*sin(r[2])*cos(r[0])*a[0] + 2*r[1]*cos(r[0])*cos(r[2])*v[0]*v[2] + sin(r[0])*sin(r[2])*a[1] + 2*sin(r[0])*cos(r[2])*v[1]*v[2] + 2*sin(r[2])*cos(r[0])*v[0]*v[1]
                    self.__a__[self.k][2][self.i] = -r[1]*sin(r[2])*a[2] - r[1]*cos(r[2])*v[2]**2 - 2*sin(r[2])*a[1]*a[2] + cos(r[2])*a[1]
                    # Velocidad
                    self.__v__[self.k][0][self.i] = -r[1]*sin(r[0])*sin(r[2])*v[0] + r[1]*cos(r[0])*cos(r[2])*v[2] + sin(r[2])*cos(r[0])*v[1]
                    self.__v__[self.k][1][self.i] = r[1]*sin(r[0])*cos(r[2])*v[2] + r[1]*sin(r[2])*cos(r[0])*v[0] + sin(r[0])*sin(r[2])*v[1]
                    self.__v__[self.k][2][self.i] = -r[1]*sin(r[2])*v[2] + cos(r[2])*v[1]
                # Posición
                if self.k in list(self.tracks.keys()):
                    for i in range((points-1)*prec+1):
                        r = [ self.__tracks__[self.k][j][i] for j in range(3) ]
                        self.__tracks__[self.k][0][i] = r[1]*sin(r[2])*cos(r[0])
                        self.__tracks__[self.k][1][i] = r[1]*sin(r[2])*sin(r[0])
                        self.__tracks__[self.k][2][i] = r[1]*cos(r[2])
                    for self.i in range(points):
                        for j in range(3):
                            self.__r__[self.k][j][self.i] = self.__tracks__[self.k][j][self.i*prec]
                else:
                    for self.i in range(points):
                        r = [ self.__r__[self.k][j][self.i] for j in range(3) ]
                        self.__r__[self.k][0][self.i] = r[1]*sin(r[2])*cos(r[0])
                        self.__r__[self.k][1][self.i] = r[1]*sin(r[2])*sin(r[0])
                        self.__r__[self.k][2][self.i] = r[1]*cos(r[2])
            elif vars_list == [Symbol('rho'), Symbol('upsilon'), Symbol('xi')]:
                for self.i in range(points):
                    a = [ self.__a__[self.k][j][self.i] for j in range(3) ]
                    v = [ self.__v__[self.k][j][self.i] for j in range(3) ]
                    r = [ self.__r__[self.k][j][self.i] for j in range(3) ]
                    # Aceleración
                    self.__a__[self.k][0][self.i] = 2*(8*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])**2*r[0]**2*r[2] - 2*(2*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])*r[0]*v[2] + 4*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])*r[2]*v[0] + (r[0]*a[0] + r[1]*a[1] + r[2]*a[2] + v[0]**2 + v[1]**2 + v[2]**2)*r[0]*r[2])*(r[0]**2 + r[1]**2 + r[2]**2)*r[0] + (r[0]**2 + r[1]**2 + r[2]**2)**2*(r[0]**2*a[2] + 2*r[0]*r[2]*a[0] + 4*r[0]*v[0]*v[2] + 2*r[2]*v[0]**2))/(r[0]**2 + r[1]**2 + r[2]**2)**3
                    self.__a__[self.k][1][self.i] = 2*(8*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])**2*r[0]**2*r[1] - 2*(2*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])*r[0]*v[1] + 4*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])*r[1]*v[0] + (r[0]*a[0] + r[1]*a[1] + r[2]*a[2] + v[0]**2 + v[1]**2 + v[2]**2)*r[0]*r[1])*(r[0]**2 + r[1]**2 + r[2]**2)*r[0] + (r[0]**2 + r[1]**2 + r[2]**2)**2*(r[0]**2*a[1] + 2*r[0]*r[1]*a[0] + 4*r[0]*v[0]*v[1] + 2*r[1]*v[0]**2))/(r[0]**2 + r[1]**2 + r[2]**2)**3
                    self.__a__[self.k][2][self.i] = (8*((r[0]*v[0] + r[1]*v[1] + r[2]*v[2])*r[0] - (r[0]**2 + r[1]**2 + r[2]**2)*v[0])*(r[0]**2 + r[1]**2 + r[2]**2)*r[0]*v[0] - 4*(-(4*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])*v[0] + (r[0]*a[0] + r[1]*a[1] + r[2]*a[2] + v[0]**2 + v[1]**2 + v[2]**2)*r[0])*(r[0]**2 + r[1]**2 + r[2]**2)*r[0] + (r[0]*a[0] + v[0]**2)*(r[0]**2 + r[1]**2 + r[2]**2)**2 + 4*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])**2*r[0]**2)*r[0] + (-r[0]**2 + r[1]**2 + r[2]**2)*(r[0]**2 + r[1]**2 + r[2]**2)**2*a[0])/(r[0]**2 + r[1]**2 + r[2]**2)**3
                    # Velocidad
                    self.__v__[self.k][0][self.i] = 2*((r[0]*v[2] + 2*r[2]*v[0])*(r[0]**2 + r[1]**2 + r[2]**2) - 2*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])*r[0]*r[2])*r[0]/(r[0]**2 + r[1]**2 + r[2]**2)**2
                    self.__v__[self.k][1][self.i] = 2*((r[0]*v[1] + 2*r[1]*v[0])*(r[0]**2 + r[1]**2 + r[2]**2) - 2*(r[0]*v[0] + r[1]*v[1] + r[2]*v[2])*r[0]*r[1])*r[0]/(r[0]**2 + r[1]**2 + r[2]**2)**2
                    self.__v__[self.k][2][self.i] = (4*((r[0]*v[0] + r[1]*v[1] + r[2]*v[2])*r[0] - (r[0]**2 + r[1]**2 + r[2]**2)*v[0])*r[0]**2 + (-r[0]**2 + r[1]**2 + r[2]**2)*(r[0]**2 + r[1]**2 + r[2]**2)*v[0])/(r[0]**2 + r[1]**2 + r[2]**2)**2
                # Posición
                if self.k in list(self.tracks.keys()):
                    for i in range((points-1)*prec+1):
                        r = [ self.__tracks__[self.k][j][i] for j in range(3) ]
                        self.__tracks__[self.k][0][i] = 2*r[0]**2*r[2]/(r[0]**2 + r[1]**2 + r[2]**2)
                        self.__tracks__[self.k][1][i] = 2*r[0]**2*r[1]/(r[0]**2 + r[1]**2 + r[2]**2)
                        self.__tracks__[self.k][2][i] = (1 - 2*r[0]**2/(r[0]**2 + r[1]**2 + r[2]**2))*r[0]
                    for self.i in range(points):
                        for j in range(3):
                            self.__r__[self.k][j][self.i] = self.__tracks__[self.k][j][self.i*prec]
                else:
                    for self.i in range(points):
                        r = [ self.__r__[self.k][j][self.i] for j in range(3) ]
                        self.__r__[self.k][0][self.i] = 2*r[0]**2*r[2]/(r[0]**2 + r[1]**2 + r[2]**2)
                        self.__r__[self.k][1][self.i] = 2*r[0]**2*r[1]/(r[0]**2 + r[1]**2 + r[2]**2)
                        self.__r__[self.k][2][self.i] = (1 - 2*r[0]**2/(r[0]**2 + r[1]**2 + r[2]**2))*r[0]
        # Cambio de origen, necesariamente después del cambio de coordenadas
        # y antes de máximos y mínimos.
        for self.k in range(self.particles):
            if 'orig_part' in list(self.cine[self.k].keys()):
                orig = self.cine[self.k]['orig_part']
                for j in range(self.dim[self.k]):
                    if self.k in list(self.tracks.keys()):
                        for i in range((points-1)*prec+1):
                            self.__tracks__[self.k][j][i] += self.__tracks__[orig][j][i]
                        for self.i in range(points):
                            self.__r__[self.k][j][self.i] = self.__tracks__[self.k][j][self.i*prec]
                            self.__v__[self.k][j][self.i] += self.__v__[orig][j][self.i]
                            self.__a__[self.k][j][self.i] += self.__a__[orig][j][self.i]
                    else:
                        for self.i in range(points):
                            self.__r__[self.k][j][self.i] += self.__r__[orig][j][self.i]
                            self.__v__[self.k][j][self.i] += self.__v__[orig][j][self.i]
                            self.__a__[self.k][j][self.i] += self.__a__[orig][j][self.i]
        # Cálculos de máximos y mínimos.
        if extremes == []:
            self.max = [ [] for j in range(self.dim_max) ]
            self.min = [ [] for j in range(self.dim_max) ]
            for k in range(self.particles):
                for j in range(self.dim[k]):
                    self.max[j].append(max(self.__r__[k][j]))
                    self.min[j].append(min(self.__r__[k][j]))
            for j in range(self.dim_max):
                self.max[j] = max(self.max[j])
                self.min[j] = min(self.min[j])
        else:
            self.max = extremes[1]
            self.min = extremes[0]
        # No dibuja las magnitudes cinemáticas nulas
        for k in range(self.particles):
            way = 0
            vel = 0
            for j in range(self.dim[k]):
                way += sum(map(abs,self.__v__[k][j]))
                vel += sum(map(abs,self.__a__[k][j]))
            if round(way,4) == 0:
                self.draw_v[k] = False
                self.draw_a[k] = False
                self.mov[k] = False
            elif round(vel,4) == 0:
                self.draw_a[k] = False
        # Cálculo del módulo de los vectores.
        # Después de ver magnitudes cinemáticas nulas ya que las omitirá.
        self.__lvl__ = [[] for k in range(self.particles) ]
        self.__lal__ = [[] for k in range(self.particles) ]
        for k in range(self.particles):
            if self.draw_a[k]:
                for i in range(points):
                    self.__lal__[k].append(0)
                    for j in range(self.dim[k]):
                        self.__lal__[k][-1] += self.__a__[k][j][i]**2
                    self.__lal__[k][-1] = sqrt(self.__lal__[k][-1])
            if self.draw_v[k]:
                for i in range(points):
                    self.__lvl__[k].append(0)
                    for j in range(self.dim[k]):
                        self.__lvl__[k][-1] += self.__v__[k][j][i]**2
                    self.__lvl__[k][-1] = sqrt(self.__lvl__[k][-1])
        # Cálculo de las unidades
        widths_list = [self.max[j]-self.min[j] for j in range(self.dim_max) ]
        max_width = max(widths_list)
        self.index_of_max_width = widths_list.index(max_width)
        self.unit = 1/(max_width)
        if norm[0] == 0:
            self.v_unit = 10*self.unit
        else:
            v_list = []
            for k in range(self.particles):
                if self.draw_v[k]:
                    v_list += self.__lvl__[k]
            if len(v_list) == 0:
                v_mode = 0
            else:
                v_mode = mode_cont(v_list)
            if v_mode == 0:
                self.v_unit = 10*self.unit
            else:
                self.v_unit = norm[0]/v_mode
        if norm[1] == 0:
            self.a_unit = 10*self.unit
        else:
            a_list = []
            for k in range(self.particles):
                if self.draw_a[k]:
                    a_list += self.__lal__[k]
            if len(a_list) == 0:
                a_mode = 0
            else:
                a_mode = mode_cont(a_list)
            if a_mode == 0:
                self.a_unit = 10*self.unit
            else:
                self.a_unit = norm[1]/a_mode
        ##### Comienza el cálculo de fuerzas. #####
        self.__F__ = [[[[] for j in range(self.dim[k])] for l in range(self.Fnum[k])] for k in range(self.particles)]
        for self.k in range(self.particles):
            for l in range(self.Fnum[self.k]):
                for j in range(self.dim[self.k]):
                    for self.i in range(points):
                        self.__F__[self.k][l][j].append(self.__ev__(self.F[self.k][l][j]))
        self.__lFl__ = [[[] for l in range(self.Fnum[k])] for k in range(self.particles)]
        for k in range(self.particles):
            for l in range(self.Fnum[k]):
                for i in range(points):
                    self.__lFl__[k][l].append(0)
                    for j in range(self.dim[k]):
                        self.__lFl__[k][l][-1] += self.__F__[k][l][j][i]**2
                    self.__lFl__[k][l][-1] = sqrt(self.__lFl__[k][l][-1])
        if norm[2] == 0:
            F_unit = 10*self.unit
        else:
            F_list = []
            for k in range(self.particles):
                for l in range(self.Fnum[k]):
                    F_list += self.__lFl__[k][l]
            if F_list == []:
                F_mode = 0
            else:
                F_mode = mode_cont(F_list)
            if F_mode == 0:
                F_unit = 10*self.unit
            else:
                F_unit = norm[2]/F_mode
        self.__Fs__ = [[[[] for j in range(self.dim[k])] for l in range(self.Fnum[k])] for k in range(self.particles)]
        for self.k in range(self.particles):
            for l in range(self.Fnum[self.k]):
                for j in range(self.dim[self.k]):
                    for self.i in range(points):
                        self.__Fs__[self.k][l][j].append(self.__F__[self.k][l][j][self.i]*F_unit*self.Fscal[self.k][l])
        # Finaliza el cálculo de fuerzas.
        sys.stderr.write("Animation: Cálculos finalizados.\n")
    def n(self, expression, prec = -1):
        expression = erase_units(expression)
        if prec == -1:
            result = "%f"%(expression)
            result = result.rstrip("0").rstrip(".")
        else:
            result = ("%."+str(prec)+"g")%(expression)
            tmp = result.replace("e",r"\cdot{\scriptstyle 10}^{")
            if tmp != result:
                result = tmp + "}"
                result = regexp.sub("\^\{\+?(\-?)0*([0-9]+)", "^{\\1\\2", result)
        return result
    def animate(self, size = 14, margin = 0.5, digits = 4, viewpoint = [60, 60, 60], lightsrc = [120, 100, 100], origin2d = [], origin3d = [], frame = [], axeslabels = ["x", "y", "z"], grid = True, axes = None, center = True, tail = 0, loop = [], tl = True, exceed = 0, aunit = "m/s^2", vunit = "m/s"):
        # Variables.
        self.size = size
        self.margin = margin
        self.digits = digits
        self.aunit = aunit
        self.vunit = vunit
        if frame == []:
            frame = [[-10, -10, -10], [10, 10, 10]]
        else:
            if (len(frame[0]) == 2)&(origin2d == []):
                origin2d = frame[0]
            if (len(frame[0]) == 3)&(origin3d == []):
                origin3d = frame[0]
        if axes == None:
            if self.dim_max == 3:
                axes = "frame"
            else:
                axes = "real"
        shadows = False
        for k in range(self.particles):
            if "shadows" in list(self.cine[k].keys()):
                shadows = True
                break
        # Origen de la imagen.
        if origin2d == []:
            origin2d = [-10, -10]
        if origin3d == []:
            origin3d = [-10, -10, -10]
        self.origin = []
        for k in range(self.particles):
            if self.dim[k] == 3:
                self.origin.append(origin3d)
            elif self.dim[k] == 2:
                self.origin.append(origin2d)
            else:
                self.origin.append(-1)
        self.origin3d = origin3d
        self.origin2d = origin2d
        if center:
            self.orig_center = []
            for j in range(self.dim_max):
                self.orig_center.append((self.max[j]+self.min[j]-1/self.unit)/2)
        else:
            self.orig_center = self.min
        # Máximos en las coordenadas de la imagen picture.
        self.ref_width = frame[1][self.index_of_max_width]-frame[0][self.index_of_max_width]
        pic_width = []
        for j in range(self.dim_max):
            pic_width.append( frame[1][j]-frame[0][j] )
        self.pmmax = [frame[1][0]+self.margin/size*pic_width[0], frame[1][1]+self.margin/size*pic_width[1]]
        self.pmmin = [frame[0][0]-self.margin/size*pic_width[0], frame[0][1]-self.margin/size*pic_width[1]]
        self.pmax = [frame[1][0], frame[1][1]]
        self.pmin = [frame[0][0], frame[0][1]]
        # Array de funciones para convertir de realidad
        # a marco de la animación en el documento.
        self.vars2pic = []
        for j in range(self.dim_max):
            if self.max[j] == self.min[j]:
                self.vars2pic.append( lambda variable2pic: variable2pic )
            elif exceed != 0:
                def tmp_fun(variable2pic, index_of_dim=j, cent_orig=self.orig_center[j], factor_exceed=exceed, frame_width=self.ref_width):
                    tmp_value = round(frame_width*self.unit*(variable2pic - cent_orig)+self.origin[self.k][index_of_dim],3)
                    if tmp_value > factor_exceed*self.pmmax[index_of_dim]:
                        return factor_exceed*self.pmmax[index_of_dim]
                    if tmp_value < factor_exceed*self.pmmin[index_of_dim]:
                        return factor_exceed*self.pmmin[index_of_dim]
                    return tmp_value
                self.vars2pic.append( tmp_fun )
            else:
                self.vars2pic.append( lambda variable2pic, index_of_dim=j, cent_orig=self.orig_center[j], frame_width=self.ref_width: round(frame_width*self.unit*(variable2pic - cent_orig)+self.origin[self.k][index_of_dim],3) )
        self.v_vars2pic = [ lambda v_variable2pic: round(self.v_unit*v_variable2pic,3) for j in range(self.dim_max) ]
        self.a_vars2pic = [ lambda a_variable2pic: round(self.a_unit*a_variable2pic,3) for j in range(self.dim_max) ]
        ##### Coordenadas en la imagen. #####
        self.__tracksp__ = [[ [] for j in range(self.dim[k]) ] for k in range(self.particles) ]
        self.__rp__ = [[ [] for j in range(self.dim[k]) ] for k in range(self.particles) ]
        for k in range(self.particles):
            for j in range(self.dim[k]):
                if k in list(self.tracks.keys()):
                    for i in range((self.points-1)*self.prec+1):
                        self.__tracksp__[k][j].append(self.vars2pic[j](self.__tracks__[k][j][i]))
                    for i in range(self.points):
                        self.__rp__[k][j].append(self.__tracksp__[k][j][i*self.prec])
                else:
                    for i in range(self.points):
                        self.__rp__[k][j].append(self.vars2pic[j](self.__r__[k][j][i]))
        # Encuentra el punto en el que se repite la trayectoria.
        if loop != []:
            if len(loop) == 1:
                start_point = self.fps + 4
            else:
                start_point = round(self.fps*loop[1]) + 1
            for i in range(int(start_point), self.points):
                env = True
                for k in range(self.particles):
                    for j in range(self.dim[k]):
                        if abs(self.__r__[k][j][i] - self.__r__[k][j][0]) > abs(self.__r__[k][j][loop[0]] - self.__r__[k][j][0]):
                            env = False
                            break
                        elif abs(self.__v__[k][j][i] - self.__v__[k][j][0]) > abs(self.__v__[k][j][loop[0]] - self.__v__[k][j][0]):
                            env = False
                            break
                    if not env:
                        break
                if env:
                    self.points = i + 1
                    break
        if tl:
            dynamic_viewpoint = False
        else:
            dynamic_viewpoint = True
        head_picture = ""
        latex_grid  = r"\psSolid[object=grille,base=0 20 0 20,ngrid=4 4,linecolor=lightgray,RotX=-90]("+n2t(origin3d[0])+","+n2t(origin3d[1])+","+n2t(origin3d[2]+20)+")"
        latex_grid += r"\psSolid[object=grille,base=0 20 0 20,ngrid=4 4,linecolor=lightgray,RotY=90]("+n2t(origin3d[0])+","+n2t(origin3d[1])+","+n2t(origin3d[2]+20)+")"
        latex_grid += r"\psSolid[object=grille,base=0 20 0 20,ngrid=4 4,linecolor=lightgray]("+n2t(origin3d[0])+","+n2t(origin3d[1])+","+n2t(origin3d[2])+")"
        latex_plan  = r"\psSolid[object=plan,definition=equation,args={[1 0 0 "+n2t(-origin3d[0])+"] 90},base="+n2t(origin3d[1])+" "+n2t(origin3d[1]+20)+" "+n2t(origin3d[2])+" "+n2t(origin3d[2]+20)+r",name=planX,action=none]"
        latex_plan += r"\psSolid[object=plan,definition=equation,args={[0 1 0 "+n2t(-origin3d[1])+"] -90},base="+n2t(origin3d[2])+" "+n2t(origin3d[2]+20)+" "+n2t(origin3d[0])+" "+n2t(origin3d[0]+20)+r",name=planY,action=none]"
        latex_plan += r"\psSolid[object=plan,definition=equation,args={[0 0 1 "+n2t(-origin3d[2])+"]},base="+n2t(origin3d[0])+" "+n2t(origin3d[0]+20)+" "+n2t(origin3d[1])+" "+n2t(origin3d[1]+20)+r",name=planZ,action=none]"
        latex_axes  = r"\psLineIIID[linecolor=black,linewidth=1pt,arrows=->]("+n2t(origin3d[0])+","+n2t(origin3d[1])+","+n2t(origin3d[2])+")("+n2t(origin3d[0]+20)+","+n2t(origin3d[1])+","+n2t(origin3d[2])+")"+r"\psPoint("+n2t(origin3d[0]+20.5)+","+n2t(origin3d[1])+","+n2t(origin3d[2])+r"){XLABEL}\rput[b](XLABEL){$"+axeslabels[0]+"$}"
        latex_axes += r"\psLineIIID[linecolor=black,linewidth=1pt,arrows=->]("+n2t(origin3d[0])+","+n2t(origin3d[1])+","+n2t(origin3d[2])+")("+n2t(origin3d[0])+","+n2t(origin3d[1]+20)+","+n2t(origin3d[2])+")"+r"\psPoint("+n2t(origin3d[0])+","+n2t(origin3d[1]+20.5)+","+n2t(origin3d[2])+r"){YLABEL}\rput[b](YLABEL){$"+axeslabels[1]+"$}"
        latex_axes += r"\psLineIIID[linecolor=black,linewidth=1pt,arrows=->]("+n2t(origin3d[0])+","+n2t(origin3d[1])+","+n2t(origin3d[2])+")("+n2t(origin3d[0])+","+n2t(origin3d[1])+","+n2t(origin3d[2]+20)+")"+r"\psPoint("+n2t(origin3d[0])+","+n2t(origin3d[1])+","+n2t(origin3d[2]+20.5)+r"){ZLABEL}\rput[b](ZLABEL){$"+axeslabels[2]+"$}"
        # Definimos variables que podremos usar en las inserciones.
        #var('unit maxx minx rmaxx rminx maxy miny rmaxy rminy')
        psset = r"\psset{unit="+n2t(size/self.ref_width)+"cm"
        bpicture = r"\begin{pspicture}("+str(round(self.pmmin[0],3))+","+str(round(self.pmmin[1],3))+")("+str(round(self.pmmax[0],3))+","+str(round(self.pmmax[1],3))+")"
        if self.dim_max == 3:
            self.time_dependent = False
            viewpoint = erase_units(viewpoint)
            pviewpoint = []
            for icoord in range(3):
                tmp0 = str(viewpoint[icoord])
                pviewpoint.append(regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0))
            if self.time_dependent:
                dynamic_viewpoint = True
                psset += ",viewpoint='+str(round(float(" + pviewpoint[0] + "),3))+' '+str(round(float(" + pviewpoint[1] + "),3))+' '+str(round(float(" + pviewpoint[2] + "),3))+'"
            else:
                psset += ",viewpoint="+str(round(eval(pviewpoint[0]) + origin3d[0],3))+" "+str(round(eval(pviewpoint[1]) + origin3d[1],3))+" "+str(round(eval(pviewpoint[2]) + origin3d[2],3))
            if isinstance(lightsrc, list):
                psset += ",lightsrc="+n2t(lightsrc[0])+" "+n2t(lightsrc[1])+" "+n2t(lightsrc[2])
            else:
                psset += ",lightsrc="+lightsrc
            if grid:
                head_picture += latex_grid
            if axes == "frame":
                head_picture += latex_axes
            if shadows:
                psset += ",solidmemory"
                #self.sshadows[-1] += latex_plan
                #self.shadows[-1] += latex_plan
        else:
            if axes == "frame":
                if (self.min == frame[0][:2])&(self.max == frame[1][:2]):
                    head_picture += r"\psaxes[linewidth=1pt,labels=all,Dx="+axesN(pic_width[0]/size)+",Dy="+axesN(pic_width[1]/size)+"]{->}("+n2t(frame[0][0])+","+n2t(frame[0][1])+")("+n2t(frame[0][0])+","+n2t(frame[0][1])+")("+n2t(frame[1][0])+","+n2t(frame[1][1])+")"
                else:
                    head_picture += r"\psline[linecolor=black,linewidth=1pt]{->}("+n2t(origin2d[0])+","+n2t(origin2d[1])+")("+n2t(origin2d[0]+20)+","+n2t(origin2d[1])+r")\rput[l]("+n2t(origin2d[0]+20.2)+","+n2t(origin2d[1])+"){$"+axeslabels[0]+"$}"
                    head_picture += r"\psline[linecolor=black,linewidth=1pt]{->}("+n2t(origin2d[0])+","+n2t(origin2d[1])+")("+n2t(origin2d[0])+","+n2t(origin2d[1]+20)+r")\rput[b]("+n2t(origin2d[0])+","+n2t(origin2d[1]+20.2)+"){$"+axeslabels[1]+"$}"
            elif axes == "center":
                if (self.min == frame[0][:2])&(self.max == frame[1][:2]):
                    head_picture += r"\psaxes[linewidth=1pt,labels=all,Dx="+axesN(pic_width[0]/size)+",Dy="+axesN(pic_width[1]/size)+"]{->}(0,0)("+n2t(frame[0][0])+","+n2t(frame[0][1])+")("+n2t(frame[1][0])+","+n2t(frame[1][1])+")"
                else:
                    head_picture += r"\psline[linecolor=black,linewidth=1pt]{->}("+n2t(origin2d[0])+","+n2t(origin2d[1]+10)+")("+n2t(origin2d[0]+20)+","+n2t(origin2d[1]+10)+r")\rput[l]("+n2t(origin2d[0]+20.2)+","+n2t(origin2d[1]+10)+"){$"+axeslabels[0]+"$}"
                    head_picture += r"\psline[linecolor=black,linewidth=1pt]{->}("+n2t(origin2d[0]+10)+","+n2t(origin2d[1])+")("+n2t(origin2d[0]+10)+","+n2t(origin2d[1]+20)+r")\rput[b]("+n2t(origin2d[0]+10)+","+n2t(origin2d[1]+20.2)+"){$"+axeslabels[1]+"$}"
            elif axes == "real":
                if (self.min == frame[0][:2])&(self.max == frame[1][:2]):
                    head_picture += r"\psaxes[linewidth=1pt,labels=all,Dx="+axesN(pic_width[0]/size)+",Dy="+axesN(pic_width[1]/size)+"]{->}(0,0)("+n2t(frame[0][0])+","+n2t(frame[0][1])+")("+n2t(frame[1][0])+","+n2t(frame[1][1])+")"
                else:
                    head_picture += r"\psline[linecolor=black,linewidth=1pt]{->}("+n2t(origin2d[0])+","+n2t(self.vars2pic[1](0))+")("+n2t(origin2d[0]+20)+","+n2t(self.vars2pic[1](0))+r")\rput[l]("+n2t(origin2d[0]+20.2)+","+n2t(self.vars2pic[1](0))+"){$"+axeslabels[0]+"$}"
                    head_picture += r"\psline[linecolor=black,linewidth=1pt]{->}("+n2t(self.vars2pic[0](0))+","+n2t(origin2d[1])+")("+n2t(self.vars2pic[0](0))+","+n2t(origin2d[1]+20)+r")\rput[b]("+n2t(self.vars2pic[0](0))+","+n2t(origin2d[1]+20.2)+"){$"+axeslabels[1]+"$}"
        psset += "}"
        # Preparación de leyenda.
        if self.bgputs != "":
            if self.bgputsmov:
                self.objects[-1] += r"\\rput[tl]("+n2t(self.pmmin[0])+","+n2t(self.pmmax[1])+r"){\\parbox{"+n2t(size)+"cm}{"+self.bgputs+"}}"
            else:
                self.static[-1] += r"\\rput[tl]("+n2t(self.pmmin[0])+","+n2t(self.pmmax[1])+r"){\\parbox{"+n2t(size)+"cm}{"+self.bgputs+"}}"
        # Inicialización
        objects2d = []
        objects3d = []
        interobjsset = set([])
        for iset in list(self.interobjs.keys()):
            interobjsset |= iset
        sinterobjsset = set([])
        for iset in list(self.sinterobjs.keys()):
            sinterobjsset |= iset
        for k in range(self.particles):
            if self.dim[k] == 3:
                objects3d.append(k)
            else:
                objects2d.append(k)
        pspicture = ani2eps()
        frame = 0
        self.i = 0
        sys.stderr.write("\r" + "Procesando fotograma " + str(self.i+1) + " de " + str(self.points))
        if tl:
            name = str(self)
            name = "__delme__" + name[name.find("0x"):-1]
            timeline = open("tmp_ltx/" + name + ".tln", "w")
            # Fotograma de fondo
            pspicture.append( eval("'" + psset + "'") )
            pspicture.append( bpicture )
            pspicture.append( head_picture )
            pspicture.append( eval("'" + self.static[-1] + "'") )
            if shadows:
                pspicture.append( latex_plan )
                pspicture.append( eval("'" + self.sshadows[-1] + "'") )
                for self.k in range(self.particles):
                    pspicture.append( eval("'" + self.sshadows[self.k] + "'") )
                pspicture.append( r"\composeSolid" )
            # Colocación de objetos estáticos. INI
            distance = []
            for self.k in objects3d:
                distance.append(self.__rp__[self.k][0][self.i]*self.__ev__(viewpoint[0]) + self.__rp__[self.k][1][self.i]*self.__ev__(viewpoint[1]) + self.__rp__[self.k][2][self.i]*self.__ev__(viewpoint[2]))
            tmp_dist = [x for (y,x) in sorted(zip(distance,objects3d))]
            for self.k in tmp_dist:
                pspicture.append( eval("'" + self.static[self.k] + "'") )
                # Objetos entre dos partículas.
                if self.k in sinterobjsset:
                    tmp_obj = sorted(list(self.sinterobjslist[self.k]), key=lambda x, l=tmp_dist: l.index(x))
                    for k_dest in tmp_obj:
                        tmp_set = frozenset([self.k,k_dest])
                        value = self.sinterobjs[tmp_set]
                        if value[0]:
                            tmp = list(tmp_set)
                            __RAB__  = sqrt((self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i])**2+(self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])**2)
                            __rAB__  = sqrt(__RAB__**2+(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i])**2)
                            __angY__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i], __RAB__)
                            __angZ__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i], self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])
                            pspicture.append( eval("'" + value[1] + "'") )
                            self.sinterobjs[tmp_set][0] = False
                        else:
                            self.sinterobjs[tmp_set][0] = True
            for self.k in objects2d:
                pspicture.append( eval("'" + self.static[self.k] + "'") )
                # Objetos entre dos partículas.
                if self.k in sinterobjsset:
                    for key, value in list(self.sinterobjs.items()):
                        if self.k in key:
                            if value[0]:
                                pspicture.append( eval("'" + value[1] + "'") )
                                self.sinterobjs[key][0] = False
                            else:
                                self.sinterobjs[key][0] = True
            # Colocación de objetos estáticos. FIN
            pspicture.append( r"\end{pspicture}" )
            # Fotograma presentación
            pspicture.append( eval("'" + psset + "'") )
            pspicture.append( bpicture )
            pspicture.append( eval("'" + self.objects[-1] + "'") )
            if shadows:
                pspicture.append( latex_plan )
                pspicture.append( eval("'" + self.shadows[-1] + "'") )
                for self.k in range(self.particles):
                    pspicture.append( eval("'" + self.shadows[self.k] + "'") )
                pspicture.append( r"\composeSolid" )
            # Colocación de objetos. INI
            for self.k in tmp_dist:
                pspicture.append( eval("'" + self.objects[self.k] + "'") )
                # Objetos entre dos partículas.
                if self.k in interobjsset:
                    tmp_obj = sorted(list(self.interobjslist[self.k]), key=lambda x, l=tmp_dist: l.index(x))
                    for k_dest in tmp_obj:
                        tmp_set = frozenset([self.k,k_dest])
                        value = self.interobjs[tmp_set]
                        if value[0]:
                            tmp = list(tmp_set)
                            __RAB__  = sqrt((self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i])**2+(self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])**2)
                            __rAB__  = sqrt(__RAB__**2+(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i])**2)
                            __angY__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i], __RAB__)
                            __angZ__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i], self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])
                            pspicture.append( eval("'" + value[1] + "'") )
                            self.interobjs[tmp_set][0] = False
                        else:
                            self.interobjs[tmp_set][0] = True
            for self.k in objects2d:
                pspicture.append( eval("'" + self.objects[self.k] + "'") )
                # Objetos entre dos partículas.
                if self.k in interobjsset:
                    for key, value in list(self.interobjs.items()):
                        if self.k in key:
                            if value[0]:
                                pspicture.append( eval("'" + value[1] + "'") )
                                self.interobjs[key][0] = False
                            else:
                                self.interobjs[key][0] = True
            # Colocación de objetos. FIN
            pspicture.append( r"\end{pspicture}" )
        # Preparación inicio
        bit = str(tail*2)
        frame += 1
        if dynamic_viewpoint:
            bit = "1"
            # Si el punto de vista cambia no hay material estático
            self.objects[-1] = self.static[-1] + self.objects[-1]
            # No se hace lo mismo con shadows[-1] y sshadows[-1]
            # dado que contienen lo mismo.
            for k in range(self.particles):
                self.objects[k] = self.static[k] + self.objects[k]
                self.shadows[k] = self.sshadows[k] + self.shadows[k]
                self.interobjslist[k] |= self.sinterobjslist[k]
            interobjsset |= sinterobjsset
            self.interobjs.update(self.sinterobjs)
        if tl:
            timeline.write("::0x"+bit+",1x1\n")
        # Primer fotograma en movimiento
        pspicture.append( eval("'" + psset + "'") )
        pspicture.append( bpicture )
        if dynamic_viewpoint:
            pspicture.append( head_picture )
        pspicture.append( eval("'" + self.objects[-1] + "'") )
        if shadows:
            pspicture.append( latex_plan )
            pspicture.append( eval("'" + self.shadows[-1] + "'") )
            for self.k in range(self.particles):
                pspicture.append( eval("'" + self.shadows[self.k] + "'") )
            pspicture.append( r"\composeSolid" )
        # Colocación de objetos. INI
        distance = []
        for self.k in objects3d:
            distance.append(self.__rp__[self.k][0][self.i]*self.__ev__(viewpoint[0]) + self.__rp__[self.k][1][self.i]*self.__ev__(viewpoint[1]) + self.__rp__[self.k][2][self.i]*self.__ev__(viewpoint[2]))
        tmp_dist = [x for (y,x) in sorted(zip(distance,objects3d))]
        for self.k in tmp_dist:
            pspicture.append( eval("'" + self.objects[self.k] + "'") )
            # Objetos entre dos partículas.
            if self.k in interobjsset:
                tmp_obj = sorted(list(self.interobjslist[self.k]), key=lambda x, l=tmp_dist: l.index(x))
                for k_dest in tmp_obj:
                    tmp_set = frozenset([self.k,k_dest])
                    value = self.interobjs[tmp_set]
                    if value[0]:
                        tmp = list(tmp_set)
                        __RAB__  = sqrt((self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i])**2+(self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])**2)
                        __rAB__  = sqrt(__RAB__**2+(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i])**2)
                        __angY__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i], __RAB__)
                        __angZ__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i], self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])
                        pspicture.append( eval("'" + value[1] + "'") )
                        self.interobjs[tmp_set][0] = False
                    else:
                        self.interobjs[tmp_set][0] = True
            # Cinemática y Dinámica
            pspicture.append( self.dynamic() )
            pspicture.append( self.cinema() )
        for self.k in objects2d:
            pspicture.append( eval("'" + self.objects[self.k] + "'") )
            # Objetos entre dos partículas.
            if self.k in interobjsset:
                for key, value in list(self.interobjs.items()):
                    if self.k in key:
                        if value[0]:
                            pspicture.append( eval("'" + value[1] + "'") )
                            self.interobjs[key][0] = False
                        else:
                            self.interobjs[key][0] = True
            # Cinemática y Dinámica
            pspicture.append( self.dynamic() )
            pspicture.append( self.cinema() )
        # Colocación de objetos. FIN
        frame += 1
        if tl:
            timeline.write("::" + str(frame) + "\n")
        pspicture.append( r"\end{pspicture}" )
        # Iteración de fotogramas
        if self.draw_track:
            # Tracks de las trayectorias.
            extra = ""
            for self.i in range(1, self.points):
                sys.stderr.write("\r" + "Procesando fotograma " + str(self.i+1) + " de " + str(self.points))
                pspicture.append( eval("'" + psset + "'") )
                pspicture.append( bpicture )
                if dynamic_viewpoint:
                    pspicture.append( head_picture )
                if shadows:
                    pspicture.append( latex_plan )
                if bit == "1":
                    if tail == 0:
                        ifrom = 0
                    else:
                        ifrom = max(self.i - tail, 0)*self.prec
                else:
                    ifrom = (self.i - 1)*self.prec
                for self.k in list(self.tracks.keys()):
                    if (shadows)&(self.dim[self.k] == 3):
                        if (self.tracks[self.k] == "")|(not "shadows" in list(self.cine[self.k].keys())):
                            continue
                        if "x" in self.cine[self.k]["shadows"]:
                            pspicture.append( r"\psProjection[object=line,linecolor="+self.tracks[self.k]+r"!50,linewidth=1pt,opacity=0.33,args=" )
                            for i in range(ifrom, self.i*self.prec + 1):
                                pspicture.append( n2t(self.__tracksp__[self.k][1][i])+" "+n2t(self.__tracksp__[self.k][2][i]) )
                            pspicture.append( ",plan=planX]" )
                        if "y" in self.cine[self.k]["shadows"]:
                            pspicture.append( r"\psProjection[object=line,linecolor="+self.tracks[self.k]+r"!50,linewidth=1pt,opacity=0.33,args=" )
                            for i in range(ifrom, self.i*self.prec + 1):
                                pspicture.append( n2t(self.__tracksp__[self.k][2][i])+" "+n2t(self.__tracksp__[self.k][0][i]) )
                            pspicture.append( ",plan=planY]" )
                        if "z" in self.cine[self.k]["shadows"]:
                            pspicture.append( r"\psProjection[object=line,linecolor="+self.tracks[self.k]+r"!50,linewidth=1pt,opacity=0.33,args=" )
                            for i in range(ifrom, self.i*self.prec + 1):
                                pspicture.append( n2t(self.__tracksp__[self.k][0][i])+" "+n2t(self.__tracksp__[self.k][1][i]) )
                            pspicture.append( ",plan=planZ]" )
                for self.k in list(self.tracks.keys()):
                    if self.tracks[self.k] == "":
                        continue
                    if self.dim[self.k] == 3:
                        pspicture.append( r"\psSolid[object=line,linecolor="+self.tracks[self.k]+r",args=" )
                        for i in range(ifrom, self.i*self.prec + 1):
                            pspicture.append( n2t(self.__tracksp__[self.k][0][i])+" "+n2t(self.__tracksp__[self.k][1][i])+" "+n2t(self.__tracksp__[self.k][2][i]) )
                        pspicture.append( "]" )
                    else:
                        tmp_str = r"\psline[linecolor="+self.tracks[self.k]+r",linewidth=1pt]{-}"
                        for i in range(ifrom, self.i*self.prec + 1):
                            tmp_str += "("+n2t(self.__tracksp__[self.k][0][i])+","+n2t(self.__tracksp__[self.k][1][i])+")"
                        pspicture.append(tmp_str)
                if tl:
                    pspicture.append( r"\end{pspicture}" )
                    frame += 1
                    extra = str(frame) + "x"+bit+","
                    timeline.write("::" + extra + str(frame+1) + "\n")
                # Material instantaneo.
                    pspicture.append( eval("'" + psset + "'") )
                    pspicture.append( bpicture )
                    if shadows:
                        pspicture.append( latex_plan )
                if shadows:
                    pspicture.append( eval("'" + self.shadows[-1] + "'") )
                    for self.k in range(self.particles):
                        pspicture.append( eval("'" + self.shadows[self.k] + "'") )
                    pspicture.append( r"\composeSolid" )
                pspicture.append( eval("'" + self.objects[-1] + "'") )
                # Colocación de objetos. INI
                distance = []
                for self.k in objects3d:
                    distance.append(self.__rp__[self.k][0][self.i]*self.__ev__(viewpoint[0]) + self.__rp__[self.k][1][self.i]*self.__ev__(viewpoint[1]) + self.__rp__[self.k][2][self.i]*self.__ev__(viewpoint[2]))
                tmp_dist = [x for (y,x) in sorted(zip(distance,objects3d))]
                for self.k in tmp_dist:
                    pspicture.append( eval("'" + self.objects[self.k] + "'") )
                    # Objetos entre dos partículas.
                    if self.k in interobjsset:
                        tmp_obj = sorted(list(self.interobjslist[self.k]), key=lambda x, l=tmp_dist: l.index(x))
                        for k_dest in tmp_obj:
                            tmp_set = frozenset([self.k,k_dest])
                            value = self.interobjs[tmp_set]
                            if value[0]:
                                tmp = list(tmp_set)
                                __RAB__  = sqrt((self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i])**2+(self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])**2)
                                __rAB__  = sqrt(__RAB__**2+(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i])**2)
                                __angY__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i], __RAB__)
                                __angZ__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i], self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])
                                pspicture.append( eval("'" + value[1] + "'") )
                                self.interobjs[tmp_set][0] = False
                            else:
                                self.interobjs[tmp_set][0] = True
                    # Cinemática y Dinámica
                    pspicture.append( self.dynamic() )
                    pspicture.append( self.cinema() )
                for self.k in objects2d:
                    pspicture.append( eval("'" + self.objects[self.k] + "'") )
                    # Objetos entre dos partículas.
                    if self.k in interobjsset:
                        for key, value in list(self.interobjs.items()):
                            if self.k in key:
                                if value[0]:
                                    pspicture.append( eval("'" + value[1] + "'") )
                                    self.interobjs[key][0] = False
                                else:
                                    self.interobjs[key][0] = True
                    # Cinemática y Dinámica
                    pspicture.append( self.dynamic() )
                    pspicture.append( self.cinema() )
                # Colocación de objetos. FIN
                pspicture.append( r"\end{pspicture}" )
                frame += 1
        else:
            for self.i in range(1, self.points):
                sys.stderr.write("\r" + "Procesando fotograma " + str(self.i+1) + " de " + str(self.points))
                # Material instantaneo.
                pspicture.append( eval("'" + psset + "'") )
                pspicture.append( bpicture )
                if dynamic_viewpoint:
                    pspicture.append( head_picture )
                pspicture.append( eval("'" + self.objects[-1] + "'") )
                if shadows:
                    pspicture.append( latex_plan )
                    pspicture.append( eval("'" + self.shadows[-1] + "'") )
                    for self.k in range(self.particles):
                        pspicture.append( eval("'" + self.shadows[self.k] + "'") )
                # Colocación de objetos. INI
                distance = []
                for self.k in objects3d:
                    distance.append(self.__rp__[self.k][0][self.i]*self.__ev__(viewpoint[0]) + self.__rp__[self.k][1][self.i]*self.__ev__(viewpoint[1]) + self.__rp__[self.k][2][self.i]*self.__ev__(viewpoint[2]))
                tmp_dist = [x for (y,x) in sorted(zip(distance,objects3d))]
                for self.k in tmp_dist:
                    pspicture.append( eval("'" + self.objects[self.k] + "'") )
                    # Objetos entre dos partículas.
                    if self.k in interobjsset:
                        tmp_obj = sorted(list(self.interobjslist[self.k]), key=lambda x, l=tmp_dist: l.index(x))
                        for k_dest in tmp_obj:
                            tmp_set = frozenset([self.k,k_dest])
                            value = self.interobjs[tmp_set]
                            if value[0]:
                                tmp = list(tmp_set)
                                __RAB__  = sqrt((self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i])**2+(self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])**2)
                                __rAB__  = sqrt(__RAB__**2+(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i])**2)
                                __angY__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][2][self.i]-self.__rp__[tmp[0]][2][self.i], __RAB__)
                                __angZ__ = 180./3.1415926*arctan(self.__rp__[tmp[1]][0][self.i]-self.__rp__[tmp[0]][0][self.i], self.__rp__[tmp[1]][1][self.i]-self.__rp__[tmp[0]][1][self.i])
                                pspicture.append( eval("'" + value[1] + "'") )
                                self.interobjs[tmp_set][0] = False
                            else:
                                self.interobjs[tmp_set][0] = True
                    # Cinemática y Dinámica
                    pspicture.append( self.dynamic() )
                    pspicture.append( self.cinema() )
                for self.k in objects2d:
                    pspicture.append( eval("'" + self.objects[self.k] + "'") )
                    # Objetos entre dos partículas.
                    if self.k in interobjsset:
                        for key, value in list(self.interobjs.items()):
                            if self.k in key:
                                if value[0]:
                                    pspicture.append( eval("'" + value[1] + "'") )
                                    self.interobjs[key][0] = False
                                else:
                                    self.interobjs[key][0] = True
                    # Cinemática y Dinámica
                    pspicture.append( self.dynamic() )
                    pspicture.append( self.cinema() )
                # Colocación de objetos. FIN
                pspicture.append( r"\end{pspicture}" )
                frame += 1
                if tl:
                    timeline.write("::" + str(frame) + "\n")
        # Liberamos memoria.
        del self.__tracks__
        del self.__a__
        del self.__v__
        del self.__r__
        del self.__lal__
        del self.__ao__
        del self.__F__
        del self.__Fs__
        del self.__lvl__
        del self.__ro__
        del self.__vo__
#        collected = gc.collect()
#        sys.stderr.write("Garbage collector: collected %d objects.\n" % (collected))
        # Escribimos el código de la animación.
        sys.stderr.write("\nAnimation: Compilando código Latex del entorno picture "+str(pspicture.number)+"...\n")
        pspicture.make()
        sys.stderr.write("Animation: Compilado.\n")
        if loop != []:
            cparam = ",loop"
        else:
            cparam = ""
        if tl:
            cparam += ",timeline=tmp_ltx/" + name + ".tln"
        print(r"\animategraphics[controls"+cparam+"]{"+str(self.fps)+"}{"+"tmp_ltx/"+pspicture.name+"}{000001}{"+"%06d"%(pspicture.number)+"}")
        if tl:
            timeline.close()
    def limit_reg(self, x0, y0, vx, vy):
        x1 = x0+vx
        y1 = y0+vy
        if (vx == 0)&(vy == 0):
            lim = 1
        elif vx == 0:
            if vy < 0:
                limy = self.pmin[1] - y0
            else:
                limy = self.pmax[1] - y0
            lim = limy/vy
        elif vy == 0:
            if vx < 0:
                limx = self.pmin[0] - y0
            else:
                limx = self.pmax[0] - x0
            lim = limx/vx
        else:
            if vx < 0:
                limx = self.pmin[0] - x0
            else:
                limx = self.pmax[0] - x0
            if vy < 0:
                limy = self.pmin[1] - y0
            else:
                limy = self.pmax[1] - y0
            lim = min(limx/vx,limy/vy)
        if lim < 1:
            posx = x0 + vx*lim
            posy = y0 + vy*lim
        else:
            posx = x1
            posy = y1
        return posx, posy
    def cinema(self, k = -1, i = -1):
        if k == -1:
            k = self.k
        if i == -1:
            i = self.i
        result = ""
        _abc_ = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
        if self.draw_a[k]:
            if self.dim[self.k] == 3:
                x0 = self.__rp__[k][0][i]
                y0 = self.__rp__[k][1][i]
                z0 = self.__rp__[k][2][i]
                vx = self.__a__[k][0][i]
                vy = self.__a__[k][1][i]
                vz = self.__a__[k][2][i]
                # Conversión de realidad a imagen.
                vx = self.a_vars2pic[0](vx)
                vy = self.a_vars2pic[1](vy)
                vz = self.a_vars2pic[2](vz)
                result += r"\psSolid[object=vecteur,args={"+n2t(vx)+" "+n2t(vy)+" "+n2t(vz)+" [0.17 0.8]},linecolor=green(pigment)]("+n2t(x0)+","+n2t(y0)+","+n2t(z0)+")"
                #result += r"\psLineIIID[linecolor=green,linewidth=2pt,arrows=->]("+self.n(x0)+","+self.n(y0)+","+self.n(z0)+")("+self.n(x0+vx)+","+self.n(y0+vy)+","+self.n(z0+vz)+")"
                result += r"\psPoint("+n2t(x0+vx)+","+n2t(y0+vy)+","+n2t(z0+vz)+r"){ACEL}\rput[b](ACEL){$\overrightarrow{a}_{"+_abc_[k]+"}\ "+self.n(self.__lal__[k][i], self.digits)+r"\;"+self.aunit+"$}"
            else:
                x0 = self.__rp__[k][0][i]
                y0 = self.__rp__[k][1][i]
                vx = self.__a__[k][0][i]
                vy = self.__a__[k][1][i]
                # Conversión de realidad a imagen.
                vx = self.a_vars2pic[0](vx)
                vy = self.a_vars2pic[1](vy)
                vx, vy = self.moderate(vx, vy)
                posx, posy = self.limit_reg(x0, y0, vx, vy)
                result += r"\psline[linecolor=green(pigment),linewidth=2pt,arrowinset=2]{->}("+n2t(x0)+","+n2t(y0)+r")("+n2t(x0+vx)+","+n2t(y0+vy)+")"
                result += r"\rput[b]{"+n2t(180/pi*arctan(vx,vy,True))+"}("+n2t(posx)+","+n2t(posy)+r"){$\overrightarrow{a}_{"+_abc_[k]+"}\ "+self.n(self.__lal__[k][i], self.digits)+r"\;"+self.aunit+"$}"
        if self.draw_v[k]:
            # Vector velocidad
            if self.dim[self.k] == 3:
                x0 = self.__rp__[k][0][i]
                y0 = self.__rp__[k][1][i]
                z0 = self.__rp__[k][2][i]
                vx = self.__v__[k][0][i]
                vy = self.__v__[k][1][i]
                vz = self.__v__[k][2][i]
                # Conversión de realidad a imagen.
                vx = self.v_vars2pic[0](vx)
                vy = self.v_vars2pic[1](vy)
                vz = self.v_vars2pic[2](vz)
                result += r"\psSolid[object=vecteur,args={"+n2t(vx)+" "+n2t(vy)+" "+n2t(vz)+" [0.1 0.5]},linecolor=blue(pigment)]("+n2t(x0)+","+n2t(y0)+","+n2t(z0)+")"
                #result += r"\psLineIIID[linecolor=blue,linewidth=1.2pt,arrows=->]("+self.n(x0)+","+self.n(y0)+","+self.n(z0)+")("+self.n(x0+vx)+","+self.n(y0+vy)+","+self.n(z0+vz)+")"
                result += r"\psPoint("+n2t(x0+vx)+","+n2t(y0+vy)+","+n2t(z0+vz)+r"){VEL}\rput[t](VEL){$\overrightarrow{v}_{"+_abc_[k]+"}\ "+self.n(self.__lvl__[k][i], self.digits)+r"\;"+self.vunit+"$}"
            else:
                x0 = self.__rp__[k][0][i]
                y0 = self.__rp__[k][1][i]
                vx = self.__v__[k][0][i]
                vy = self.__v__[k][1][i]
                # Conversión de realidad a imagen.
                vx = self.v_vars2pic[0](vx)
                vy = self.v_vars2pic[1](vy)
                vx, vy = self.moderate(vx, vy)
                posx, posy = self.limit_reg(x0, y0, vx, vy)
                result += r"\psline[linecolor=blue(pigment),linewidth=1.2pt,arrowinset=2]{->}("+n2t(x0)+","+n2t(y0)+r")("+n2t(x0+vx)+","+n2t(y0+vy)+")"
                result += r"\rput[t]{"+n2t(180/pi*arctan(vx,vy,True))+"}("+n2t(posx)+","+n2t(posy)+r"){$\overrightarrow{v}_{"+_abc_[k]+"}\ "+self.n(self.__lvl__[k][i], self.digits)+r"\;"+self.vunit+"$}"
        return result
    def dynamic(self, k = -1, i = -1):
        if k == -1:
            k = self.k
        if i == -1:
            i = self.i
        result = ""
        _abc_ = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"]
        if self.dim[self.k] == 3:
            for l in range(self.Fnum[k]):
                # Vector fuerza
                x0 = self.__rp__[k][0][i]
                y0 = self.__rp__[k][1][i]
                z0 = self.__rp__[k][2][i]
                vx = self.__Fs__[k][l][0][i]
                vy = self.__Fs__[k][l][1][i]
                vz = self.__Fs__[k][l][2][i]
                # Conversión de realidad a imagen.
                result += r"\psSolid[object=vecteur,args={"+n2t(vx)+" "+n2t(vy)+" "+n2t(vz)+" [0.2 1.]},linecolor=burlywood]("+n2t(x0)+","+n2t(y0)+","+n2t(z0)+")"
                #result += r"\psLineIIID[linecolor=ferrarired,linewidth=2.8pt,arrows=->]("+self.n(x0)+","+self.n(y0)+","+self.n(z0)+")("+self.n(x0+vx)+","+self.n(y0+vy)+","+self.n(z0+vz)+")"
                result += r"\psPoint("+n2t(x0+vx)+","+n2t(y0+vy)+","+n2t(z0+vz)+r"){FORCE"+str(l)+r"}\rput[t](FORCE"+str(l)+"){$\overrightarrow{"+self.Fname[k][l]+"}_{"+_abc_[k]+"}\ "+self.n(self.__lFl__[k][l][i], self.digits)+self.Funit[k][l]+"$}"
        else:
            for l in range(self.Fnum[k]):
                # Vector fuerza
                x0 = self.__rp__[k][0][i]
                y0 = self.__rp__[k][1][i]
                vx = self.__Fs__[k][l][0][i]
                vy = self.__Fs__[k][l][1][i]
                # Conversión de realidad a imagen.
                vx, vy = self.moderate(vx, vy)
                posx, posy = self.limit_reg(x0, y0, vx, vy)
                if self.Falig[k][l] < 0:
                    alig = "t"
                else:
                    alig = "b"
                result += r"\psline[linecolor=burlywood,linewidth=2.8pt,arrowinset=2]{->}("+n2t(x0)+","+n2t(y0)+r")("+n2t(x0+vx)+","+n2t(y0+vy)+")\n"
                result += r"\rput["+alig+"]{"+n2t(180/pi*arctan(vx,vy,True))+"}("+n2t(posx)+","+n2t(posy)+r"){\raisebox{"+str(self.Falig[k][l])+"em}{$\overrightarrow{"+self.Fname[k][l]+"}_{"+_abc_[k]+r"}\ "+self.n(self.__lFl__[k][l][i], self.digits)+self.Funit[k][l]+"$}}"
        return result
    def _repl_str_(self, match):
        result = match.group(1)
        if result == "t":
            result = "(self.start + self.i*self.lap)"
            self.time_dependent = True
        elif result == "unit":
            result = "self.unit"
        elif result == "margin":
            result = "self.margin"
        elif result == "size":
            result = "self.size"
        else:
            r = [ "x", "y", "z" ]
            v = [ "v_x", "v_y", "v_z" ]
            a = [ "a_x", "a_y", "a_z" ]
            for k in range(self.particles):
                for j in range(self.dim[k]):
                    # Variables naturales.
                    if result == str(self.a_vars[k][self.vars[k][j]]):
                        result = "self.__ao__["+str(k)+"]["+str(j)+"][self.i]"
                        self.time_dependent = True
                        return result + match.group(2)
                    if result == str(self.v_vars[k][self.vars[k][j]]):
                        result = "self.__vo__["+str(k)+"]["+str(j)+"][self.i]"
                        self.time_dependent = True
                        return result + match.group(2)
                    if result == str(self.vars[k][j]):
                        result = "self.__ro__["+str(k)+"]["+str(j)+"][self.i]"
                        self.time_dependent = True
                        return result + match.group(2)
                    # Variables cartesianas.
                    if result == a[j]+str(k):
                        result = "self.__a__["+str(self.k)+"]["+str(j)+"][self.i]"
                        self.time_dependent = True
                        return result + match.group(2)
                    if result == v[j]+str(k):
                        result = "self.__v__["+str(self.k)+"]["+str(j)+"][self.i]"
                        self.time_dependent = True
                        return result + match.group(2)
                    if result == r[j]+str(k):
                        result = "self.__r__["+str(self.k)+"]["+str(j)+"][self.i]"
                        self.time_dependent = True
                        return result + match.group(2)
                    if result == "_"+a[j]+str(k):
                        result = "self.a_vars2pic["+str(j)+"](self.__a__["+str(self.k)+"]["+str(j)+"][self.i])"
                        self.time_dependent = True
                        return result + match.group(2)
                    if result == "_"+v[j]+str(k):
                        result = "self.v_vars2pic["+str(j)+"](self.__v__["+str(self.k)+"]["+str(j)+"][self.i])"
                        self.time_dependent = True
                        return result + match.group(2)
                    if result == "_"+r[j]+str(k):
                        result = "self.__rp__["+str(self.k)+"]["+str(j)+"][self.i]"
                        self.time_dependent = True
                        return result + match.group(2)
        return result + match.group(2)
    def insert(self, k, *subjects):
        self.k = k
        # Salvo las fuerzas todo lo demás debe insertarse después de .evol
        if self.evoled:
            _beg_ = "«"; _end_ = "»"; _nbeg_ = len(_beg_); _nend_ = len(_end_)
            if isinstance(subjects[0], int):
                first = 1
            else:
                first = 0
            for subject in subjects[first:]:
                self.time_dependent = False
                # Comenzamos procesando los delimitadores.
                # Proceso de parentesis.
                subject = subject.lstrip(" ").replace("\\", "\\\\")
                begin, end = delim(subject, len(subject)-1, step = -1)
                while end != None:
                    if subject[begin] =="(":
                        tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, subject[begin:end+1])
                        tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                        params = arguments(tmp1, 0, paren = "()")
                        nparams = len(params)
                        #if nparams != 1:
                        params = mapi([lambda x, var=j: "self.vars2pic["+str(var)+"]("+x+")" for j in range(nparams) ], params)
                        #fi
                        subject = subject[:begin] + "('+n2t(" + ")+','+n2t(".join(params) + ")+')" + subject[end+1:]
                    begin, end = delim(subject, begin-1, step = -1)
                # Proceso de código python. A insertar solo en corchetes y llaves.
                begin, end = subject.find(_beg_), subject.find(_end_)
                while (begin != -1)&(end != -1):
                    tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, subject[begin+_nbeg_:end])
                    tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                    subject = subject[:begin] + "'+latex(cevalf(" + tmp1 + ",self.digits))+'" + subject[end+_nend_:]
                    begin, end = subject.find(_beg_), subject.find(_end_)
                # Obtención de información.
                # Nombre del comando.
                cmd = ""
                pos = 0
                nsubject = len(subject)
                while not subject[pos] in "({[\\":
                    cmd += subject[pos]
                    pos += 1
                    if pos == nsubject:
                        break
                # Contenido de delimitadores.
                pparam = ""
                cparam = ""
                kparam = ""
                begin, end = delim(subject, pos)
                while begin != None:
                    if subject[begin] =="(":
                        pparam = subject[begin+1:end]
                    elif subject[begin] =="[":
                        cparam = "," + subject[begin+1:end]
                    elif subject[begin] =="{":
                        kparam = subject[begin+1:end]
                    begin, end = delim(subject, end+1)
                ##### Casos por comandos #####
                # Comandos de dos partículas.
                if first == 1:
                    if cmd == "line":
                        if kparam == "":
                            kparam = "-"
                        scparam = regexp.sub("![0-9]+", "", cparam)
                        scparam = regexp.sub("(linecolor=[^\,]+)", "\\1!50", scparam)
                        if (self.time_dependent)|(self.mov[subjects[0]])|(self.mov[k]):
                            self.interobjslist[k] |= set([subjects[0]])
                            self.interobjslist[subjects[0]] |= set([k])
                            if self.dim[k] == 3:
#                                if "shadows" in self.cine[k].keys():
#                                    if "x" in self.cine[k]["shadows"]:
#                                        self.shadows[k] += r"\psProjection[object=line,linewidth="+kparam+r"pt,linecolor=black!50,opacity=0.33"+scparam+",args='+str(self.__rp__["+str(k)+r"][1][self.i])+' '+str(self.__rp__["+str(k)+r"][2][self.i])+' '+str(self.__rp__["+str(subjects[0])+r"][1][self.i])+','+str(self.__rp__["+str(subjects[0])+r"][2][self.i])+',plan=planX]"
#                                    if "y" in self.cine[k]["shadows"]:
#                                        self.shadows[k] += r"\psProjection[object=line,linewidth="+kparam+r"pt,linecolor=black!50,opacity=0.33"+scparam+",args='+str(self.__rp__["+str(k)+r"][2][self.i])+' '+str(self.__rp__["+str(k)+r"][0][self.i])+' '+str(self.__rp__["+str(subjects[0])+r"][2][self.i])+','+str(self.__rp__["+str(subjects[0])+r"][0][self.i])+',plan=planY]"
#                                    if "z" in self.cine[k]["shadows"]:
#                                        self.shadows[k] += r"\psProjection[object=line,linewidth="+kparam+r"pt,linecolor=black!50,opacity=0.33"+scparam+",args='+str(self.__rp__["+str(k)+r"][0][self.i])+' '+str(self.__rp__["+str(k)+r"][1][self.i])+' '+str(self.__rp__["+str(subjects[0])+r"][0][self.i])+','+str(self.__rp__["+str(subjects[0])+r"][1][self.i])+',plan=planZ]"
                                tmp_set = frozenset([k,subjects[0]])
                                if tmp_set in list(self.interobjs.keys()):
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=line"+cparam+r",args='+n2t(self.__rp__["+str(k)+r"][0][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][0][self.i]-self.__rp__["+str(subjects[0])+r"][0][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(k)+r"][1][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][1][self.i]-self.__rp__["+str(subjects[0])+r"][1][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(k)+r"][2][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][2][self.i]-self.__rp__["+str(subjects[0])+r"][2][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][0][self.i]-self.__rp__["+str(subjects[0])+r"][0][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][1][self.i]-self.__rp__["+str(subjects[0])+r"][1][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][2][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][2][self.i]-self.__rp__["+str(subjects[0])+r"][2][self.i])/__rAB__)+']"
                                else:
                                    self.interobjs.update({tmp_set: [True, r"\\psSolid[object=line"+cparam+r",args='+n2t(self.__rp__["+str(k)+r"][0][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][0][self.i]-self.__rp__["+str(subjects[0])+r"][0][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(k)+r"][1][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][1][self.i]-self.__rp__["+str(subjects[0])+r"][1][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(k)+r"][2][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][2][self.i]-self.__rp__["+str(subjects[0])+r"][2][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][0][self.i]-self.__rp__["+str(subjects[0])+r"][0][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][1][self.i]-self.__rp__["+str(subjects[0])+r"][1][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][2][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][2][self.i]-self.__rp__["+str(subjects[0])+r"][2][self.i])/__rAB__)+']" ] })
                            else:
                                tmp_set = frozenset([k,subjects[0]])
                                if tmp_set in list(self.interobjs.keys()):
                                    self.interobjs[tmp_set][1] += r"\\psline[linewidth=1pt"+cparam+r"]{"+kparam+r"}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+')('+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i])+','+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i])+')"
                                else:
                                    self.interobjs.update({tmp_set: [True, r"\\psline[linewidth=1pt"+cparam+r"]{"+kparam+r"}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+')('+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i])+','+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i])+')" ] })
                        else:
                            self.sinterobjslist[k] |= set([subjects[0]])
                            self.sinterobjslist[subjects[0]] |= set([k])
                            if self.dim[k] == 3:
#                                if "shadows" in self.cine[k].keys():
#                                    if "x" in self.cine[k]["shadows"]:
#                                        self.shadows[k] += r"\psProjection[object=line,linewidth="+kparam+r"pt,linecolor=black!50,opacity=0.33"+scparam+",args='+str(self.__rp__["+str(k)+r"][1][self.i])+' '+str(self.__rp__["+str(k)+r"][2][self.i])+' '+str(self.__rp__["+str(subjects[0])+r"][1][self.i])+','+str(self.__rp__["+str(subjects[0])+r"][2][self.i])+',plan=planX]"
#                                    if "y" in self.cine[k]["shadows"]:
#                                        self.shadows[k] += r"\psProjection[object=line,linewidth="+kparam+r"pt,linecolor=black!50,opacity=0.33"+scparam+",args='+str(self.__rp__["+str(k)+r"][2][self.i])+' '+str(self.__rp__["+str(k)+r"][0][self.i])+' '+str(self.__rp__["+str(subjects[0])+r"][2][self.i])+','+str(self.__rp__["+str(subjects[0])+r"][0][self.i])+',plan=planY]"
#                                    if "z" in self.cine[k]["shadows"]:
#                                        self.shadows[k] += r"\psProjection[object=line,linewidth="+kparam+r"pt,linecolor=black!50,opacity=0.33"+scparam+",args='+str(self.__rp__["+str(k)+r"][0][self.i])+' '+str(self.__rp__["+str(k)+r"][1][self.i])+' '+str(self.__rp__["+str(subjects[0])+r"][0][self.i])+','+str(self.__rp__["+str(subjects[0])+r"][1][self.i])+',plan=planZ]"
                                tmp_set = frozenset([k,subjects[0]])
                                if tmp_set in list(self.interobjs.keys()):
                                    self.sinterobjs[tmp_set][1] += r"\\psSolid[object=line"+cparam+r",args='+n2t(self.__rp__["+str(k)+r"][0][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][0][self.i]-self.__rp__["+str(subjects[0])+r"][0][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(k)+r"][1][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][1][self.i]-self.__rp__["+str(subjects[0])+r"][1][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(k)+r"][2][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][2][self.i]-self.__rp__["+str(subjects[0])+r"][2][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][0][self.i]-self.__rp__["+str(subjects[0])+r"][0][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][1][self.i]-self.__rp__["+str(subjects[0])+r"][1][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][2][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][2][self.i]-self.__rp__["+str(subjects[0])+r"][2][self.i])/__rAB__)+']"
                                else:
                                    self.sinterobjs.update({tmp_set: [True, r"\\psSolid[object=line"+cparam+r",args='+n2t(self.__rp__["+str(k)+r"][0][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][0][self.i]-self.__rp__["+str(subjects[0])+r"][0][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(k)+r"][1][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][1][self.i]-self.__rp__["+str(subjects[0])+r"][1][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(k)+r"][2][self.i]-"+self.radius[k]+"*(self.__rp__["+str(k)+r"][2][self.i]-self.__rp__["+str(subjects[0])+r"][2][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][0][self.i]-self.__rp__["+str(subjects[0])+r"][0][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][1][self.i]-self.__rp__["+str(subjects[0])+r"][1][self.i])/__rAB__)+' '+n2t(self.__rp__["+str(subjects[0])+r"][2][self.i]+"+self.radius[subjects[0]]+"*(self.__rp__["+str(k)+r"][2][self.i]-self.__rp__["+str(subjects[0])+r"][2][self.i])/__rAB__)+']" ] })
                            else:
                                tmp_set = frozenset([k,subjects[0]])
                                if tmp_set in list(self.interobjs.keys()):
                                    self.sinterobjs[tmp_set][1] += r"\\psline[linewidth=1pt"+cparam+r"]{"+kparam+r"}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+')('+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i])+','+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i])+')"
                                else:
                                    self.sinterobjs.update({tmp_set: [True, r"\\psline[linewidth=1pt"+cparam+r"]{"+kparam+r"}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+')('+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i])+','+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i])+')" ] })
                    elif cmd == "coil":
                        self.coils += 1
                        if (self.time_dependent)|(self.mov[subjects[0]])|(self.mov[k]):
                            self.interobjslist[k] |= set([subjects[0]])
                            self.interobjslist[subjects[0]] |= set([k])
                            if self.dim[k] == 3:
                                default = [ "5", str(max(eval(self.radius[k]),eval(self.radius[subjects[0]]))) ]
                                tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                                tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                                kparam = arguments("{" + tmp1 + "}", 0, "{}")
                                for i, param in enumerate(kparam):
                                    if param != "":
                                        default[i] = param
                                if k > subjects[0]:
                                    tmp_angY = "180-__angY__"
                                    tmp_angZ = "Mod(180+__angZ__,360)"
                                else:
                                    tmp_angY = "__angY__"
                                    tmp_angZ = "__angZ__"
                                tmp_set = frozenset([k,subjects[0]])
                                if tmp_set in list(self.interobjs.keys()):
                                    self.interobjs[tmp_set][1] += r"\\defFunction[algebraic]{helice"+str(self.coils)+r"}(t){"+default[1]+r"*cos(2*3.1415*t*"+default[0]+r")}{"+default[1]+r"*sin(2*3.1415*t*"+default[0]+r")}{'+n2t(__rAB__)+'*t}"
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=courbe,range=0 1,linewidth=0.2pt,fillcolor=ashgrey,r=0.1,resolution=360,RotY='+n2t("+tmp_angY+")+',RotZ='+n2t("+tmp_angZ+")+'"+cparam+",function=helice"+str(self.coils)+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                                    self.interobjs[tmp_set][1] += r"\\composeSolid"
                                else:
                                    self.interobjs.update({tmp_set: [True, r"\\defFunction[algebraic]{helice"+str(self.coils)+r"}(t){"+default[1]+r"*cos(2*3.1415*t*"+default[0]+r")}{"+default[1]+r"*sin(2*3.1415*t*"+default[0]+r")}{'+n2t(__rAB__)+'*t}" ] })
                                    self.interobjs[tmp_set][1] +=  r"\\psSolid[object=courbe,range=0 1,linewidth=0.2pt,fillcolor=ashgrey,r=0.1,resolution=360,RotY='+n2t("+tmp_angY+")+',RotZ='+n2t("+tmp_angZ+")+'"+cparam+",function=helice"+str(self.coils)+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                                    self.interobjs[tmp_set][1] += r"\\composeSolid"
                            else:
                                if kparam != "":
                                    tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                                    kparam = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                                tmp_set = frozenset([k,subjects[0]])
                                if tmp_set in list(self.interobjs.keys()):
                                    self.interobjs[tmp_set][1] += r"\\pscoil[linecolor=ashgrey"+cparam+"]{-}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+')('+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i])+','+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i])+')"
                                    if kparam != "":
                                        self.interobjs[tmp_set][1] += r"{\\rput('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){$\\begin{array}{rl}l =& '+self.n(sqrt((self.__r__["+str(k)+r"][0][self.i]-self.__r__["+str(subjects[0])+r"][0][self.i])**2 + (self.__r__["+str(k)+r"][1][self.i]-self.__r__["+str(subjects[0])+r"][1][self.i])**2),2)+'\\;m \\\\ \\Delta l =& '+self.n(sqrt((self.__r__["+str(k)+r"][0][self.i]-self.__r__["+str(subjects[0])+r"][0][self.i])**2 + (self.__r__["+str(k)+r"][1][self.i]-self.__r__["+str(subjects[0])+r"][1][self.i])**2)-"+kparam+r",2)+'\\;m\\end{array}$}}"
                                else:
                                    self.interobjs.update({tmp_set: [True, r"\\pscoil[linecolor=ashgrey"+cparam+"]{-}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+')('+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i])+','+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i])+')" ] })
                                    if kparam != "":
                                        self.interobjs[tmp_set][1] += r"{\\rput('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){$\\begin{array}{rl}l =& '+self.n(sqrt((self.__r__["+str(k)+r"][0][self.i]-self.__r__["+str(subjects[0])+r"][0][self.i])**2 + (self.__r__["+str(k)+r"][1][self.i]-self.__r__["+str(subjects[0])+r"][1][self.i])**2),2)+'\\;m \\\\ \\Delta l =& '+self.n(sqrt((self.__r__["+str(k)+r"][0][self.i]-self.__r__["+str(subjects[0])+r"][0][self.i])**2 + (self.__r__["+str(k)+r"][1][self.i]-self.__r__["+str(subjects[0])+r"][1][self.i])**2)-"+kparam+r",2)+'\\;m\\end{array}$}}"
                        else:
                            self.sinterobjslist[k] |= set([subjects[0]])
                            self.sinterobjslist[subjects[0]] |= set([k])
                            if self.dim[k] == 3:
                                default = [ "5", str(max(eval(self.radius[k]),eval(self.radius[subjects[0]]))) ]
                                tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                                tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                                kparam = arguments("{" + tmp1 + "}", 0, "{}")
                                for i, param in enumerate(kparam):
                                    if param != "":
                                        default[i] = param
                                if k > subjects[0]:
                                    tmp_angY = "180-__angY__"
                                    tmp_angZ = "Mod(180+__angZ__,360)"
                                else:
                                    tmp_angY = "__angY__"
                                    tmp_angZ = "__angZ__"
                                tmp_set = frozenset([k,subjects[0]])
                                if tmp_set in list(self.interobjs.keys()):
                                    self.sinterobjs[tmp_set][1] += r"\\defFunction[algebraic]{helice"+str(self.coils)+r"}(t){"+default[1]+r"*cos(2*3.1415*t*"+default[0]+r")}{"+default[1]+r"*sin(2*3.1415*t*"+default[0]+r")}{'+n2t(__rAB__)+'*t}"
                                    self.sinterobjs[tmp_set][1] += r"\\psSolid[object=courbe,range=0 1,linewidth=0.2pt,fillcolor=ashgrey,r=0,resolution=360,RotY='+n2t("+tmp_angY+")+',RotZ='+n2t("+tmp_angZ+")+'"+cparam+",function=helice"+str(self.coils)+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                                    self.sinterobjs[tmp_set][1] += r"\\composeSolid"
                                else:
                                    self.sinterobjs.update({tmp_set: [True, r"\\defFunction[algebraic]{helice"+str(self.coils)+r"}(t){"+default[1]+r"*cos(2*3.1415*t*"+default[0]+r")}{"+default[1]+r"*sin(2*3.1415*t*"+default[0]+r")}{'+n2t(__rAB__)+'*t}" ] })
                                    self.sinterobjs[tmp_set][1] +=  r"\\psSolid[object=courbe,range=0 1,linewidth=0.2pt,fillcolor=ashgrey,r=0,resolution=360,RotY='+n2t("+tmp_angY+")+',RotZ='+n2t("+tmp_angZ+")+'"+cparam+",function=helice"+str(self.coils)+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                                    self.sinterobjs[tmp_set][1] += r"\\composeSolid"
                            else:
                                if kparam != "":
                                    tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                                    kparam = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                                self.static[k] += r"\\pscoil[linecolor=ashgrey"+cparam+"]{-}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+')('+n2t(self.__rp__["+str(subjects[0])+r"][0][self.i])+','+n2t(self.__rp__["+str(subjects[0])+r"][1][self.i])+')"
                                if kparam != "":
                                    self.static[k] += r"{\\rput('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){$\\begin{array}{rl}l =& '+n2t(sqrt((self.__r__["+str(k)+r"][0][self.i]-self.__r__["+str(subjects[0])+r"][0][self.i])**2 + (self.__r__["+str(k)+r"][1][self.i]-self.__r__["+str(subjects[0])+r"][1][self.i])**2),2)+'\\;m \\\\ \\Delta l =& '+n2t(sqrt((self.__r__["+str(k)+r"][0][self.i]-self.__r__["+str(subjects[0])+r"][0][self.i])**2 + (self.__r__["+str(k)+r"][1][self.i]-self.__r__["+str(subjects[0])+r"][1][self.i])**2)-"+kparam+r",2)+'\\;m\\end{array}$}}"
                    elif cmd == "pendulum":
                        self.pendulums += 1
                        default = [ "0.1", "0.4" ]
                        tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                        tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                        kparam = arguments("{" + tmp1 + "}", 0, "{}")
                        for i, param in enumerate(kparam):
                            if param != "":
                                default[i] = param
                        self.radius[subjects[0]] = default[1]
                        if (self.time_dependent)|(self.mov[subjects[0]])|(self.mov[k]):
                            self.interobjslist[k] |= set([subjects[0]])
                            self.interobjslist[subjects[0]] |= set([k])
                            if self.dim[k] == 3:
                                if k > subjects[0]:
                                    tmp_angY = "180-__angY__"
                                    tmp_angZ = "Mod(180+__angZ__,360)"
                                else:
                                    tmp_angY = "__angY__"
                                    tmp_angZ = "__angZ__"
                                tmp_set = frozenset([k,subjects[0]])
                                if tmp_set in list(self.interobjs.keys()):
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=cylindre,h='+n2t(__rAB__-"+default[1]+"-"+self.radius[k]+")+',r='+n2t("+default[0]+")+',fillcolor=cadetblue,action=none"+cparam+",name=cylin"+str(self.pendulums)+"](0,0,"+self.radius[k]+")"
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=sphere,r='+n2t("+default[1]+")+',fillcolor=cadetblue,action=none"+cparam+",name=sphere"+str(self.pendulums)+"](0,0,'+n2t(__rAB__)+')"
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=fusion,linewidth=0.2pt,base=cylin"+str(self.pendulums)+" sphere"+str(self.pendulums)+",RotY='+n2t("+tmp_angY+")+',RotZ='+n2t("+tmp_angZ+")+']('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                                    self.interobjs[tmp_set][1] += r"\\composeSolid"
                                else:
                                    self.interobjs.update({tmp_set: [True, r"\\psSolid[object=cylindre,h='+n2t(__rAB__-"+default[1]+"-"+self.radius[k]+")+',r='+n2t("+default[0]+")+',fillcolor=cadetblue,action=none"+cparam+",name=cylin"+str(self.pendulums)+"](0,0,"+self.radius[k]+")" ] })
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=sphere,r='+n2t("+default[1]+")+',fillcolor=cadetblue,action=none"+cparam+",name=sphere"+str(self.pendulums)+"](0,0,'+n2t(__rAB__)+')"
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=fusion,linewidth=0.2pt,base=cylin"+str(self.pendulums)+" sphere"+str(self.pendulums)+",RotY='+n2t("+tmp_angY+")+',RotZ='+n2t("+tmp_angZ+")+']('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                                    self.interobjs[tmp_set][1] += r"\\composeSolid"
                        else:
                            self.sinterobjslist[k] |= set([subjects[0]])
                            self.sinterobjslist[subjects[0]] |= set([k])
                            if self.dim[k] == 3:
                                if k > subjects[0]:
                                    tmp_angY = "180-__angY__"
                                    tmp_angZ = "Mod(180+__angZ__,360)"
                                else:
                                    tmp_angY = "__angY__"
                                    tmp_angZ = "__angZ__"
                                tmp_set = frozenset([k,subjects[0]])
                                if tmp_set in list(self.interobjs.keys()):
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=cylindre,linewidth=0.2pt,h='+n2t(__rAB__-"+default[1]+")+',r='+n2t("+default[0]+")+',fillcolor=cadetblue,action=none"+cparam+",name=cylin"+str(self.pendulums)+"](0,0,0)"
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=sphere,linewidth=0.2pt,r='+n2t("+default[1]+")+',fillcolor=cadetblue,action=none"+cparam+",name=sphere"+str(self.pendulums)+"](0,0,'+n2t(__rAB__)+')"
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=fusion,base=cylin"+str(self.pendulums)+" sphere"+str(self.pendulums)+",RotY='+n2t("+tmp_angY+")+',RotZ='+n2t("+tmp_angZ+")+']('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                                    self.interobjs[tmp_set][1] += r"\\composeSolid"
                                else:
                                    self.interobjs.update({tmp_set: [True, r"\\psSolid[object=cylindre,linewidth=0.2pt,h='+n2t(__rAB__-"+default[1]+")+',r='+n2t("+default[0]+")+',fillcolor=cadetblue,action=none"+cparam+",name=cylin"+str(self.pendulums)+"](0,0,0)" ] })
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=sphere,linewidth=0.2pt,r='+n2t("+default[1]+")+',fillcolor=cadetblue,action=none"+cparam+",name=sphere"+str(self.pendulums)+"](0,0,'+n2t(__rAB__)+')"
                                    self.interobjs[tmp_set][1] += r"\\psSolid[object=fusion,base=cylin"+str(self.pendulums)+" sphere"+str(self.pendulums)+",RotY='+n2t("+tmp_angY+")+',RotZ='+n2t("+tmp_angZ+")+']('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                                    self.interobjs[tmp_set][1] += r"\\composeSolid"
                # Comandos de una partícula,
                elif cmd == "floor*":
                    if kparam == "":
                        kparam = "-1.5"
                    if self.time_dependent:
                        self.objects[k] += r"\\psframe*[linecolor=earthyellow,fillcolor=earthyellow"+cparam+"]('+n2t(self.pmmin[0])+','+n2t(self.pmmin[1])+')('+n2t(self.pmmax[0])+',"+kparam+")"
                    else:
                        self.static[k] += r"\\psframe*[linecolor=earthyellow,fillcolor=earthyellow"+cparam+"]('+n2t(self.pmmin[0])+','+n2t(self.pmmin[1])+')('+n2t(self.pmmax[0])+',"+kparam+")"
                elif cmd == "floor":
                    if kparam == "":
                        kparam = "-1.5"
                    if self.time_dependent:
                        self.objects[k] += r"\\psframe[linecolor=earthyellow,fillcolor=earthyellow"+cparam+"]('+n2t(self.pmmin[0])+','+n2t(self.pmmin[1])+')('+n2t(self.pmmax[0])+',"+kparam+")"
                    else:
                        self.static[k] += r"\\psframe[linecolor=earthyellow,fillcolor=earthyellow"+cparam+"]('+n2t(self.pmmin[0])+','+n2t(self.pmmin[1])+')('+n2t(self.pmmax[0])+',"+kparam+")"
                elif cmd == "point":
                    if kparam == "":
                        kparam = "0.2"
                    if (self.time_dependent)|(self.mov[k]):
                        if self.dim[k] == 3:
                            self.shadows[k] += r"\\psProjection[object=point,args='+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t("+kparam+")+',linecolor=black!50,opacity=0.33,plan=planX]"
                            self.shadows[k] += r"\\psProjection[object=point,args='+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t("+kparam+")+',linecolor=black!50,opacity=0.33,plan=planY]"
                            self.shadows[k] += r"\\psProjection[object=point,args='+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t("+kparam+")+',linecolor=black!50,opacity=0.33,plan=planZ]"
                            self.objects[k] += r"\\psSolid[object=point"+cparam+",args='+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t(self.__rp__["+str(k)+r"][2][self.i])+']"
                        else:
                            self.objects[k] += r"\\pscircle*[linecolor=black,fillcolor=black"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){'+n2t("+kparam+")+'}"
                    else:
                        if self.dim[k] == 3:
                            self.sshadows[k] += r"\\psProjection[object=point,args='+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t("+kparam+")+',linecolor=black!50,opacity=0.33,plan=planX]"
                            self.sshadows[k] += r"\\psProjection[object=point,args='+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t("+kparam+")+',linecolor=black!50,opacity=0.33,plan=planY]"
                            self.sshadows[k] += r"\\psProjection[object=point,args='+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t("+kparam+")+',linecolor=black!50,opacity=0.33,plan=planZ]"
                            self.static[k] += r"\\psSolid[object=point"+cparam+",args='+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t(self.__rp__["+str(k)+r"][2][self.i])+']"
                        else:
                            self.static[k] += r"\\pscircle*[linecolor=black,fillcolor=black"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){'+n2t("+kparam+")+'}"
                elif cmd == "circle*":
                    if kparam == "":
                        kparam = "1.5"
                    self.radius[k] = kparam
                    if (self.time_dependent)|(self.mov[k]):
                        if self.dim[k] == 3:
                            if "shadows" in list(self.cine[k].keys()):
                                if "x" in self.cine[k]["shadows"]:
                                    self.shadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planX]"
                                if "y" in self.cine[k]["shadows"]:
                                    self.shadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planY]"
                                if "z" in self.cine[k]["shadows"]:
                                    self.shadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planZ]"
                            self.objects[k] += r"\\psSolid[object=sphere,linewidth=0.2pt,r='+n2t("+kparam+")+',fillcolor=cadetblue,action=draw**"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                        else:
                            self.objects[k] += r"\\pscircle*[linecolor=cadetblue,fillcolor=cadetblue"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){'+n2t("+kparam+")+'}"
                    else:
                        if self.dim[k] == 3:
                            if "shadows" in list(self.cine[k].keys()):
                                if "x" in self.cine[k]["shadows"]:
                                    self.sshadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planX]"
                                if "y" in self.cine[k]["shadows"]:
                                    self.sshadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planY]"
                                if "z" in self.cine[k]["shadows"]:
                                    self.sshadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planZ]"
                            self.static[k] += r"\\psSolid[object=sphere,linewidth=0.2pt,r='+n2t("+kparam+")+',fillcolor=cadetblue,action=draw**"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                        else:
                            self.static[k] += r"\\pscircle*[linecolor=cadetblue,fillcolor=cadetblue"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){'+n2t("+kparam+")+'}"
                elif cmd == "circle":
                    if kparam == "":
                        kparam = "1.5"
                    self.radius[k] = kparam
                    if (self.time_dependent)|(self.mov[k]):
                        if self.dim[k] == 3:
                            if "shadows" in list(self.cine[k].keys()):
                                if "x" in self.cine[k]["shadows"]:
                                    self.shadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planX]"
                                if "y" in self.cine[k]["shadows"]:
                                    self.shadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planY]"
                                if "z" in self.cine[k]["shadows"]:
                                    self.shadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planZ]"
                            self.objects[k] += r"\\psSolid[object=sphere,linewidth=0.2pt,r='+n2t("+kparam+")+',linecolor=cadetblue,action=draw"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                        else:
                            self.objects[k] += r"\\pscircle[linecolor=cadetblue"+cparam+"]('+n2t((self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){'+n2t("+kparam+")+'}"
                    else:
                        if self.dim[k] == 3:
                            if "shadows" in list(self.cine[k].keys()):
                                if "x" in self.cine[k]["shadows"]:
                                    self.sshadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planX]"
                                if "y" in self.cine[k]["shadows"]:
                                    self.sshadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][2][self.i])+' '+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planY]"
                                if "z" in self.cine[k]["shadows"]:
                                    self.sshadows[k] += r"\\psProjection[object=cercle,args='+n2t(self.__rp__["+str(k)+r"][0][self.i])+' '+n2t(self.__rp__["+str(k)+r"][1][self.i])+' '+n2t("+kparam+")+',fillstyle=solid,linecolor=black!50,fillcolor=black!50,opacity=0.33,plan=planZ]"
                            self.static[k] += r"\\psSolid[object=sphere,linewidth=0.2pt,r='+n2t("+kparam+")+',linecolor=cadetblue,action=draw"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                        else:
                            self.static[k] += r"\\pscircle[linecolor=cadetblue"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){'+n2t("+kparam+")+'}"
                elif cmd == "box*":
                    default = [ "1.5", "0" ]
                    tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                    tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                    kparam = arguments("{" + tmp1 + "}", 0, "{}")
                    for i, param in enumerate(kparam):
                        if param != "":
                            default[i] = param
                    self.radius[k] = default[0]
                    if (self.time_dependent)|(self.mov[k]):
                        if self.dim[k] == 3:
                            self.objects[k] += r"\\psSolid[object=cube,linewidth=0.2pt,a='+n2t("+default[0]+")+',RotX='+n2t("+default[1]+")+',fillcolor=cadetblue,action=draw**"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                        else:
                            self.objects[k] += r"\\rput{'+n2t("+default[1]+")+'}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){\\psframe*[linecolor=cadetblue,fillcolor=cadetblue"+cparam+"]('+n2t(-"+default[0]+")+','+n2t(-"+default[0]+")+')('+n2t("+default[0]+")+','+n2t("+default[0]+")+')}"
                    else:
                        if self.dim[k] == 3:
                            self.static[k] += r"\\psSolid[object=cube,linewidth=0.2pt,a='+n2t("+default[0]+")+',RotX='+n2t("+default[1]+")+',fillcolor=cadetblue,action=draw**"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                        else:
                            self.static[k] += r"\\rput{'+n2t("+default[1]+")+'}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){\\psframe*[linecolor=cadetblue,fillcolor=cadetblue"+cparam+"]('+n2t(-"+default[0]+")+','+n2t(-"+default[0]+")+')('+n2t("+default[0]+")+','+n2t("+default[0]+")+')}"
                elif cmd == "box":
                    default = [ "1.5", "0" ]
                    tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                    tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                    kparam = arguments("{" + tmp1 + "}", 0, "{}")
                    for i, param in enumerate(kparam):
                        if param != "":
                            default[i] = param
                    self.radius[k] = default[0]
                    if (self.time_dependent)|(self.mov[k]):
                        if self.dim[k] == 3:
                            self.objects[k] += r"\\psSolid[object=cube,linewidth=0.2pt,a='+n2t("+default[0]+")+',RotX='+n2t("+default[1]+")+',linecolor=cadetblue,action=draw"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t((self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                        else:
                            self.objects[k] += r"\\rput{"+default[1]+"}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){\\psframe[linecolor=cadetblue"+cparam+"]('+n2t(-"+default[0]+")+','+n2t(-"+default[0]+")+')('+n2t("+default[0]+")+','+n2t("+default[0]+")+')}"
                    else:
                        if self.dim[k] == 3:
                            self.static[k] += r"\\psSolid[object=cube,linewidth=0.2pt,a='+n2t("+default[0]+")+',RotX='+n2t("+default[1]+")+',linecolor=cadetblue,action=draw"+cparam+"]('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+')"
                        else:
                            self.static[k] += r"\\rput{"+default[1]+"}('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){\\psframe[linecolor=cadetblue"+cparam+"]('+n2t(-"+default[0]+")+','+n2t(-"+default[0]+")+')('+n2t("+default[0]+")+','+n2t("+default[0]+")+')}"
                elif cmd == "put":
                    kparam = "{" + kparam + "}"
                    iargs = iarguments(kparam, 0, paren = "{}")
                    if iargs != [-1]:
                        if k == -1:
                            self.bgputs += kparam[iargs[-2]+1:iargs[-1]] + r"\\newline "
                            self.bgputsmov |= self.time_dependent
                        else:
                            niargs = len(iargs) - 1
                            if cparam == "":
                                str_block = "[bl]"
                            elif cparam == ",c":
                                str_block = ""
                            else:
                                str_block = r"["+cparam[1:]+r"]"
                            if pparam == "":
                                pparam = 1
                            else:
                                pparam = eval(eval("'"+pparam+"'"))
                            if niargs == 1:
                                str_block += "{0}"
                            elif niargs == 2:
                                str_block += "{"+kparam[iargs[0]+1:iargs[1]]+"}"
                            if (self.time_dependent)|(self.mov[k]):
                                if self.dim[k] == 3:
                                    self.puts += 1
                                    self.objects[k] += r"\\psPoint('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+'){PUT"+str(self.puts)+r"}{\\rput"+str_block+r"(PUT"+str(self.puts)+r"){"+kparam[iargs[-2]+1:iargs[-1]]+"}}"
                                else:
                                    self.objects[k] += r"\\rput"+str_block+r"('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){"+kparam[iargs[-2]+1:iargs[-1]]+"}"
                            else:
                                if self.dim[k] == 3:
                                    self.puts += 1
                                    self.static[k] += r"\\psPoint('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+','+n2t(self.__rp__["+str(k)+r"][2][self.i])+'){PUT"+str(self.puts)+r"}{\\rput"+str_block+r"(PUT"+str(self.puts)+r"){"+kparam[iargs[-2]+1:iargs[-1]]+"}}"
                                else:
                                    self.static[k] += r"\\rput"+str_block+r"('+n2t(self.__rp__["+str(k)+r"][0][self.i])+','+n2t(self.__rp__["+str(k)+r"][1][self.i])+'){"+kparam[iargs[-2]+1:iargs[-1]]+"}"
                elif cmd == "plot":
                    tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                    #tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                    tmp1 = regexp.sub("t($|[\)\]\}\+\-\*/ ,\:=])", "(self.start + self.i*self.lap)\\1", tmp0)
                    if tmp0 != tmp1:
                        self.time_dependent = True
                    if self.dim_max == 3:
                        tmp1 = regexp.sub("x($|[\)\]\}\+\-\*/ ,\:=])", "((x-self.origin3d[0])/self.ref_width/"+str(self.unit)+"+"+str(self.min[0])+")\\1", tmp1)
                        tmp1 = regexp.sub("y($|[\)\]\}\+\-\*/ ,\:=])", "((y-self.origin3d[1])/self.ref_width/"+str(self.unit)+"+"+str(self.min[1])+")\\1", tmp1)
                        if pparam == "":
                            pparam = "('+n2t(self.origin[self.k][0])+','+n2t(self.origin[self.k][1])+')('+n2t(self.ref_width*self.unit*(self.max[0] -self.min[0])+self.origin[self.k][0])+','+n2t(self.ref_width*self.unit*(self.max[1] -self.min[1])+self.origin[self.k][1])+')"
                        kparam = "{'+str(rounds(self.ref_width*"+str(self.unit)+"*("+tmp1+"-self.orig_center[2])+self.origin3d[2],3)).replace(\"**\",\"^\")+'}"
                        if self.time_dependent:
                            self.objects[k] += r"\\psSurface[algebraic,ngrid=.5 .5,linewidth=0.2pt,incolor=yellow,hue= .07 .2"+cparam+"]"+pparam+kparam
                        else:
                            self.static[k] += r"\\psSurface[algebraic,ngrid=.5 .5,linewidth=0.2pt,incolor=yellow,hue= .07 .2"+cparam+"]"+pparam+kparam
                    else:
                        tmp1 = regexp.sub("x($|[\)\]\}\+\-\*/ ,\:=])", "((x-self.origin2d[0])/self.ref_width/"+str(self.unit)+"+"+str(self.min[0])+")\\1", tmp1)
                        if pparam == "":
                            pparam = "{'+n2t(self.origin[self.k][0])+'}{'+n2t(self.ref_width*self.unit*(self.max[0] -self.min[0])+self.origin[self.k][0])+'}"
                        else:
                            pparam = pparam.replace("(","{").replace(")","}")
                        kparam = "{'+str(rounds(self.ref_width*"+str(self.unit)+"*("+tmp1+"-self.orig_center[1])+self.origin2d[1],3)).replace(\"**\",\"^\")+'}"
                        if self.time_dependent:
                            self.objects[k] += r"\\psplot[linecolor=blue,algebraic=true,plotpoints=1000,yMaxValue='+n2t(self.pmmax[1])+',yMinValue='+n2t(self.pmmin[1])+'"+cparam+"]"+pparam+kparam
                        else:
                            self.static[k] += r"\\psplot[linecolor=blue,algebraic=true,plotpoints=1000,yMaxValue='+n2t(self.pmmax[1])+',yMinValue='+n2t(self.pmmin[1])+'"+cparam+"]"+pparam+kparam
                elif cmd == "curve":
                    self.curves += 1
                    tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                    tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                    tmp1 = arguments("{" + tmp1 + "}", 0, "{}")
                    kparam = ""
                    for i in range(len(tmp1)):
                        kparam += "{'+str(rounds(self.ref_width*"+str(self.unit)+"*("+tmp1[i]+"-self.orig_center["+str(i)+"])+self.origin3d["+str(i)+"],3)).replace(\"**\",\"^\")+'}"
                    if self.time_dependent:
                        if self.dim_max == 3:
                            self.objects[k] += r"\\defFunction[algebraic]{CURVE"+str(self.curves)+"}(s)"+kparam+r"\\psSolid[object=courbe,r=0,resolution=360,linecolor=palatinateblue"+cparam+",function=CURVE"+str(self.curves)+"]"
                    else:
                        if self.dim_max == 3:
                            self.static[k] += r"\\defFunction[algebraic]{CURVE"+str(self.curves)+"}(s)"+kparam+r"\\psSolid[object=courbe,r=0,resolution=360,linecolor=palatinateblue"+cparam+",function=CURVE"+str(self.curves)+"]"
                elif cmd == "field":
                    if pparam == "":
                        pparam = "-10"
                    tmp0 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", _repl_val_wtu_, kparam)
                    tmp1 = regexp.sub("([a-zA-Z_][a-zA-Z_0-9]*)($|[\)\]\}\+\-\*/ ,\:=])", self._repl_str_, tmp0)
                    if self.time_dependent:
                        if self.dim_max == 3:
                            self.objects[k] += r"\\multido{\\nA=-10+5}{5}{\\multido{\\nB=-10+5}{5}{\\psSolid[object=vecteur,args={'+n2t(self.a_vars2pic[0](("+tmp1+r")[0]))+' '+n2t(self.a_vars2pic[1](("+tmp1+r")[1]))+' '+n2t(self.a_vars2pic[2](("+tmp1+r")[2]))+' [0.35 1.5]},linecolor=electricblue!80,opacity=0.7](\\nA, \\nB, "+pparam+")}}"
                    else:
                        if self.dim_max == 3:
                            self.static[k]  += r"\\multido{\\nA=-10+5}{5}{\\multido{\\nB=-10+5}{5}{\\psSolid[object=vecteur,args={'+n2t(self.a_vars2pic[0](("+tmp1+r")[0]))+' '+n2t(self.a_vars2pic[1](("+tmp1+r")[1]))+' '+n2t(self.a_vars2pic[2](("+tmp1+r")[2]))+' [0.35 1.5]},linecolor=electricblue!80,opacity=0.7](\\nA, \\nB, "+pparam+")}}"
                else:
                    if (self.time_dependent)|(self.mov[k]):
                        self.objects[k] += subject
                    else:
                        self.static[k] += subject
        else:
            # Fuerzas: deben insertarse antes de ejecutar .evol
            # Extracción de unidades
            def get_unit(list_expr):
                has_units = False
                for expr in list_expr:
                    if (expr != 0)&(hasattr(expr, "atoms")):
                        if len(expr.atoms(un.Unit)) != 0:
                            has_units = True
                            break
                if not has_units:
                    return ""
                expr = factor(expr.subs({Symbol('x'):um, Symbol('y'):um, Symbol('z'):um, Symbol('v_x'):um/us, Symbol('v_y'):um/us, Symbol('v_z'):um/us, Symbol('a_x'):um/us**2, Symbol('a_y'):um/us**2, Symbol('a_z'):um/us**2, Symbol('t'):us}))
                if isinstance(expr, Mul):
                    units = 1
                    for arg in expr.args:
                        if isinstance(arg, Pow):
                            if isinstance(arg.base, un.Unit):
                                units *= arg
                        elif isinstance(arg, un.Unit):
                            units *= arg
                else:
                    units = expr
                return latex(physics_format(units))
            for subject in subjects:
                # Nombre del comando.
                cmd = ""
                pos = 0
                nsubject = len(subject)
                while not subject[pos] in "({[\\":
                    cmd += subject[pos]
                    pos += 1
                    if pos == nsubject:
                        break
                # Obtenemos las coordenadas.
                begin, end = delim(subject, len(cmd))
                params = eval(subject[begin:end+1], globals())
                self.Funit[k].append(get_unit(params))
                params = [ erase_units(param) for param in params ]
                self.F[k].append([])
                for param in params:
                    self.F[k][-1].append(param)
                self.Fname[k].append(cmd)
                # Obtenemos los parámetros.
                params = arguments(subject, end + 1, "[]")
                if params == [-1]:
                    nparams = 0
                else:
                    nparams = len(params)
                if nparams > 0:
                    self.scale = eval(params[0])
                self.Fscal[k].append(self.scale)
                if nparams <= 1:
                    tmpalig = 1.5
                else:
                    tmpalig = eval(params[1])*1.5
                if tmpalig < 0:
                    tmpalig -= 1
                self.Falig[k].append(tmpalig)
# Runge-Kutta con las funciones suministradas como parámetros.
class RK4:
    """
    Integra un sistema de ecuaciones diferenciales de primer grado.

    Las ecuaciones se darán como una lista de funciones.

    RK4(lap, functions, initials)
    
    - lap       - Diferencial con el que se integrará.
    - functions - Lista de funciones del sistema de ecuaciones diferenciales.
                    El primer parámetro de las funciones siempre es el tiempo.
    - initials  - Valores iniciales de las variables.
                    La primera variable de la lista siempre es el tiempo.

    Ejemplo 1
    =========

    Integra la ecuación diferencial: dx/dt = x
    con la condición initial: t, x = 0, 1
    cuyo resultado es: x = exp(t)

    >>> num = RK4(0.001, [ lambda t, x: x ], [0, 1])
    >>> num.iterate(3000)
    >>> import matplotlib.pyplot as plt
    >>> plt.plot(*num.x)
    [<matplotlib.lines.Line2D object at 0x7fa710ff9ac8>]
    >>> plt.show()

    Ejemplo 2
    =========

    Integra el sistema: dx/dt = y, dy/dt = -x
    con la condición inicial: t, x, y = 0, 1, 0
    cuyo resultado es: x = cos(t), y = sin(t)

    >>> num = RK4(0.001, [ lambda t, x, y: y, lambda t, x, y: -x ], [0, 1, 0])
    >>> num.iterate(10000)
    >>> from mpl_toolkits.mplot3d import Axes3D
    >>> from matplotlib import rcParams
    >>> import matplotlib.pyplot as plt
    >>> fig = plt.figure()
    >>> ax = fig.gca(projection='3d')
    >>> ax.plot(num.x[1], num.x[2], num.x[0], 
    ...         label = 'Curva paramétrica',
    ...         color = 'DarkMagenta',
    ...         linewidth = 3.2,
    ...         linestyle = '-'             # alternativas - -- -. :
    ...         )
    [<mpl_toolkits.mplot3d.art3d.Line3D object at 0x7fdda7607a90>]
    >>> rcParams['legend.fontsize'] = 11
    >>> ax.legend()
    <matplotlib.legend.Legend object at 0x7fdd9ff829e8>
    >>> ax.set_xlabel('x')
    <matplotlib.text.Text object at 0x7fdd9ff43198>
    >>> ax.set_xlim(-1.2, 1.2)
    (-1.2, 1.2)
    >>> ax.set_ylabel('y')
    <matplotlib.text.Text object at 0x7fdd9ff4ddd8>
    >>> ax.set_ylim(-1.2, 1.2)
    (-1.2, 1.2)
    >>> ax.set_zlabel('t')
    <matplotlib.text.Text object at 0x7fdd9ff547f0>
    >>> ax.set_zlim(0, 10)
    (0, 10)
    >>> ax.set_title('Integración', va='bottom')
    <matplotlib.text.Text object at 0x7fdd9ff63a58>
    >>> ax.view_init(elev=8, azim=-57)
    >>> ax.dist=9
    >>> plt.show()


    Ejemplo 3
    =========

    Atractor de Lorenz

    >>> a = 10
    >>> b = 28
    >>> c = 8/3
    >>> 
    >>> num = RK4(0.001, [
    ... lambda t, x, y, z: a*(y - x) ,
    ... lambda t, x, y, z: x*(b - z) - y ,
    ... lambda t, x, y, z: x*y - c*z
    ... ], [0, 2, 2, 2])
    >>> num.iterate(50000)
    >>> 
    >>> from mpl_toolkits.mplot3d import Axes3D
    >>> from matplotlib import rcParams
    >>> import matplotlib.pyplot as plt
    >>> 
    >>> fig = plt.figure()
    >>> ax = fig.gca(projection='3d')
    >>> ax.plot(num.x[1], num.x[2], num.x[3], 
    ...         label = 'Curva paramétrica',
    ...         color = 'Red',
    ...         linewidth = 1.1,
    ...         linestyle = '-'             # alternativas - -- -. :
    ...         )
    [<mpl_toolkits.mplot3d.art3d.Line3D object at 0x7fe95bc8c080>]
    >>> rcParams['legend.fontsize'] = 11
    >>> 
    >>> ax.legend()
    <matplotlib.legend.Legend object at 0x7fe954011b70>
    >>> ax.set_xlabel('x')
    <matplotlib.text.Text object at 0x7fe9540552e8>
    >>> ax.set_xlim(min(num.x[1]), max(num.x[1]))
    (-17.499147938424173, 19.239520723644926)
    >>> ax.set_ylabel('y')
    <matplotlib.text.Text object at 0x7fe95405ff28>
    >>> ax.set_ylim(min(num.x[2]), max(num.x[2]))
    (-23.244844690515738, 26.53721291767171)
    >>> ax.set_zlabel('z')
    <matplotlib.text.Text object at 0x7fe954064940>
    >>> ax.set_zlim(min(num.x[3]), max(num.x[3]))
    (1.9917108178406806, 47.170421907945084)
    >>> ax.set_title('Atractor de Lorenz', va='bottom')
    <matplotlib.text.Text object at 0x7fe954075ba8>
    >>> 
    >>> ax.view_init(elev=8, azim=-42)
    >>> ax.dist=9
    >>> plt.show()
    """
    def __init__(self, lap, functions, initials):
        self.i = 0
        self.lap = lap
        self.dim = len(functions) + 1
        if self.dim != len(initials):
            sys.exit("RK4: Requerido un valor inicial más que ecuaciones (para el tiempo). Eq: "+str(len(functions))+" Ini: "+str(len(initials)) )
        self.x = [ [float(initials[i])] for i in range(self.dim) ]
        self.functions = functions
    # Primer punto de Runge-Kutta.
    def rk0(self, fun, *x):
        return float(self.functions[fun-1](*x))
    # Segundo punto de Runge-Kutta.
    def rk1(self, fun, *x):
        result = [ fun ] + [ x[0] + self.lap/2 ] + [ x[i] + self.lap/2.*self.rk0(i, *x) for i in range(1, self.dim) ]
        return self.rk0(*result)
    # Tercer punto de Runge-Kutta.
    def rk2(self, fun, *x):
        result = [ fun ] + [ x[0] + self.lap/2 ] + [ x[i] + self.lap/2.*self.rk1(i, *x) for i in range(1, self.dim) ]
        return self.rk0(*result)
    # Cuarto punto de Runge-Kutta.
    def rk3(self, fun, *x):
        result = [ fun ] + [ x[0] + self.lap ] + [ x[i] + self.lap*self.rk2(i, *x) for i in range(1, self.dim) ]
        return self.rk0(*result)
    # Calculo de iteraciones
    def iterate(self, points):
        for self.i in range(self.i, self.i + points):
            x = [ self.x[j][-1] for j in range(self.dim) ]
            # Cálculo de la siguiente iteración.
              # Siguiente iteración temporal.
            self.x[0].append(x[0] + self.lap)
              # Siguiente iteración espacial.
            for i in range(1, self.dim):
                self.x[i].append(x[i] + self.lap/6.*(self.rk0(i, *x) + 2.*self.rk1(i, *x) + 2.*self.rk2(i, *x) + self.rk3(i, *x)))
#            # Aplicamos la corrección de ligadura.
#            if self.dh != None:
#                for j in range(4):
#                    x = [ self.x[j][-1] for j in range(self.dim) ]
#                    for i in range(self.dim):
#                        self.x[i][-1] += self.dh(*x)[i]/4
class ODE:
    """
    Integra un sistema de ecuaciones diferenciales de primer grado.

    Las ecuaciones se darán como una lista de funciones.
    """
    def __init__(self, lap, f, initials, jac = None, integrator = 'vode', method = 'adams'):
        self.i = 0
        self.lap = lap
        self.dim = len(initials)
        self.x = [ [float(initials[i])] for i in range(self.dim) ]
        # Preparación de integrador.
        if integrator in ['dopri5', 'dop853']:
            jac = None
        self.f = f
        self.jac = jac
        self.integrator = integrator
        self.method = method
        self.__odeinit__()
    def __odeinit__(self):
        self.r = ode(self.f, self.jac)
        if self.integrator in ['vode', 'zvode']:
            if self.jac == None:
                self.r.set_integrator(self.integrator, method = self.method)
            else:
                self.r.set_integrator(self.integrator, method = self.method, with_jacobian = True)
        else:
            if self.jac == None:
                self.r.set_integrator(self.integrator)
            else:
                self.r.set_integrator(self.integrator, with_jacobian = True)
        self.r.set_initial_value([ self.x[i+1][-1] for i in range(self.dim-1) ], self.x[0][-1])
    def iterate(self, points):
        for self.i in range(self.i, self.i + points):
            # Cálculo de la siguiente iteración.
            # Siguiente iteración temporal.
            self.x[0].append(self.x[0][-1] + self.lap)
            self.r.integrate(self.x[0][-1])
            if not self.r.successful():
                sys.exit("ODE: Error al integrar.")
            # Siguiente iteración espacial:
            for i in range(1, self.dim):
                self.x[i].append(float(self.r.y[i-1]))
#############################################################
#                 Funciones para impresión
#############################################################
def lp(expr, *params):
    import __main__
    if "__physics__" in dir(__main__):
        simplify_units = __main__.__physics__
    else:
        simplify_units = __physics__
    dicti = {}
    split = 0
    fmt = ""
    for param in params:
        if isinstance(param, bool):
            simplify_units = param
        elif isinstance(param, dict):
            dicti = param
        elif isinstance(param, int):
            split = param
        elif isinstance(param, str):
            fmt = param
#    # Redondea antes del trabajo con unidades.
#    if isinstance(expr, dict):
#        Expr = srepr(expr.values())
#        if "Float(" in Expr:
#            expr = {k: expand(v.evalf(__digits__)) for k, v in expr.items() }
#    else:
#        Expr = srepr(expr)
#        if "Float(" in Expr:
#            if isinstance(expr, list):
#                expr = [ expand(v.evalf(__digits__)) for v in expr ]
#            else:
#                expr = expand(expr.evalf(__digits__))
    # Opera las unidades.
    if simplify_units:
        expr = physics_format(expr, dicti)
#    # Combierte las unidades en un bloque para evitar problemas.
#    expr = freeze_units(expr)
    # Combierte a latex
    output = latexsy(expr, dicti)
    # Parte las matrices demasiado anchas.
    if split > 0:
        output = split_mat(output, split)
    if fmt == "newline":
        output = output + "\n"
    sys.stdout.write(output)
def p(*params):
    sys.stdout.write(" ".join(map(str,params)))
def ep(*params):
    sys.stderr.write(" ".join(map(str,params)) + "\n")
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
#######                    Comienzo del programa                     #######
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
############################################################################
# El programa sólo se ejecuta con parámetros.
if len(sys.argv) > 1:
    import traceback
    import os.path
    #from pyparsing import nestedExpr
    R = Rational
    seed(31415926)
    # Valores iniciales de las variables.
    __e__ = False
    _infile_ = ""
    _outfile_ = ""
    _ssep_ = "««"
    _nsi_ = len(_ssep_)
    _esep_ = "»»"
    _nei_ = len(_esep_)
    _nline_ = 0
    # Procesado de parametros.
    for _param_ in sys.argv[1:]:
        if ".ptx" == _param_[-4:]:
            _infile_ = _param_
        elif (".ltx" == _param_[-4:])|(".tex" == _param_[-4:])|("-" == _param_):
            _outfile_ = _param_
        elif os.path.isfile(_param_ + ".ptx"):
            _infile_ = _param_ + ".ptx"
    if _infile_ == "":
        sys.exit("\nError: fichero origen sin expecificar.")
    if _outfile_ == "":
        _outfile_ = _infile_[:-4] + ".ltx"
    if not os.path.isfile(_infile_):
        sys.exit("\nError: no existe el fichero origen.")
    _abs_dir_ = os.path.dirname(os.path.abspath(_infile_))
    # Preparacion de salida.
    class Text:
        def __init__(self, file):
            self.stdout = file
        def write(self, text):
            self.stdout.write(text)
        def flush(self): # Requerido por python.
            pass
    #############################################################
    #            Salida estandar a fichero
    #############################################################
    if not _outfile_ in "-+":
        _wf_ = open(_outfile_, "w")
        sys.stdout = Text(_wf_)
    #############################################################
    #############################################################
    #############################################################
    #                 Apertura de ficheros.
    #############################################################
    #############################################################
    #############################################################
    def document(_file):
        global _abs_dir_
        _found = False
        for _rel in [ "", _abs_dir_ ]:
            for _ext in [ "", ".ptx", ".ltx", ".tex" ]:
                if os.path.isfile(os.path.join(_rel, _file + _ext)):
                    _file = os.path.join(_rel, _file + _ext)
                    _found = True
                    break
            if _found:
                break
        if not _found:
            sys.exit("\nError: document: no existe fichero\n" + _abs_dir_ + "/" + _file)
        if ".ptx" != _file[-4:]:
            _rlf = open(_file, "r")
            _tmp = _rlf.readline()
            while (_tmp != "")&("\\begin{document}\n" != _tmp):
                _tmp = _rlf.readline()
            _tmp = _rlf.readline()
            while (_tmp != "")&("\\end{document}\n" != _tmp):
                sys.stdout.write(_tmp)
                _tmp = _rlf.readline()
            _rlf.close()
        else:
            print("\n"*4)
            print(("\n" + "%"*60)*3)
            print("%"*4 + "  Archivo:  " + _file)
            print(("%"*60 + "\n")*2)
            print("\n"*2)
            py2ltx(_file)
    #############################################################
    #############################################################
    #############################################################
    #                   Función de proceso.
    #############################################################
    #############################################################
    #############################################################
    def py2ltx(_infile_):
        global __e__, _ssep_, _nsi_, _esep_, _nei_, _nline_
        _rf_ = open(_infile_, "r")
        _line_ = _rf_.readline()
        _nline_+=1
        while _line_ != "":
            _si_ = _line_.find(_ssep_)
            if _si_ != -1:
                _out_ = _line_[0:_si_]
                sys.stdout.write(_out_)
                _line_ = _line_[_si_ + _nsi_:]
                _ei_ = _line_.find(_esep_)
                _si_ = _line_.find(_ssep_)
                if ((_si_ < _ei_)|(_ei_ == -1))&(_si_ != -1):
                    sys.exit("\nError: entorno sin cerrar en línea " + str(_nline_))
                if _ei_ != -1:
                    # Comandos Python en una sola línea.
                    _out_ = _line_[0:_ei_].lstrip(" ").rstrip(" ")
                    _lpc_ = _out_.rfind(";")
                    _lcd_ = _out_[_lpc_+1:].lstrip(" ")
                    if _lcd_ != "":
                        if (regexp.match("lp *\(", _lcd_) == None)&(regexp.match(" *#", _lcd_) == None)&(regexp.search("=[^=]", _lcd_) == None):
                            if regexp.match("co\[['\"_a-zA-Z0-9]+\]", _lcd_) == None:
                                _opt_ = ")"
                            else:
                                _opt_ = ",False)"
                            if _lcd_ == _out_:
                                _out_ = "lp(" + _out_ + _opt_
                            else:
                                _out_ = _out_[:_lpc_] + ";lp(" + _lcd_ + _opt_
                    try:
                        exec(_out_, globals())
                    except:
                        __e__ = True
                        sys.stderr.write("\nError archivo " + _infile_ + " línea " + str(_nline_) + "\n>>> " + _out_)
                        sys.stderr.write("\n" + traceback.format_exc())
                    _line_ = _line_[_ei_ + _nei_:]
                else:
                    # Comandos Python en varias líneas.
                    _out_ = _line_
                    _line_ = _rf_.readline()
                    _nline_+=1
                    _ei_ = _line_.find(_esep_)
                    while _ei_ == -1:
                        if _line_ == "":
                            sys.exit("\nError: entorno sin cerrar al final del fichero")
                        _si_ = _line_.find(_ssep_)
                        if _si_ != -1:
                            sys.exit("\nError: entorno sin cerrar en línea " + str(_nline_))
                        _out_ = _out_ + _line_
                        _line_ = _rf_.readline()
                        _nline_+=1
                        _ei_ = _line_.find(_esep_)
                    _out_ = _out_ + _line_[:_ei_]
                    try:
                        exec(_out_, globals())
                    except:
                        __e__ = True
                        sys.stderr.write("\nError archivo " + _infile_ + " línea " + str(_nline_) + "\n>>> " + _out_)
                        sys.stderr.write("\n" + traceback.format_exc())
                    _line_ = _line_[_ei_ + _nei_:]
            else:
    #            if _line_.lstrip() != "":
                sys.stdout.write(_line_)
                _line_ = _rf_.readline()
                _nline_+=1
        _rf_.close()
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #                Cabecera y macros de latex.
    #############################################################
    #############################################################
    #############################################################
    if _outfile_ != "-":
        __path__ = os.path.realpath(os.path.dirname(sys.argv[0]))
        __path__ = __path__[:__path__.rfind("/")]
        __model_ltx__ = open(__path__+"/latex/modelo.ltx", "r")
        for line in __model_ltx__:
            print(line, end="")
    print(r"\begin{document}")
    print(r"")
    py2ltx(_infile_)
    print(r"")
    print(r"\end{document}")
    if not _outfile_ in "-+":
        _wf_.close()
    FNULL.close()
    if __e__:
        sys.exit("Error: Se han producido errores.")
    else:
        sys.stderr.write("% Python-Sympy -> LaTeX success.\n")
