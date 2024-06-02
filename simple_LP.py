"""
This code will solve a simple linear programming problem using the CVXPY library.
The problem description can be found in: https://www.coursera.org/learn/operations-research-modeling/lecture/QM5N0/2-12-computers-the-solver-add-in-and-example-1-producing-desks-and-tables
"""
# problem

"""
max 700x1 + 900x2
s.t.
3x1 + 5x2 <= 3600 (wood)
x1 + 2x2 <= 1600 (labor)
50x1 + 20x2 <= 48000 (machine)
x1 >= 0
x2 >= 0
"""

# using cvxpy
import cvxpy as cp


# Define the variables

x1 = cp.Variable()
x2 = cp.Variable()

# Define the constraints

constraints = [
    3 * x1 + 5 * x2 <= 3600,
    x1 + 2 * x2 <= 1600,
    50 * x1 + 20 * x2 <= 48000,
    x1 >= 0,
    x2 >= 0,
]

# Define the objective function

obj = cp.Maximize(700 * x1 + 900 * x2)


# Solve the problem

prob = cp.Problem(obj, constraints)
prob.solve()

# Print the result
if prob.status == cp.OPTIMAL:
    print("optimal value", prob.value)
    print("optimal var", x1.value, x2.value)
else:
    print("problem not solved")
