from pulp import *

def print_matr(H,n,m):
    for i in range(n):
        for j in range(m):
            print(H[i][j], end=' ')
        print()

def enter_matr(n,m):
    H = [[0] * m for i in range(n)]
    print('вводите матрицу по строчно:')
    for i in range(n):
        row = input().split()
        for j in range(m):
            H[i][j] = int(row[j])
    return H

print('введите размер матрицы H:')
print('количество столбцов H:')
m = int(input())
print('количество строк H:')
n = int(input())

H = enter_matr(n, m)
print_matr(H, n, m)
EDGES = []
COSTS = []
for i in range(n):
    EDGES.append((0, 99999))
    COSTS.append(1)
D = []
for i in range(m):
    D.append(1)
X = []
prob = LpProblem("Problem", LpMinimize)
for i in range(n):
    temp_name = 'x'+str(i)
    X.append(LpVariable(temp_name, *EDGES[i]))
prob += lpDot(COSTS, X), "Costs"
for i in range(m):
    temp = 0
    for j in range(n):
        temp += H[j][i]*X[j]
    prob += temp >= D[i]
status = prob.solve()

Ix = 0
for ind, x in enumerate(X):
    Ix += value(x)

Ix = 1/Ix


EDGES = []
COSTS = []
for i in range(m):
    EDGES.append((0, 999999999))
    COSTS.append(1)
D = []
for i in range(n):
    D.append(1)
Y = []
prob = LpProblem("Problem", LpMaximize)
for i in range(m):
    temp_name = 'y'+str(i)
    Y.append(LpVariable(temp_name, *EDGES[i]))
prob += lpDot(COSTS, Y), "Costs"
for i in range(n):
    temp = 0
    for j in range(m):
        temp += H[i][j] * Y[j]
    prob += temp <= D[i]
status = prob.solve()

Iy = 0
for ind, y in enumerate(Y):
    Iy += value(y)

Iy = 1/Iy

print('I = ', Ix)
for ind, x in enumerate(X):
    print('p', end='')
    print(ind+1, ' = ', value(x) * Ix, end='\t\t')
print()
for y in enumerate(Y):
    print('q', end='')
    print(y[0]+1, ' = ', value(y[1]) * Iy, end='\t\t')