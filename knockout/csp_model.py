from constraint import Problem
from functools import partial
from knockout.fox_strategy_csp import FoxStrategyCSP
from knockout.fox_solutiion_csp import FoxCSPSolution

R_DOMAIN = [0,1]
F_DOMAIN = [0,1,2,3]
E_DOMAIN = [0,1,2]

def single_channel_cstr(a,b,c):
    return a + b + c == 3

def sum_of_fakes_cst(*fakes):
    sum_f = 0
    for f in fakes:
        sum_f += f
    return sum_f <= 12

def one_real_cst(*reals):
    sum_r = 0
    for r in reals:
        sum_r += r
    return sum_r > 0

def objective_function(values,n,t):
    fs = FoxStrategyCSP()
    for i in range(n):
        fs.add_itr(values[f'{i}-r'],values[f'{i}-f'],values[f'{i}-e'])
    return fs.calc_linear_programming_score(t_fox=t,b_fox=14)

def exec(n,t):
    problem = Problem() 
    for i in range(n):
        problem.addVariable(f'{i}-r', R_DOMAIN)
        problem.addVariable(f'{i}-f', F_DOMAIN)
        problem.addVariable(f'{i}-e', E_DOMAIN)
    fakes = [f"{i}-f" for i in range(n)]
    reals = [f"{i}-r" for i in range(n)]
    for i in range(n):
        problem.addConstraint(single_channel_cstr, (f'{i}-r',f'{i}-f',f'{i}-e'))
    problem.addConstraint(sum_of_fakes_cst, fakes)
    problem.addConstraint(one_real_cst, reals)
    objective_function_partial = partial(objective_function,n=n,t=t)
    best_solution = None
    best_value = float('-inf')
    for solution in problem.getSolutionIter():
        current_value = objective_function_partial(solution)
        if current_value > best_value:
            best_value = current_value
            best_solution = solution
    return FoxCSPSolution(best_solution,best_value,n)