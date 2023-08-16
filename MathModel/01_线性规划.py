import scipy.optimize

# 定义目标函数和约束条件
c = [2, 3, -5]
A = [[-2, 5, -1], [1, 3, 1]]
b = [-10, 12]
aeq = [[1, 1, 1]]
beq = [7]
# 求解问题
result = scipy.optimize.linprog(c, A_ub=A, b_ub=b, A_eq=aeq, b_eq=beq)

# 提取最优解和目标函数的最优值
optimal_solution = result.x
optimal_value = result.fun

print("最优解:", optimal_solution)
print("目标函数的最优值:", optimal_value)
