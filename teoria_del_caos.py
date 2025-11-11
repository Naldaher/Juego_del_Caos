"""Perturbaciones en sistemas lineales"""
import numpy as np

#Definimos el sistema
A = np.matrix([[1.0, 1.0], [1, 1.0001]])
b = np.array([2.0, 2.0])

print(np.linalg.cond(A,1)) #norma = 1

x1 = np.linalg.solve(A,b) #resuelve el sistema Ax1 = b y devuelve x1
print(x1)

epsilon = 1.e-3 #perturbación
b = np.array([2.0, 2.0+epsilon]) #añadimos a b, epsilon_b

x2 = np.linalg.solve(A,b) #resolvemos el sistema perturbado
print(x2)

print(f"el errores: {np.linalg.norm(x2-x1, 2)} para una perturbación de: {epsilon}")

#Otro

B = np.matrix([[1.0, 1.0], [1.0, -1.0]])
c = np.array([-0.1, 0.9])

x3 = np.linalg.solve(B,c) #devuelve la solucion del sistema sin perturbar
print(x3)

delta = np.array([0.1, 0.1])
c = np.array([-0.1, 0.9]) + delta
x4 = np.linalg.solve(B,c)
print(x4)
