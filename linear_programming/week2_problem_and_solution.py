import cvxpy as cp


# variales
x1 = cp.Variable(nonneg=True)
x2 = cp.Variable(nonneg=True)
A, B, C = 9, 1 / 1.1, 1 / 0.7


obj = cp.Maximize(A * x1 + 18 * x2)

constraints = [7 * x1 + 4 * x2 <= 50, B * x1 + C * x2 <= 10]


prob = cp.Problem(objective=obj, constraints=constraints)

prob.solve()
print(x1.value, x2.value)
print(prob.value)
