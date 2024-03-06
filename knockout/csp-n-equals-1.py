from constraint import Problem
from functools import partial
from strategy import FoxStrategy


def sum_constraint(a,b,c):
    return a + b + c == 3

def objective_function(values):
    fs = FoxStrategy()
    fs.add_itr(values['r'],values['f'],values['e'])
    return fs.calc_linear_programming_score(t_fox=7.43199,b_fox=14)

problem = Problem() 

problem.addVariable('r', [1])
problem.addVariable('f', [0,1,2,3])
problem.addVariable('e', [0,1,2])

problem.addConstraint(sum_constraint, ('r', 'f', 'e'))

objective_function_partial = partial(objective_function)

best_solution = None
best_value = float('-inf')

for solution in problem.getSolutionIter():
    print(solution)
    current_value = objective_function_partial(solution)
    print(current_value)
    if current_value > best_value:
        best_value = current_value
        best_solution = solution

print("Best Solution:", best_solution)
print("Maximized Objective Value:", best_value)