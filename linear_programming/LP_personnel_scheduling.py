"""
A simple personnel scheduling LP problem from the operation research course on Coursera
Link: https://www.coursera.org/learn/operations-research-modeling/lecture/Vm9yl/2-13-computers-example-2-personnel-scheduling

problem formulation

min x1 + x2 + x3 + x4 + x5 + x6 + x7
s.t.
x1 + x4 + x5 + x6 + x7 >= 110
x1 + x2 + x5 + x6 + x7 >= 80
x1 + x2 + x3 + x6 + x7 >= 150
x1 + x2 + x3 + x4 + x7 >= 30
x1 + x2 + x3 + x4 + x5 >= 70
x2 + x3 + x4 + x5 + x6 >= 160
x3 + x4 + x5 + x6 + x7 >= 120

xi >= 0, for all i in {1,..., 7}

"""

import cvxpy as cp

# Define the variables
x1 = cp.Variable(nonneg=True)  # nonneg=True means x1 >= 0
x2 = cp.Variable(nonneg=True)
x3 = cp.Variable(nonneg=True)
x4 = cp.Variable(nonneg=True)
x5 = cp.Variable(nonneg=True)
x6 = cp.Variable(nonneg=True)
x7 = cp.Variable(nonneg=True)


# Define the constraints
constrainsts = [
    x1 + x4 + x5 + x6 + x7 >= 110,
    x1 + x2 + x5 + x6 + x7 >= 80,
    x1 + x2 + x3 + x6 + x7 >= 150,
    x1 + x2 + x3 + x4 + x7 >= 30,
    x1 + x2 + x3 + x4 + x5 >= 70,
    x2 + x3 + x4 + x5 + x6 >= 160,
    x3 + x4 + x5 + x6 + x7 >= 120,
]

# Define the objective function
obj = cp.Minimize(x1 + x2 + x3 + x4 + x5 + x6 + x7)


# Define the problem
prob = cp.Problem(objective=obj, constraints=constrainsts)

prob.solve()

if prob.status == cp.OPTIMAL:
    print("The problem has been solved successfully.")
    print(f"The optimal varlue of the objective is: {prob.value}")
else:
    print("The problem has not been solved.")
